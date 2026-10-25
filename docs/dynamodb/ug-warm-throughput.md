> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/warm-throughput.html
> Downloaded: 2026-10-24

# Understanding DynamoDB warm throughput

Warm throughput refers to the number of read and write operations your DynamoDB table can instantaneously support. These values are available by default for all tables and global secondary indexes (GSI) and represent how much they have scaled based on historical usage. If you are using on-demand mode, or if you update your provisioned throughput to these values, your application will be able to issue requests up to those values instantly.

DynamoDB will automatically adjust warm throughput values as your usage increases. You can also increase these values proactively when needed, which is especially useful for upcoming peak events like product launches or sales. For planned peak events, where request rates to your DynamoDB table might increase by 10x, 100x, or more, you can now assess whether the current warm throughput is sufficient to handle the expected traffic. If it’s not, you can increase the warm throughput value without changing your throughput settings or billing mode. This process is referred to as pre-warming a table, allowing you to set a baseline that your tables can instantly support. This ensures your applications can handle higher request rates from the moment they occur. After warm throughput is increased, the values can't be decreased.

You can increase the warm throughput value for read operations, write operations, or both. You can increase this value for new and existing single-Region tables, global tables, and GSIs. For global tables, this feature is available for version 2019.11.21 (Current), and the warm throughput settings you set will automatically apply to all replica tables in the global table. There is no limit to the number of DynamoDB tables you can pre-warm at any time. The time to complete pre-warming depends on the values you set and the size of the table or index. You can submit simultaneous pre-warm requests and these requests will not interfere with any table operations. You can pre-warm your table up to the table or index quota limit for your account in that Region. Use the Service Quotas console to check your current limits and increase them if needed. 

Warm throughput values are available by default for all tables and secondary indexes at no cost. However, if you proactively increase these default warm throughput values to pre-warm the tables, you will be charged for those requests. For more information, see Amazon DynamoDB pricing.

For more information about warm throughput, see the topics below:Topics
Check your DynamoDB table's current warm throughput
Increase your existing DynamoDB table's warm throughput
Create a new DynamoDB table with higher warm throughput
Understanding DynamoDB warm throughput in different scenarios
