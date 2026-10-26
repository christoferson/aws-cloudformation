
## Step Functions - JSONata and variables

[step-functions-jsonata-order-pricing.yaml](step-functions-jsonata-order-pricing.yaml)

### The problem with JSONPath

Classic ASL moves data with **five path fields** per state (`InputPath`, `Parameters`, `ResultSelector`, `ResultPath`, `OutputPath`), a `.$` suffix on every dynamic key, and a few intrinsic functions (`States.Format`, `States.ArrayLength`, ...).
- **No real expressions:** you can't add, sum or filter. Even "price × quantity" needed a Lambda function.
- **Data must be carried along:** anything a later state needs must be threaded through every state's output in between (`ResultPath: $.something`).

### What changed (November 2024)

| | JSONPath (default) | **JSONata** (`QueryLanguage: JSONata`) |
|---|---|---|
| Expressions | Paths (`$.order.total`) + intrinsic functions | `"{% ... %}"`: arithmetic, `$sum`, `$map`, filters `items[qty>1]`, conditionals `a ? b : c`, string and date functions |
| State input → API | `InputPath` + `Parameters` (`"key.$": "$.x"`) | **`Arguments`** (`"key": "{% $states.input.x %}"`) |
| API result → output | `ResultSelector` + `ResultPath` + `OutputPath` | **`Output`** (`"{% $states.result... %}"`) |
| Choice | `Variable` + `NumericGreaterThan`, `StringEquals`, ... | **`Condition`**: `"{% $subtotal >= 100 %}"` |
| Map items | `ItemsPath` | **`Items`** |
| Dynamic numbers | `TimeoutSecondsPath`, `SecondsPath`, ... | Plain field: `"TimeoutSeconds": "{% $timeout %}"` |
| Errors | — | `States.QueryEvaluationError` (catchable / retryable) |

**Variables** (`Assign`) work with **both** query languages. You store a value once, and any later state reads it as `$name`:

```yaml
StoreOrder:
  Type: Pass
  Assign:
    orderId: "{% $uuid() %}"            # available as $orderId from the NEXT state on
    customerId: "{% $states.input.customerId %}"
```

`$states` is the one reserved variable:

| Field | Contents |
|---|---|
| `input` | The state input |
| `result` | The task, Map or Parallel result |
| `errorOutput` | The error output, inside `Catch` only |
| `context` | The Context object (execution, task token, ...) |

Offline docs: [../../docs/step-functions/README.md](../../docs/step-functions/README.md)

----------------------------------------------------------------------------------

## The workflow (no Lambda)

```
 input { customerId, couponCode?, items: [{productId, quantity}] }
   │
 StoreOrder      Pass    Assign $orderId=$uuid(), $customerId, $couponCode, $orderedAt=$now()
   │                     Output = items only
 PriceItems      Map     per item: dynamodb:getItem -> {name, unitPrice, lineTotal}
   │                       unknown product -> $error(...) ──Catch──► RejectOrder
   │                     Assign $lines = results, $subtotal = $round($sum(results.lineTotal), 2)
 ChooseDiscount  Choice  Condition $couponCode = 'SAVE10'  -> 10%
   │                     Condition $subtotal >= 100        -> 5%       (Assign in the rule)
   │                     Default -> NoDiscount (0)
 SaveOrder       Task    dynamodb:putItem; JSONata builds the typed item (List of Maps from $lines)
                         Output = response built from variables
```

What each feature replaces:

| In the template | Without JSONata / variables |
|---|---|
| `$round($number(Item.price.N) * quantity, 2)` in `Output` | A Lambda function to calculate prices |
| `$sum($states.result.lineTotal)` | A Lambda function, or `ResultSelector` gymnastics |
| `$orderId`, `$customerId`, `$subtotal` read in `SaveOrder` | `ResultPath` into the payload in every state in between |
| `Condition: "{% $couponCode = 'SAVE10' %}"` | `Variable` + `StringEquals`, plus a separate path for each comparison |
| `$map($lines, function($line){ {'M': {...}} })` | Building a DynamoDB list in code |
| `$exists(Item) ? {...} : $error(...)` | A Lambda function to validate the product, or a Choice state per check |

Built-in JSONata 2.0.6 functions are available, except `$eval` (use `$parse`). Step Functions adds `$partition`, `$range`, `$hash`, `$random`, `$uuid` and `$parse`.

### Rules that trip people up

