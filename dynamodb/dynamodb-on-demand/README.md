
## DynamoDB on-demand and global tables (after the November 2024 price cut)

### What changed

On 2024-11-01 DynamoDB cut two prices ([announcement](../../docs/dynamodb/whatsnew-2024-11-dynamodb-price-reduction.md)):

| | Before | Now |
|---|---|---|
| **On-demand** read / write requests | — | **−50%** |
| **Global tables** replicated writes | Priced above normal writes | **Same price as single-Region writes**: −67% on on-demand, −33% on provisioned |

AWS: on-demand is now *"the default and recommended mode for most DynamoDB workloads"*. The capacity mode guide adds that on-demand is cheaper when average provisioned utilization is **below 35%**, and often above that too when traffic has quiet periods and peaks.

All the older templates in [../](../README.md) use **provisioned** capacity (`ProvisionedThroughput` 5/5 and similar). The templates here are the on-demand versions, following the repo conventions (`Application` / `Environment`, full-word names, `Name` tags).

| Template | Scenario | Shows |
|---|---|---|
| [dynamodb-on-demand-table.yaml](dynamodb-on-demand-table.yaml) | Orders table | On-demand, **maximum throughput** cost guard on the table and GSI, deletion protection, PITR recovery period, **resource-based policy** for cross-account read |
| [dynamodb-on-demand-warm-throughput.yaml](dynamodb-on-demand-warm-throughput.yaml) | Ticket sale / launch day | **Warm throughput**: pre-warm the table and GSI for an instant peak |
| [dynamodb-global-table-mrec.yaml](dynamodb-global-table-mrec.yaml) | Active-active profiles in 3 Regions | Global table, **eventual consistency** (MREC), on-demand, per-replica settings |
| [dynamodb-global-table-mrsc.yaml](dynamodb-global-table-mrsc.yaml) | Balances that must never be stale | Global table, **strong consistency** (MRSC), 2 replicas + **witness**, RPO 0 |

Provisioned capacity is still shown by [../dynamodb-autoscale.yaml](../dynamodb-autoscale.yaml).

Offline docs: [../../docs/dynamodb/README.md](../../docs/dynamodb/README.md)

----------------------------------------------------------------------------------

## On-demand vs provisioned

| Choose | When |
|---|---|
| **On-demand** (`PAY_PER_REQUEST`) | Traffic changes over time, spikes, batch jobs, drops to zero or below 30% of peak, new apps with unknown load, or average provisioned utilization < 35%. No capacity planning and no auto scaling. A table instantly absorbs up to 2× its previous peak |
| **Provisioned** | Steady, predictable traffic you can provision close to actual use, especially with **reserved capacity** (not available for rWCU or Standard-IA). Mode can be switched: provisioned → on-demand up to 4 times per 24 hours, and on-demand → provisioned at any time |

### Cost guard: maximum throughput

On-demand has no capacity ceiling, so a bug or a runaway job can drive cost up. `OnDemandThroughput` (table) or `WriteOnDemandThroughputSettings` / `ReadOnDemandThroughputSettings` (global table) cap requests per second:
- **Effect:** requests above the cap are throttled with `ThrottlingException`. The cap is best effort, so burst capacity can briefly exceed it.
- **GSIs:** each GSI has its own cap.
- **Global tables:** all replicas share the same **write** cap. The read cap is set per replica.
- **Monitoring:** watch the CloudWatch metrics `OnDemandMaxReadRequestUnits` / `OnDemandMaxWriteRequestUnits` and throttling.

### Warm throughput

A **new** on-demand table can instantly serve **12,000 reads and 4,000 writes per second**, and grows from there with use. For a launch where traffic jumps 10× to 100× at once, set `WarmThroughput` to the expected peak **beforehand**:
- **Not a limit:** it isn't a cap or reserved capacity, and you still pay per request. Raising it is charged.
- **Defaults:** the template's default values match the new-table defaults, so they cost nothing.
- **One-way:** once increased, warm throughput can't be decreased.
- **Check it:** `aws dynamodb describe-table --table-name <t> --query "Table.WarmThroughput"`.

## Global tables: MREC vs MRSC

