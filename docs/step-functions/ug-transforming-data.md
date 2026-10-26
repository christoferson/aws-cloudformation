> Source: https://docs.aws.amazon.com/step-functions/latest/dg/transforming-data.html
> Downloaded: 2026-10-26

# Transforming data with JSONata in Step Functions

 With JSONata, you gain a powerful open source query and expression language to select and transform data in your workflows. For a complete JSONata language reference, see the JSONata 2.0.6 documentation. Supported JSONata version

Step Functions implements JSONata based on the 2.0.6 specification. All built-in JSONata functions and operators in the 2.0.6 specification are supported, with one exception: `$eval` is not available—use `$parse` instead. Step Functions also provides additional functions described in JSONata functions.

 The following video describes variables and JSONata in Step Functions with a DynamoDB example:   

 You must opt-in to use the JSONata query and transformation language for existing workflows. When creating a workflow in the console, we recommend choosing JSONata for the top-level state machine `QueryLanguage`. For existing or new workflows that use JSONPath, the console provides an option to convert individual states to JSONata. 

 After selecting JSONata, your workflow fields will be reduced from five JSONPath fields (`InputPath`, `Parameters`, `ResultSelector`, `ResultPath`, and `OutputPath`) to only two fields: `Arguments` and `Output`. Also, you will not use `.$` on JSON object key names. 

 If you are new to Step Functions, you only need to know that JSONata expressions use the following syntax: 

 JSONata syntax: `"{% <JSONata expression> %}"` 

 The following code samples show a conversion from JSONPath to JSONata: 

```
# Original sample using JSONPath
{
  "QueryLanguage": "JSONPath", // Set explicitly; could be set and inherited from top-level
  "Type": "Task",
  ...
  "Parameters": {
    "static": "Hello",
    "title.$": "$.title",
    "name.$": "$customerName",  // With $customerName declared as a variable
    "not-evaluated": "$customerName"
  }
}
  
```

```
# Sample after conversion to JSONata
{
  "QueryLanguage": "JSONata", // Set explicitly; could be set and inherited from top-level
  "Type": "Task",
  ...
  "Arguments": { // JSONata states do not have Parameters
    "static": "Hello",
    "title": "{% $states.input.title %}", 
    "name": "{% $customerName %}",   // With $customerName declared as a variable
    "not-evaluated": "$customerName"
  }
}
  
```

 Given input `{ "title" : "Doctor" }` and variable `customerName` assigned to `"María"`, both state machines will produce the following JSON result: 

```
{
  "static": "Hello",
  "title": "Doctor",
  "name": "María",
  "not-evaluated": "$customerName"
 }
  
```

 In the next diagram, you can see a graphical representation showing how converting JSONPath (left) to JSONata (right) will reduce the complexity of the steps in your state machines:   

 You can (optionally) select and transform data from the state input into Arguments to send to your integrated action. With JSONata, you can then (optionally) select and transform the results from the action for assigning to variables and for state Output. 

 Note: Assign and Output steps occur in parallel. If you choose to transform data during variable assignment, that transformed data will not be available in the Output step. You must reapply the JSONata transformation in the Output step.    

## QueryLanguage field 

 In your workflow ASL definitions, there is a `QueryLanguage` field at the top level of a state machine definition and in individual states. By setting `QueryLanguage` inside individual states, you can incrementally adopt JSONata in an existing state machine rather than upgrading the state machine all at once.  

 The `QueryLanguage` field can be set to `"JSONPath"` or `"JSONata"`. If the top-level `QueryLanguage` field is omitted, it defaults to `"JSONPath"`. If a state contains a state-level `QueryLanguage` field, Step Functions will use the specified query language for that state. If the state does not contain a `QueryLanguage` field, then it will use the query language specified in the top-level `QueryLanguage` field.  

## Writing JSONata expressions in JSON strings 

 When a string in the value of an ASL field, a JSON object field, or a JSON array element is surrounded by `{% %}` characters, that string will be evaluated as JSONata . Note, the string must start with `{%` with no leading spaces, and must end with `%}` with no trailing spaces. Improperly opening or closing the expression will result in a validation error.  

 Some examples:   
 `"TimeoutSeconds" : "{% $timeout %}"`  
 `"Arguments" : {"field1" : "{% $name %}"}` in a `Task` state 
 `"Items": [1, "{% $two %}", 3]` in a `Map` state  
 

 Not all ASL fields accept JSONata. For example, each state’s `Type` field must be set to a constant string. Similarly, the `Task` state’s `Resource` field must be a constant string. The `Map` state `Items` field will accept a JSON array, a JSON object, or a JSONata expression that must evaluate to an array or object.  

