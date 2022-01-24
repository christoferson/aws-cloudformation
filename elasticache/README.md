
## Basic

Launch Elasticache Redis Cluster inside a VPC with single shard

elasticache-redis-basic.yaml

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
