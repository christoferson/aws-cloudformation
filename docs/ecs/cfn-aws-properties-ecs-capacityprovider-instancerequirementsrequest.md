> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-instancerequirementsrequest.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider InstanceRequirementsRequest

The instance requirements for attribute-based instance type selection. Instead of specifying exact instance types, you define requirements such as vCPU count, memory size, network performance, and accelerator specifications. Amazon ECS automatically selects Amazon EC2 instance types that match these requirements, providing flexibility and helping to mitigate capacity constraints.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AcceleratorCount" : AcceleratorCountRequest,
  "AcceleratorManufacturers" : [ String, ... ],
  "AcceleratorNames" : [ String, ... ],
  "AcceleratorTotalMemoryMiB" : AcceleratorTotalMemoryMiBRequest,
  "AcceleratorTypes" : [ String, ... ],
  "AllowedInstanceTypes" : [ String, ... ],
  "BareMetal" : String,
  "BaselineEbsBandwidthMbps" : BaselineEbsBandwidthMbpsRequest,
  "BurstablePerformance" : String,
  "CpuManufacturers" : [ String, ... ],
  "ExcludedInstanceTypes" : [ String, ... ],
  "InstanceGenerations" : [ String, ... ],
  "LocalStorage" : String,
  "LocalStorageTypes" : [ String, ... ],
  "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice" : Integer,
  "MemoryGiBPerVCpu" : MemoryGiBPerVCpuRequest,
  "MemoryMiB" : MemoryMiBRequest,
  "NetworkBandwidthGbps" : NetworkBandwidthGbpsRequest,
  "NetworkInterfaceCount" : NetworkInterfaceCountRequest,
  "OnDemandMaxPricePercentageOverLowestPrice" : Integer,
  "RequireHibernateSupport" : Boolean,
  "SpotMaxPricePercentageOverLowestPrice" : Integer,
  "TotalLocalStorageGB" : TotalLocalStorageGBRequest,
  "VCpuCount" : VCpuCountRangeRequest
}

```

### YAML

```
  AcceleratorCount: 
    AcceleratorCountRequest
  AcceleratorManufacturers: 
    - String
  AcceleratorNames: 
    - String
  AcceleratorTotalMemoryMiB: 
    AcceleratorTotalMemoryMiBRequest
  AcceleratorTypes: 
    - String
  AllowedInstanceTypes: 
    - String
  BareMetal: String
  BaselineEbsBandwidthMbps: 
    BaselineEbsBandwidthMbpsRequest
  BurstablePerformance: String
  CpuManufacturers: 
    - String
  ExcludedInstanceTypes: 
    - String
  InstanceGenerations: 
    - String
  LocalStorage: String
  LocalStorageTypes: 
    - String
  MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Integer
  MemoryGiBPerVCpu: 
    MemoryGiBPerVCpuRequest
  MemoryMiB: 
    MemoryMiBRequest
  NetworkBandwidthGbps: 
    NetworkBandwidthGbpsRequest
  NetworkInterfaceCount: 
    NetworkInterfaceCountRequest
  OnDemandMaxPricePercentageOverLowestPrice: Integer
  RequireHibernateSupport: Boolean
  SpotMaxPricePercentageOverLowestPrice: Integer
  TotalLocalStorageGB: 
    TotalLocalStorageGBRequest
  VCpuCount: 
    VCpuCountRangeRequest