## Reserved variable : $states 

 Step Functions defines a single reserved variable called  `$states` . In JSONata states, the following structures are assigned to `$states` for use in JSONata expressions:  

```
# Reserved $states variable in JSONata states
$states = {
  "input":       // Original input to the state
  "result":      // API or sub-workflow's result (if successful)
  "errorOutput": // Error Output (only available in a Catch)
  "context":     // Context object
}
  
```
 

 On state entry, Step Functions assigns the state input to  `$states.input` . The value of `$states.input` can be used in all fields that accept JSONata expressions. `$states.input` always refers to the original state input.  

 For `Task`, `Parallel`, and `Map` states:  
  `$states.result`  refers to the API or sub-workflow’s raw result if successful.  
  `$states.errorOutput`  refers to the Error Output if the API or sub-workflow failed. 

 `$states.errorOutput` can be used in the `Catch` field’s `Assign` or `Output`.  
 

Attempting to access `$states.result` or `$states.errorOutput` in fields and states where they are not accessible will be caught at creation, update, or validation of the state machine.  

The `$states.context` object provides your workflows information about their specific execution, such as `StartTime`, task token, and initial workflow input. To learn more, see Accessing execution data from the Context object in Step Functions . 

## Handling expression errors 

At runtime, JSONata expression evaluation might fail for a variety of reasons, such as:  
 Type error - An expression, such as `{% $x + $y %}`, will fail if `$x` or `$y` is not a number. 
 Type incompatibility - An expression might evaluate to a type that the field will not accept. For example, the field `TimeoutSeconds` requires a numeric input, so the expression `{% $timeout %}` will fail if `$timeout` returns a string. 
 Value out of range - An expression that produces a value that is outside the acceptable range for a field will fail. For example, an expression such as `{% $evaluatesToNegativeNumber %}` will fail in the `TimeoutSeconds` field. 
 Failure to return a result - JSON cannot represent an undefined value expression, so the expression `{% $data.thisFieldDoesNotExist %}` would result in an error. 
 Memory limit exceeded - A JSONata expression that consumes too much memory during evaluation will fail with an `Expression evaluation memory limit exceeded` error. This can occur with expressions that process or transform large amounts of data. To work around this limitation, consider moving the data transformation to a Lambda function. 
 Expression timeout - A JSONata expression that takes longer than 1 second to evaluate will fail with an `Expression evaluation timeout` error. This can occur with expressions that contain infinite loops or very expensive operations. 
 Stack overflow - A JSONata expression that exceeds the maximum recursion depth will fail with a `Stack overflow error`. If the recursion is non-terminating, ensure the function has a correct base case or termination condition. If the recursion terminates but the call stack grows too deep, consider rewriting the function as tail-recursive to reduce stack depth. 
 

In each case, the interpreter will throw the error: `States.QueryEvaluationError`. Your Task, Map, and Parallel states can provide a `Catch` field to catch the error, and a `Retry` field to retry on the error. 

## Converting from JSONPath to JSONata 

 The following sections compare and explain the differences between code written with JSONPath and JSONata.  

### No more path fields 

 ASL requires developers use `Path` versions of fields, as in `TimeoutSecondsPath`, to select a value from the state data when using JSONPath. When you use JSONata, you no longer use `Path` fields because ASL will interpret `{% %}`-enclosed JSONata expressions automatically for you in non-Path fields, such as `TimeoutSeconds`.   
JSONPath legacy example: `"TimeoutSecondsPath": "$timeout"`  
JSONata : `"TimeoutSeconds": "{% $timeout %}"`  
 

 Similarly, the `Map` state `ItemsPath` has been replaced with the `Items` field which accepts a JSON array, a JSON object, or a JSONata expression that must evaluate to an array or object.  

### JSON Objects 

 ASL uses the term payload template to describe a JSON object that can contain JSONPath expressions for `Parameters` and `ResultSelector` field values. ASL will not use the term payload template for JSONata because JSONata evaluation happens for all strings whether they occur on their own or inside a JSON object or a JSON array.  

