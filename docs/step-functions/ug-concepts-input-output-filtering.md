> Source: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-input-output-filtering.html
> Downloaded: 2026-10-26

# Processing input and output in Step FunctionsManaging state with variables and JSONata

Step Functions recently added variables and JSONata to manage state and transform data.

Learn more in the blog post Simplifying developer experience with variables and JSONata in AWS Step Functions 

When a Step Functions execution receives JSON input, it passes that data to the first state in the workflow as input.

With JSONata, you can retrieve state input from `$states.input`. Your state machine executions also provide that initial input data in the Context object. You can retrieve the original state machine input at any point in your workflow from `$states.context.Execution.Input`.

 When states exit, their output is available to the very next state in your state machine. Your state inputs will pass through as state output by default, unless you modify the state output. For data that you might need in later steps, consider storing it in variables. For more info, see Passing data between states with variables. QueryLanguage recommendation

For new state machines, we recommend the JSONata query language. In state machines that do not specify a query language, the state machine defaults to JSONPath for backward compatibility. You must opt-in to use JSONata for your state machines or individual states.

Processing input and output with JSONata

With JSONata expressions, you can select and transform data. In the `Arguments` field, you can customize the data sent to the action. The result can be transformed into custom state output in the `Output` field. You can also store data in variables in the `Assign` field. For more info, see Transforming data with JSONata.

The following diagram shows how JSON information moves through a JSONata task state.  

Processing input and output with JSONPathManaging state and transforming data

Learn about Passing data between states with variables and Transforming data with JSONata.

For state machines that use JSONPath, the following fields control the flow of data from state to state: `InputPath`, `Parameters`, `ResultSelector`, `ResultPath`, and `OutputPath`. Each JSONPath field can manipulate JSON as it moves through each state in your workflow.

JSONPath fields can use paths to select portions of the JSON from the input or the result. A path is a string, beginning with `$`, that identifies nodes within JSON text. Step Functions paths use JsonPath syntax.

The following diagram shows how JSON information moves through a JSONPath task state. The `InputPath` selects the parts of the JSON input to pass to the task of the `Task` state (for example, an AWS Lambda function). You can adjust the data that is sent to your action in the `Parameters` field. Then, with `ResultSelector`, you can select portions of the action result to carry forward. `ResultPath` then selects the combination of state input and task results to pass to the output. `OutputPath` can filter the JSON output to further limit the information that's passed to the output.  Topics
Passing data between states with variables
Transforming data with JSONata in Step Functions
Accessing execution data from the Context object in Step Functions
Using JSONPath paths
Manipulate parameters in Step Functions workflows
Example: Manipulating state data with paths in Step Functions workflows
Specifying state output using ResultPath in Step Functions
Map state input and output fields in Step Functions
