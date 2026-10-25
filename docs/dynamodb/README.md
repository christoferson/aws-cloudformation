
## Amazon DynamoDB - Local Documentation Snapshot

Offline copies of the AWS docs used to build [dynamodb/dynamodb-on-demand](../../dynamodb/dynamodb-on-demand/), converted from HTML to Markdown.
Downloaded 2026-10-24. Each file starts with its source URL. Check the live page if something looks off.

### What's new

| File | Topic |
|---|---|
| [whatsnew-2024-11-dynamodb-price-reduction.md](whatsnew-2024-11-dynamodb-price-reduction.md) | On-demand throughput −50%, global table replicated writes −67% (on-demand) / −33% (provisioned), from 2024-11-01 |
| [ug-DocumentHistory.md](ug-DocumentHistory.md) | DynamoDB Developer Guide document history |

### Developer Guide — Capacity and cost

| File | Topic |
|---|---|
| [ug-on-demand-capacity-mode.md](ug-on-demand-capacity-mode.md) | On-demand mode |
| [ug-on-demand-capacity-mode-max-throughput.md](ug-on-demand-capacity-mode-max-throughput.md) | Maximum throughput for on-demand tables (cost guard, throttling, metrics) |
| [ug-provisioned-capacity-mode.md](ug-provisioned-capacity-mode.md) | Provisioned mode |
| [ug-bp-switching-capacity-modes.md](ug-bp-switching-capacity-modes.md) | Switching capacity modes |
| [ug-CostOptimization_TableCapacityMode.md](ug-CostOptimization_TableCapacityMode.md) | Which mode costs less (35% utilization rule, reserved capacity) |
| [ug-CostOptimization_TableClass.md](ug-CostOptimization_TableClass.md) | Standard vs Standard-IA (~60% lower storage) |
| [ug-warm-throughput.md](ug-warm-throughput.md) | Warm throughput |
| [ug-check-warm-throughput.md](ug-check-warm-throughput.md) | Check warm throughput |
| [ug-create-table-warm-throughput.md](ug-create-table-warm-throughput.md) | Create a table with higher warm throughput |
| [ug-warm-throughput-scenarios.md](ug-warm-throughput-scenarios.md) | Scenarios (new table starts at 12,000 RRU / 4,000 WRU) |

### Developer Guide — Global tables

| File | Topic |
|---|---|
| [ug-GlobalTables.md](ug-GlobalTables.md) | Overview |
| [ug-globaltables-CoreConcepts.md](ug-globaltables-CoreConcepts.md) | Core concepts: TTL, streams, transactions, throughput per mode |
| [ug-globaltables-SameAccount.md](ug-globaltables-SameAccount.md) | Same-account global tables |
| [ug-V2globaltables_HowItWorks.md](ug-V2globaltables_HowItWorks.md) | Consistency modes MREC vs MRSC, MRSC Regions, witness, limitations |
| [ug-global-tables-billing.md](ug-global-tables-billing.md) | rWRU / rWCU billing, witness costs, no replication transfer fee |
| [ug-V2globaltables_versions.md](ug-V2globaltables_versions.md) | Version 2019.11.21 vs 2017.11.29 (legacy) |
| [ug-globaltables-bestpractices.md](ug-globaltables-bestpractices.md) | Best practices |

### Developer Guide — Protection and access

| File | Topic |
|---|---|
| [ug-Point-in-time-recovery.md](ug-Point-in-time-recovery.md) | Point-in-time recovery |
| [ug-PointInTimeRecovery_Howitworks.md](ug-PointInTimeRecovery_Howitworks.md) | Enable PITR, recovery period (1-35 days, same price) |
| [ug-access-control-resource-based.md](ug-access-control-resource-based.md) | Resource-based policies (20 KB, cross-account, Block Public Access) |

### CloudFormation Template Reference

| File | Type |
|---|---|
| [cfn-aws-resource-dynamodb-table.md](cfn-aws-resource-dynamodb-table.md) | `AWS::DynamoDB::Table` |
| [cfn-aws-resource-dynamodb-globaltable.md](cfn-aws-resource-dynamodb-globaltable.md) | `AWS::DynamoDB::GlobalTable` (`MultiRegionConsistency`, `GlobalTableWitnesses`, `TableType`, ...) |

All property types of both resources are saved too, as `cfn-aws-properties-dynamodb-table-*.md` and `cfn-aws-properties-dynamodb-globaltable-*.md`. The key ones are `ondemandthroughput`, `warmthroughput`, `resourcepolicy`, `pointintimerecoveryspecification`, `replicaspecification`, `globaltablewitness`, `writeondemandthroughputsettings` and `readondemandthroughputsettings`.