```

## Properties

**`AcceleratorCount`** 

The minimum and maximum number of accelerators for the instance types. This is used when you need instances with specific numbers of GPUs or other accelerators. 

Required: No

Type: AcceleratorCountRequest

Update requires: No interruption

**`AcceleratorManufacturers`** 

The accelerator manufacturers to include. You can specify `nvidia`, `amd`, `amazon-web-services`, or `xilinx` depending on your accelerator requirements. 

Required: No

Type: Array of String

Allowed values: `amazon-web-services | amd | habana | nvidia | xilinx`

Update requires: No interruption

**`AcceleratorNames`** 

The specific accelerator names to include. For example, you can specify `a100`, `v100`, `k80`, or other specific accelerator models. 

Required: No

Type: Array of String

Allowed values: `a10g | a100 | h100 | inferentia | k520 | k80 | m60 | radeon-pro-v520 | t4 | t4g | vu9p | v100 | l40s | l4 | gaudi-hl-205 | inferentia2 | trainium | trainium2 | u30`

Update requires: No interruption

**`AcceleratorTotalMemoryMiB`** 

The minimum and maximum total accelerator memory in mebibytes (MiB). This is important for GPU workloads that require specific amounts of video memory. 

Required: No

Type: AcceleratorTotalMemoryMiBRequest

Update requires: No interruption

**`AcceleratorTypes`** 

The accelerator types to include. You can specify `gpu` for graphics processing units, `fpga` for field programmable gate arrays, or `inference` for machine learning inference accelerators. 

Required: No

Type: Array of String

Allowed values: `gpu | fpga | inference`

Update requires: No interruption

**`AllowedInstanceTypes`** 

The instance types to include in the selection. When specified, Amazon ECS only considers these instance types, subject to the other requirements specified. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `30`

Update requires: No interruption

**`BareMetal`** 

Indicates whether to include bare metal instance types. Set to `included` to allow bare metal instances, `excluded` to exclude them, or `required` to use only bare metal instances. 

Required: No

Type: String

Allowed values: `included | required | excluded`

Update requires: No interruption

**`BaselineEbsBandwidthMbps`** 

The minimum and maximum baseline Amazon EBS bandwidth in megabits per second (Mbps). This is important for workloads with high storage I/O requirements. 

Required: No

Type: BaselineEbsBandwidthMbpsRequest

Update requires: No interruption

**`BurstablePerformance`** 

Indicates whether to include burstable performance instance types (T2, T3, T3a, T4g). Set to `included` to allow burstable instances, `excluded` to exclude them, or `required` to use only burstable instances. 

Required: No

Type: String

Allowed values: `included | required | excluded`

Update requires: No interruption

**`CpuManufacturers`** 

The CPU manufacturers to include or exclude. You can specify `intel`, `amd`, or `amazon-web-services` to control which CPU types are used for your workloads. 

Required: No

Type: Array of String

Allowed values: `intel | amd | amazon-web-services`

Update requires: No interruption

**`ExcludedInstanceTypes`** 

The instance types to exclude from selection. Use this to prevent Amazon ECS from selecting specific instance types that may not be suitable for your workloads. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `30`

Update requires: No interruption

**`InstanceGenerations`** 

The instance generations to include. You can specify `current` to use the latest generation instances, or `previous` to include previous generation instances for cost optimization. 

Required: No

Type: Array of String

Allowed values: `current | previous`

Update requires: No interruption

**`LocalStorage`** 

Indicates whether to include instance types with local storage. Set to `included` to allow local storage, `excluded` to exclude it, or `required` to use only instances with local storage. 

Required: No

Type: String

Allowed values: `included | required | excluded`

Update requires: No interruption

**`LocalStorageTypes`** 

The local storage types to include. You can specify `hdd` for hard disk drives, `ssd` for solid state drives, or both. 

Required: No

Type: Array of String

Allowed values: `hdd | ssd`

Update requires: No interruption

**`MaxSpotPriceAsPercentageOfOptimalOnDemandPrice`** 

The maximum price for Spot instances as a percentage of the optimal On-Demand price. This provides more precise cost control for Spot instance selection. 

Required: No

Type: Integer

Update requires: No interruption

**`MemoryGiBPerVCpu`** 

The minimum and maximum amount of memory per vCPU in gibibytes (GiB). This helps ensure that instance types have the appropriate memory-to-CPU ratio for your workloads. 

Required: No

Type: MemoryGiBPerVCpuRequest

Update requires: No interruption

**`MemoryMiB`** 

The minimum and maximum amount of memory in mebibytes (MiB) for the instance types. Amazon ECS selects instance types that have memory within this range. 

Required: Yes

Type: MemoryMiBRequest

Update requires: No interruption

**`NetworkBandwidthGbps`** 

The minimum and maximum network bandwidth in gigabits per second (Gbps). This is crucial for network-intensive workloads that require high throughput. 

Required: No

Type: NetworkBandwidthGbpsRequest

Update requires: No interruption

**`NetworkInterfaceCount`** 

The minimum and maximum number of network interfaces for the instance types. This is useful for workloads that require multiple network interfaces. 

Required: No

Type: NetworkInterfaceCountRequest

Update requires: No interruption

**`OnDemandMaxPricePercentageOverLowestPrice`** 

The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon ECS selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold. 

Required: No

Type: Integer

Update requires: No interruption

**`RequireHibernateSupport`** 

Indicates whether the instance types must support hibernation. When set to `true`, only instance types that support hibernation are selected. 

Required: No

Type: Boolean

Update requires: No interruption

**`SpotMaxPricePercentageOverLowestPrice`** 

The maximum price for Spot instances as a percentage over the lowest priced On-Demand instance. This helps control Spot instance costs while maintaining access to capacity. 

Required: No

Type: Integer

Update requires: No interruption

**`TotalLocalStorageGB`** 

The minimum and maximum total local storage in gigabytes (GB) for instance types with local storage. 

Required: No

Type: TotalLocalStorageGBRequest

Update requires: No interruption

**`VCpuCount`** 

The minimum and maximum number of vCPUs for the instance types. Amazon ECS selects instance types that have vCPU counts within this range. 

Required: Yes

Type: VCpuCountRangeRequest

Update requires: No interruption