- **Delimiters:** a JSONata string must **start with `{%` and end with `%}`**, with no spaces outside them, or validation fails.
- **Assign vs Output:** both are evaluated **from the same state input and result, at the same time**. A variable assigned in a state is visible **from the next state on**, and `Output` can't use a variable assigned in the same state. Recompute the value instead, as `SaveOrder` does with the total.
- **Scope:** Map iterations and Parallel branches have **their own scope**. They can read outer variables but can't assign them, and the same name can't be assigned in both scopes. Return data with `Output`, as `PriceItems` does. A `Catch` `Assign` writes to the outer scope. Distributed Map can't read outer variables.
- **Undefined is an error:** `$states.input.missing` fails with `States.QueryEvaluationError`. Guard with `$exists(...)`, as `StoreOrder` does for the coupon.
- **Limits:** a variable can be up to 256 KiB, and all variables in an execution up to 10 MiB. A JSONata expression has 1 second to evaluate.
- **Mixing languages:** `QueryLanguage` can also be set **per state**, so a JSONPath state machine can be migrated one state at a time. Path fields (`Parameters`, `ResultPath`, ...) are invalid in JSONata states, and `Arguments` / `Output` are invalid in JSONPath states.

### Exam note

JSONPath (`InputPath` → `Parameters` → `ResultSelector` → `ResultPath` → `OutputPath`) still appears in exam questions and most existing workflows, so know both. For new workflows, AWS recommends choosing JSONata in the console. [../../lambda/lambda-durable-functions/stepfunctions-order-approval.yaml](../../lambda/lambda-durable-functions/stepfunctions-order-approval.yaml) is a JSONPath example to compare against.

----------------------------------------------------------------------------------

## Deploy and try it

```bash
aws cloudformation create-stack --stack-name myapp-dev-jsonata \
  --template-body file://step-functions-jsonata-order-pricing.yaml --capabilities CAPABILITY_IAM

# Seed the catalog (prices live here, not in the order)
aws dynamodb batch-write-item --request-items '{
  "myapp-dev-jsonata-products": [
    {"PutRequest": {"Item": {"productId": {"S": "p-1"}, "name": {"S": "Keyboard"}, "price": {"N": "49.90"}}}},
    {"PutRequest": {"Item": {"productId": {"S": "p-2"}, "name": {"S": "Mouse"},    "price": {"N": "19.95"}}}},
    {"PutRequest": {"Item": {"productId": {"S": "p-3"}, "name": {"S": "Monitor"},  "price": {"N": "189.00"}}}}
  ]}'

SM=$(aws cloudformation describe-stacks --stack-name myapp-dev-jsonata \
  --query "Stacks[0].Outputs[?OutputKey=='OrderPricingStateMachineArn'].OutputValue" --output text)

run() { ARN=$(aws stepfunctions start-execution --state-machine-arn $SM --input "$1" --query executionArn --output text)
        sleep 3; aws stepfunctions describe-execution --execution-arn $ARN --query output --output text; }

run '{"customerId":"c-1","items":[{"productId":"p-1","quantity":1},{"productId":"p-2","quantity":2}]}'   # 89.80, no discount
run '{"customerId":"c-1","couponCode":"SAVE10","items":[{"productId":"p-1","quantity":1}]}'          # 10%
run '{"customerId":"c-1","items":[{"productId":"p-3","quantity":1}]}'                                # >= 100 -> 5%
run '{"customerId":"c-1","items":[{"productId":"nope","quantity":1}]}'                                # REJECTED
```

Test a single state without running the whole workflow:

```bash
aws stepfunctions test-state --role-arn <state machine role arn> \
  --definition '{"QueryLanguage":"JSONata","Type":"Pass","Output":"{% $round($sum($states.input.items.(price*qty)), 2) %}","End":true}' \
  --input '{"items":[{"price":4.99,"qty":3},{"price":12.5,"qty":2}]}'
```

The console's **Workflow Studio** and the **TestState API** are the quickest way to experiment with expressions.

## Docs

- [../../docs/step-functions/ug-transforming-data.md](../../docs/step-functions/ug-transforming-data.md) (JSONata: syntax, `$states`, Arguments / Output, Choice Condition, errors, functions)
- [../../docs/step-functions/ug-workflow-variables.md](../../docs/step-functions/ug-workflow-variables.md) (Assign, scope, evaluation order, limits, JSONPath variables)
- [../../docs/step-functions/ug-concepts-input-output-filtering.md](../../docs/step-functions/ug-concepts-input-output-filtering.md)
- [../../docs/step-functions/ug-amazon-states-language-paths.md](../../docs/step-functions/ug-amazon-states-language-paths.md) (JSONPath, for comparison)
