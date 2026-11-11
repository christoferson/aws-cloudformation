<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/prereq-runtime-monitoring-cpu-os-kernel-support.html -->
<!-- Downloaded: 2026-10-28 -->

# Supported CPU architectures, operating systems, and kernel versions

This section consolidates the CPU architectures, OS distributions, and kernel versions that have been verified to support the GuardDuty security agent. Unless a resource type is called out separately, these requirements apply to Runtime Monitoring for Amazon EC2 instances, AWS Fargate (Amazon ECS only), and Amazon EKS clusters.

Kernel support includes `eBPF`, `Tracepoints`, and `Kprobe`. For CPU architectures, Runtime Monitoring supports AMD64 (`x64`) and ARM64 (Graviton2 and above)[1](#cok-graviton-2-support).

The following table shows the OS distributions and kernel versions that have been verified to support the GuardDuty security agent.

|  OS distribution[2](#cok-os-support) |  Kernel version[3](#cok-kernel-version-required-flag) |
|---|---|
|  Amazon Linux 2 |

5.4[4](#cok-kernel-5-10), 5.10[4](#cok-kernel-5-10), 5.15 |
|  Amazon Linux 2023 |

5.4[4](#cok-kernel-5-10), 5.10[4](#cok-kernel-5-10), 5.15, 6.1, 6.5, 6.8, 6.12 |
|  Ubuntu 20.04, 22.04, 24.04, 26.04 |

5.4[4](#cok-kernel-5-10), 5.10[4](#cok-kernel-5-10), 5.15, 6.1, 6.5, 6.8, 6.13, 6.14, 6.15, 6.16, 6.17, 6.18, 7.0 |
|  Debian 11, 12, 13 |

5.4[4](#cok-kernel-5-10), 5.10[4](#cok-kernel-5-10), 5.15, 6.1, 6.5, 6.8, 6.12 |
|  RedHat 9.4, 10.2 |

5.14, 6.12 |
|  Fedora 34, 40, 41, 43, 44 |

5.11, 5.17, 6.8, 6.12, 7.1 |
|  CentOS Stream 9, 10 |

5.14, 6.12 |
|  Oracle Linux 8.9, 9.3 |

5.15 |
|  Rocky Linux 9.5, 10.1 |

5.14, 6.12 |
|  Alma Linux 9, 10 |

5.14, 6.12 |
|  SUSE Linux Enterprise Server 16 |

6.12 |
|  Bottlerocket |

5.4[4](#cok-kernel-5-10), 5.10[4](#cok-kernel-5-10), 5.15, 6.1, 6.18 |

1.

Runtime Monitoring doesn't support the first generation Graviton instance such as A1 instance types.
2.

Support for various operating systems - GuardDuty has verified Runtime Monitoring support for the operating distribution listed in the preceding table. While the GuardDuty security agent may run on operating systems not listed in the preceding table, the GuardDuty team cannot guarantee the expected security value.
3.

For any kernel version, you must set the `CONFIG_DEBUG_INFO_BTF` flag to `y` (meaning *true*). This is required so that the GuardDuty security agent can run as expected.

For AWS Fargate (Amazon ECS only), this kernel option is managed by Fargate and requires no action from you.
4.

For kernel versions 5.10 and earlier, the GuardDuty security agent uses locked memory in RAM (`RLIMIT_MEMLOCK`) to function as expected. If your system's `RLIMIT_MEMLOCK` value is set too low, GuardDuty recommends setting both hard and soft limits to at least 32 MB. For information about verifying and modifying the default `RLIMIT_MEMLOCK` value on Amazon EC2 instances, see [Viewing and updating RLIMIT_MEMLOCK values](https://docs.aws.amazon.com/guardduty/latest/ug/prereq-runtime-monitoring-ec2-support.html#runtime-monitoring-ec2-modify-rlimit-memlock).
