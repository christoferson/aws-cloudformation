## Glue Cloudformation

### Glue - Source S3 - XML

xxx

[glue-s3-xml](glue-s3-xml.yaml)


### Glue - Job - Source S3 (XML) to Destination S3 (JSON)

Provision a Glue Job that reads XML files from source bucket and writes output as json to destination bucket

##### Role

- Need permission to access script
- Need permission to access source bucket
- Need permission to access destination bucket
- Need permission to push metric to cloudwatch
- Need permission to put log to cloudwatch

##### Source XML | [link](glue-s3-job-xml/cd_catalog.xml)

```(xml)
<CATALOG>
  <CD>
    <TITLE>Empire Burlesque</TITLE>
    <ARTIST>Bob Dylan</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>Columbia</COMPANY>
    <PRICE>10.90</PRICE>
    <YEAR>1985</YEAR>
  </CD>
</CATALOG>
```

[glue-s3-job-xml](glue-s3-job-xml.yaml)


### Links


https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html

https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html

https://docs.aws.amazon.com/ja_jp/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame-reader.html

https://docs.aws.amazon.com/ja_jp/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame-writer.html#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-writer-from_options

https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format.html

/aws-glue/jobs/error

### Classes

##### GlueContext | [link](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-glue-context.html)

Wraps the Apache Spark SparkContext object, and thereby provides mechanisms for interacting with the Apache Spark platform.