### No more .$ 

 ASL requires you to append ‘`.$`’ to field names in payload templates to use JSONPath and Intrinsic Functions. When you specify `"QueryLanguage":"JSONata"`, you no longer use the ‘`.$`’ convention for JSON object field names. Instead, you enclose JSONata expressions in `{% %}` characters. You use the same convention for all string-valued fields, regardless of how deeply the object is nested inside other arrays or objects.  

### Arguments and Output Fields 

 When the `QueryLanguage` is set to `JSONata`, the old I/O processing fields will be disabled (`InputPath`, `Parameters`, `ResultSelector`, `ResultPath` and `OutputPath`) and most states will get two new fields: `Arguments` and `Output`.  

 JSONata provides a simpler way to perform I/O transformations compared to the fields used with JSONPath. JSONata’s features makes `Arguments` and `Output` more capable than the previous five fields with JSONPath. These new field names also help simplify your ASL and clarify the model for passing and returning values.  

 The `Arguments` and `Output` fields (and other similar fields such as `Map` state’s `ItemSelector`) will accept either a JSON object such as:  

```
"Arguments": {
    "field1": 42, 
    "field2": "{% jsonata expression %}"
}
  
```
 

 Or, you can use a JSONata expression directly, for example:  

```
"Output": "{% jsonata expression %}"
  
```
 

 Output can also accept any type of JSON value too, for example: `"Output":true`, `"Output":42`.  

 The `Arguments` and `Output` fields only support JSONata, so it is invalid to use them with workflows that use JSONPath. Conversely, `InputPath`, `Parameters`, `ResultSelector`, `ResultPath`, `OutputPath` , and other JSONPath fields are only supported in JSONPath, so it is invalid to use path-based fields when using JSONata as your top level workflow or state query language.  

### Pass state 

 The optional Result in a Pass state was previously treated as the output of a virtual task. With JSONata selected as the workflow or state query language, you can now use the new Output field.  

### Choice state 

 When using JSONPath, choice states have an input `Variable` and numerous comparison paths, such as the following `NumericLessThanEqualsPath` :  

```
# JSONPath choice state sample, with Variable and comparison path
"Check Price": {
  "Type": "Choice",
  "Default": "Pause",
  "Choices": [
  {
    "Variable": "$.current_price.current_price",
    "NumericLessThanEqualsPath": "$.desired_price",
    "Next": "Send Notification"
  } ],
}
  
```
 

 With JSONata, the choice state has a `Condition` where you can use a JSONata expression:  

```
# Choice state after JSONata conversion
"Check Price": {
  "Type": "Choice",
  "Default": "Pause"
  "Choices": [
    {
      "Condition": "{% $current_price <= $states.input.desired_priced %}",
      "Next": "Send Notification"
    } ]
    
  
```
 

 Note: Variables and comparison fields are only available for JSONPath. Condition is only available for JSONata.  

## JSONata examples 

 The following examples can be created in Workflow Studio to experiment with JSONata. You can create and execute the state machines, or use the Test state to pass in data and even modify the state machine definition.  

### Example: Input and Output 

 This example shows how to use `$states.input` to use the state input and the `Output` field to specify the state output when you opt into JSONata.  

```
{
  "Comment": "Input and Output example using JSONata",
  "QueryLanguage": "JSONata",
  "StartAt": "Basic Input and Output",
  "States": {
    "Basic Input and Output": {
      "QueryLanguage": "JSONata",
      "Type": "Succeed",
      "Output": {
        "lastName": "{% 'Last=>' & $states.input.customer.lastName %}",
        "orderValue": "{% $states.input.order.total %}"
      }
    }
  }
}
  
```
 

 When the workflow is executed with the following as input:  

```
{
  "customer": {
    "firstName": "Martha",
    "lastName": "Rivera"
  },
  "order": {
    "items": 7,
    "total": 27.91
  }
}
  
```
 

Test state or state machine execution will return the following JSON output: 

```
{
  "lastName": "Last=>Rivera",
  "orderValue": 27.91
}
  
```
    

### Example: Filtering with JSONata 

 You can filter your data with JSONata Path operators. For example, imagine you have a list of products for input, and you only want to process products that contain zero calories. You can create a state machine definition with the following ASL and test the `FilterDietProducts` state with the sample input that follows.  

 State machine definition for filtering with JSONata  

