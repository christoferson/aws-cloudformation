## ElastiCache


## Redis

### Redis - Cluster mode - Enabled

- Cluster mode enables replication across multiple shards for enhanced scalability and availability.
- Enabling cluster mode supports partitioning your data across up to 500 node groups and improves performance of Redis clusters. Some commands are unavailable in this mode.

### Redis - Cluster mode - Disabled

- The Redis cluster will have a single shard (node group) with one primary node and up to 5 read replica. 
- If you choose cluster mode disabled you cannot change the number of shards. The configuration supports all Redis commands and functionality but limits maximum cache size and performance

### Redis - Auth

TransitEncryptionEnabled Redis AUTH Disabled
For HIPAA compliance, you must specify TransitEncryptionEnabled as true, an AuthToken, and a CacheSubnetGroup.

### Redis - Basic (cluster mode disabled) 

Launch Elasticache Redis Cluster inside a VPC with single shard with 2 Nodes.

[elasticache-redis-basic](elasticache-redis-basic.yaml)

### Install Redis Client in EC2

```
sudo yum install gcc
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make distclean      # ubuntu systems only
make
src/redis-cli -c -h mycachecluster.eaogs8.0001.usw2.cache.amazonaws.com -p 6379
```

https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/nodes-connecting.html

## Memcached

Versions - https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/supported-engine-versions-mc.html
Encryption in Transit can only be enabled during creation.

## MemcacheD - Basic

Launch Elasticache MemCacheD Cluster inside a VPC

[elasticache-memcached-basic](elasticache-memcached-basic.yaml)


## Errors - Memcached
- engine-log log delivery is not supported for the memcached engine
- Scaling is not supported for engine memcached

## Errors - Redis
Invalid AuthToken provided.

## Links
https://aws.amazon.com/about-aws/whats-new/2022/05/amazon-elasticache-memcached-supports-encryption-data-transit/?nc1=h_ls

##TODO

User Group
Redis Cluster Enabled
Event