| | **MREC** (`EVENTUAL`, default) | **MRSC** (`STRONG`) |
|---|---|---|
| Writes | Local and fast, replicated asynchronously (usually seconds) | Synchronously stored in at least one other Region before success, so writes are slower |
| Strongly consistent read | Latest write **made in this Region** | Latest write **from any Region** |
| Conflicts | Last writer wins, per item | `ReplicatedWriteConflictException`, retry |
| RPO | Replication delay (seconds) | **0** |
| Regions | Any, any number of replicas. Add or remove one per update | **Exactly 3**: 3 replicas or 2 + **witness**, from 15 MRSC Regions. Can't add replicas later |
| Not supported | — | TTL, LSIs, transactions |
| Streams | Required (replication uses them) | Optional |
| Mode change | Can't change after creation | Can't change after creation |

**Billing for both:**
- **Replicated writes:** one write unit per replica Region, at the same price as a normal write (since November 2024). A 1 KB write to a 3-Region table = 3 rWRUs (one per replica Region), each priced like a WRU.
- **No transfer fee:** DynamoDB doesn't charge cross-Region data transfer for replication.
- **Witness:** an MRSC witness has no rWRU, storage or replication transfer charges.
- **GSI updates:** billed as normal writes in each Region.

### Global table rules in CloudFormation

- **Stack Region:** `Replicas` must include the stack Region.
- **Removing a replica deletes its data**, unless you disassociate it (MREC only) with `TableType: Regional`. Disassociation keeps the replica as a standalone table.
- **Per-replica settings:** PITR, deletion protection, the read cap, table class, Contributor Insights and the resource policy are set per replica.
- **Shared settings:** the write cap, TTL, streams, SSE and warm throughput apply to all replicas.

----------------------------------------------------------------------------------

## Deploy

```bash
ACCT=$(aws sts get-caller-identity --query Account --output text)

aws cloudformation create-stack --stack-name myapp-dev-orders \
  --template-body file://dynamodb-on-demand-table.yaml \
  --parameters ParameterKey=ReportingAccountId,ParameterValue=$ACCT

aws cloudformation create-stack --stack-name myapp-dev-tickets \
  --template-body file://dynamodb-on-demand-warm-throughput.yaml \
  --parameters ParameterKey=TableWarmWriteUnitsPerSecond,ParameterValue=4000

# Global tables: deploy in the "home" Region; replicas are created by the stack
aws cloudformation create-stack --region us-east-1 --stack-name myapp-dev-profiles \
  --template-body file://dynamodb-global-table-mrec.yaml \
  --parameters ParameterKey=SecondRegion,ParameterValue=eu-west-1 ParameterKey=ThirdRegion,ParameterValue=ap-northeast-1

aws cloudformation create-stack --region us-east-1 --stack-name myapp-dev-balances \
  --template-body file://dynamodb-global-table-mrsc.yaml \
  --parameters ParameterKey=SecondRegion,ParameterValue=us-east-2 ParameterKey=WitnessRegion,ParameterValue=us-west-2
```

Try MRSC: write in one Region, then read with strong consistency in the other:

```bash
aws dynamodb put-item --region us-east-1 --table-name myapp-dev-balances --item '{"accountId":{"S":"a-1"},"balance":{"N":"100"}}'
aws dynamodb get-item --region us-east-2 --table-name myapp-dev-balances --key '{"accountId":{"S":"a-1"}}' --consistent-read
```

## Docs

- [../../docs/dynamodb/whatsnew-2024-11-dynamodb-price-reduction.md](../../docs/dynamodb/whatsnew-2024-11-dynamodb-price-reduction.md)
- [../../docs/dynamodb/ug-CostOptimization_TableCapacityMode.md](../../docs/dynamodb/ug-CostOptimization_TableCapacityMode.md) (on-demand vs provisioned, 35% rule)
- [../../docs/dynamodb/ug-on-demand-capacity-mode-max-throughput.md](../../docs/dynamodb/ug-on-demand-capacity-mode-max-throughput.md)
- [../../docs/dynamodb/ug-warm-throughput.md](../../docs/dynamodb/ug-warm-throughput.md)
- [../../docs/dynamodb/ug-V2globaltables_HowItWorks.md](../../docs/dynamodb/ug-V2globaltables_HowItWorks.md) (MREC vs MRSC)
- [../../docs/dynamodb/ug-global-tables-billing.md](../../docs/dynamodb/ug-global-tables-billing.md)
- [../../docs/dynamodb/cfn-aws-resource-dynamodb-globaltable.md](../../docs/dynamodb/cfn-aws-resource-dynamodb-globaltable.md)