```
{
  "Comment": "Filter products using JSONata",
  "QueryLanguage": "JSONata",
  "StartAt": "FilterDietProducts",
  "States": {
    "FilterDietProducts": {
      "Type": "Pass",
      "Output": {
        "dietProducts": "{% $states.input.products[calories=0] %}"
      },
      "End": true
    }
  }
}
  
```
 

 Sample input for the test  

```
{
  "products": [
    {
      "calories": 140,
      "flavour": "Cola",
      "name": "Product-1"
    },
    {
      "calories": 0,
      "flavour": "Cola",
      "name": "Product-2"
    },
    {
      "calories": 160,
      "flavour": "Orange",
      "name": "Product-3"
    },
    {
      "calories": 100,
      "flavour": "Orange",
      "name": "Product-4"
    },
    {
      "calories": 0,
      "flavour": "Lime",
      "name": "Product-5"
    }
  ]
}
  
```
 

 Output from testing the step in your state machine  

```
{
    "dietProducts": [
        {
            "calories": 0,
            "flavour": "Cola",
            "name": "Product-2"
        },
        {
            "calories": 0,
            "flavour": "Lime",
            "name": "Product-5"
        }
    ]
}
```
    

### Example: Using previous state output in a Map state 

 This example shows how to use the output of a previous state as input for a Map state with JSONata. The following workflow uses a Pass state to simulate a task that returns an order with a list of items, and then a Map state selects the items array from that output and iterates over it.  

 State machine definition  

```
{
  "Comment": "Example: Using previous state output in a Map state with JSONata",
  "QueryLanguage": "JSONata",
  "StartAt": "GetOrder",
  "States": {
    "GetOrder": {
      "Type": "Pass",
      "Output": {
        "orderId": "{% $states.input.orderId %}",
        "items": "{% $states.input.items %}"
      },
      "Next": "ProcessItems"
    },
    "ProcessItems": {
      "Type": "Map",
      "Items": "{% $states.input.items %}",
      "ItemProcessor": {
        "ProcessorConfig": {
          "Mode": "INLINE"
        },
        "StartAt": "CalculateItemTotal",
        "States": {
          "CalculateItemTotal": {
            "Type": "Pass",
            "Output": {
              "name": "{% $states.input.name %}",
              "total": "{% $states.input.price * $states.input.quantity %}"
            },
            "End": true
          }
        }
      },
      "End": true
    }
  }
}
  
```
 

 In this definition, the `GetOrder` state outputs the order data unchanged. The `ProcessItems` Map state uses `"Items": "{% $states.input.items %}"` to select the `items` array from the output of `GetOrder`. Each iteration receives one item from the array and calculates the item total by multiplying price by quantity.  

 Sample input  

```
{
  "orderId": "ORD-1234",
  "items": [
    {
      "name": "Widget",
      "price": 4.99,
      "quantity": 3
    },
    {
      "name": "Gadget",
      "price": 12.50,
      "quantity": 2
    },
    {
      "name": "Bolt",
      "price": 0.75,
      "quantity": 10
    }
  ]
}
  
```
 

 Expected output  

```
[
  {
    "name": "Widget",
    "total": 14.97
  },
  {
    "name": "Gadget",
    "total": 25
  },
  {
    "name": "Bolt",
    "total": 7.5
  }
]
  
```
 

### Example: Flattening Parallel state output 

 When you use a Parallel state, it returns an array where each element is the output of one branch. With JSONata, you can use the `Output` field on the Parallel state to flatten or merge these results into a single object. This approach replaces the JSONPath `ResultSelector` field.  

 The following example uses a Parallel state with two branches. Each branch simulates a DynamoDB GetItem call by using a Pass state. The Parallel state uses `$merge($states.result)` in its `Output` field to merge the branch results into a single object.  

 State machine definition  

```
{
  "Comment": "Example: Flattening Parallel state output with JSONata",
  "QueryLanguage": "JSONata",
  "StartAt": "GetOrderAndCustomer",
  "States": {
    "GetOrderAndCustomer": {
      "Type": "Parallel",
      "Output": "{% $merge($states.result) %}",
      "Branches": [
        {
          "StartAt": "Get Order",
          "States": {
            "Get Order": {
              "Type": "Pass",
              "Output": {
                "orderId": "{% $states.input.orderId %}",
                "orderDate": "2024-11-20",
                "total": 35.99
              },
              "End": true
            }
          }
        },
        {
          "StartAt": "Get Customer",
          "States": {
            "Get Customer": {
              "Type": "Pass",
              "Output": {
                "customerId": "{% $states.input.customerId %}",
                "customerName": "Martha Rivera",
                "email": "martha@example.com"
              },
              "End": true
            }
          }
        }
      ],
      "Next": "Done"
    },
    "Done": {
      "Type": "Succeed"
    }
  }
}
  
```
 

 Sample input  

