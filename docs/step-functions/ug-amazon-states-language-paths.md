> Source: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-paths.html
> Downloaded: 2026-10-26

# Using JSONPath pathsManaging state and transforming data

Learn about Passing data between states with variables and Transforming data with JSONata.

In the Amazon States Language, a path is a string beginning with `$` that you can use to identify components within JSON text. Paths follow JsonPath syntax, which is only available when the `QueryLanguage` is set to JSONPath. You can specify a path to access subsets of the input when specifying values for `InputPath`, `ResultPath`, and `OutputPath`.

You must use square bracket notation if your field name contains any character that is not included in the `member-name-shorthand` definition of the JsonPath ABNF rule. Therefore, to encode special characters, such as punctuation marks (excluding `_`), you must use square bracket notation. For example, `$.abc.['def ghi']`.  

## Reference Paths 

A reference path is a path whose syntax is limited in such a way that it can identify only a single node in a JSON structure:  
You can access object fields using only dot (`.`) and square bracket (`[ ]`) notation. 
Functions such as `length()` aren't supported. 
Lexical operators, which are non-symbolic, such as `subsetof` aren't supported. 
Filtering by regular expression or by referencing another value in the JSON structure is not supported. 
The operators `@`, `,`, `:`, and `?` are not supported 
 

For example, if state input data contains the following values: 

```
{
  "foo": 123,
  "bar": ["a", "b", "c"],
  "car": {
      "cdr": true
  }
}
```
 

The following reference paths would return the following. 

```
$.foo => 123
$.bar => ["a", "b", "c"]
$.car.cdr => true

```
 

Certain states use paths and reference paths to control the flow of a state machine or configure a state's settings or options. For more information, see Modeling workflow input and output path processing with data flow simulator and Using JSONPath effectively in AWS Step Functions. 

### Flattening an array of arrays 

If the Parallel workflow state or Map workflow state state in your state machines return an array of arrays, you can transform them into a flat array with the ResultSelector field. You can include this field inside the Parallel or Map state definition to manipulate the result of these states. 

To flatten arrays, use the syntax: `[*]` in the `ResultSelector` field as shown in the following example. 

```
"ResultSelector": {
    "flattenArray.$": "$[*][*]"
  }
```
 

For examples that show how to flatten an array, see Step 3 in the following tutorials:  
Processing batch data with a Lambda function in Step Functions 
Processing individual items with a Lambda function in Step Functions