```
{
  "orderId": "12345",
  "customerId": "C-100"
}
  
```
 

 Expected output  

```
{
  "orderId": "12345",
  "orderDate": "2024-11-20",
  "total": 35.99,
  "customerId": "C-100",
  "customerName": "Martha Rivera",
  "email": "martha@example.com"
}
  
```
 

 The `$merge()` function combines an array of objects into a single object. If branches return objects with overlapping keys, later array elements take precedence. Branch results are ordered consistently — they correspond to the order of the `Branches` array in the state machine definition.  

## JSONata functions provided by Step Functions 

JSONata contains function libraries for String, Numeric, Aggregation, Boolean, Array, Object, Date/Time, and High Order functions. Step Functions provides additional JSONata functions that you can use in your JSONata expressions. These built-in functions serve as replacements for Step Functions intrinsic functions. Intrinsic functions are only available in states that use the JSONPath query language.  

 Note: Built-in JSONata functions that require integer values as parameters will automatically round down any non-integer numbers provided.  

 $partition - JSONata equivalent of `States.ArrayPartition` intrinsic function to partition a large array.  

 The first parameter is the array to partition, the second parameter is an integer representing the chunk size. The return value will be a two-dimensional array. The interpreter chunks the input array into multiple arrays of the size specified by chunk size. The length of the last array chunk may be less than the length of the previous array chunks if the number of remaining items in the array is smaller than the chunk size.  

```
"Assign": {
  "arrayPartition": "{% $partition([1,2,3,4], $states.input.chunkSize) %}"
}

```
 

 $range - JSONata equivalent of `States.ArrayRange` intrinsic function to generate an array of values.  

 This function takes three arguments. The first argument is an integer representing the first element of the new array, the second argument is an integer representing the final element of the new array, and the third argument is the delta value integer for the elements in the new array. The return value is a newly-generated array of values ranging from the first argument of the function to the second argument of the function with elements in between adjusted by the delta. The delta value can be positive or negative which will increment or decrement each element from the last until the end value is reached or exceeded.  

```
"Assign": {
  "arrayRange": "{% $range(0, 10, 2) %}"
}

```
 

 $hash - JSONata equivalent of the `States.Hash` intrinsic function to calculate the hash value of a given input.  

 This function takes two arguments. The first argument is the source string to be hashed. The second argument is a string representing the hashing algorithm to for the hash calculation. The hashing algorithm must be one of the following values: `"MD5"`, `"SHA-1"`, `"SHA-256"`, `"SHA-384"`, `"SHA-512"`. The return value is a string of the calculated hash of the data.  

 This function was created because JSONata does not natively support the ability to calculate hashes.  

```
"Assign": {
  "myHash": "{% $hash($states.input.content, $hashAlgorithmName) %}"
}

```
 

 $random - JSONata equivalent of the `States.MathRandom` intrinsic function to return a random number n where `0 ≤ n < 1`.  

 The function takes an optional integer argument representing the seed value of the random function. If you use this function with the same seed value, it returns an identical number.  

 This overloaded function was created because the built-in JSONata function `$random` does not accept a seed value.  

```
"Assign": {
   "randNoSeed": "{% $random() %}",
   "randSeeded": "{% $random($states.input.seed) %}"
}

```
 

 $uuid - JSONata version of the `States.UUID` intrinsic function.  

 The function takes no arguments. This function return a v4 UUID.  

 This function was created because JSONata does not natively support the ability to generate UUIDs.  

```
"Assign": {
  "uniqueId": "{% $uuid() %}"
}

```
 

 $parse - JSONata function to deserialize JSON strings.  

 The function takes a stringified JSON as its only argument.  

 JSONata supports this functionality via `$eval`; however, `$eval` is not supported in Step Functions workflows.  

```
"Assign": {
  "deserializedPayload": "{% $parse($states.input.json_string) %}"
}

```
