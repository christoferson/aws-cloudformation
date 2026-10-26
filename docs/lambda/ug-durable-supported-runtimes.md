> Source: https://docs.aws.amazon.com/lambda/latest/dg/durable-supported-runtimes.html
> Downloaded: 2026-10-25

# Supported runtimes for durable functions

Durable functions are available for selected managed runtimes and OCI container images for additional runtime version flexibility. You can create durable functions for Node.js, Python, Java, and C# (.NET) using managed runtimes directly in the console or programmatically through infrastructure-as-code. 

## Lambda managed runtimes 

The following managed runtimes support durable functions when you create functions in the Lambda console or using the AWS CLI with the `--durable-config '{"ExecutionTimeout": 3600, "RetentionPeriodInDays": 7}'` parameter. For complete information about Lambda runtimes, see Lambda runtimes.  
|  Language |  Runtime |    
|  Node.js |  nodejs22.x |   
|  Node.js |  nodejs24.x |   
|  Python |  python3.13 |   
|  Python |  python3.14 |   
|  Java |  java17 |   
|  Java |  java21 |   
|  Java |  java25 |   
|  C# (.NET) |  dotnet8 |   
|  C# (.NET) |  dotnet10 |    Note

Lambda Node.js and Python runtimes include the durable execution SDK for testing and development. However, we recommend including the SDK in your deployment package for production. This ensures version consistency and avoids potential runtime updates that might affect your function behavior. Because Java and C# (.NET) are compiled languages, Lambda Java and .NET runtimes do not include the durable execution SDK, so it must be included in your deployment package. 

### Node.js 

Install the SDK in your Node.js project: 

```

npm install @aws/durable-execution-sdk-js
      
```
 

The SDK supports JavaScript and TypeScript. For TypeScript projects, the SDK includes type definitions. 

### Python 

Install the SDK in your Python project: 

```

pip install aws-durable-execution-sdk-python
      
```
 

The Python SDK uses synchronous methods and doesn't require `async/await`. 

### Java 

Add a dependency to `pom.xml`: 

```

<dependency>
    <groupId>software.amazon.lambda.durable</groupId>
    <artifactId>aws-durable-execution-sdk-java</artifactId>
    <version>VERSION</version>
</dependency>
      
```
 

Install the SDK in your Java project: 

```

mvn install
      
```
 

The Java SDK provides both synchronous and asynchronous versions of each method. 

### C# (.NET) 

Add the SDK to your .NET project: 

```

dotnet add package Amazon.Lambda.DurableExecution
      
```
 

The .NET SDK exposes durable operations through `IDurableContext`. Your handler receives the durable execution service envelope and delegates to `DurableFunction.WrapAsync`. Every operation body takes a `CancellationToken`. 

## Container images 

You can use durable functions with container images to support additional runtime versions or custom runtime configurations. Container images let you use runtime versions not available as managed runtimes or customize your runtime environment. 

To create a durable function using a container image:  
Create a Dockerfile based on an Lambda base image
Install the durable execution SDK in your container
Build and push the container image to Amazon Elastic Container Registry
Create the Lambda function from the container image with durable execution enabled
 

### Container example 

Create a Dockerfile:  

**Python** 

Create a Dockerfile for Python 3.11: 

```

FROM public.ecr.aws/lambda/python:3.11

# Copy requirements file
COPY requirements.txt ${LAMBDA_TASK_ROOT}/

# Install dependencies including durable SDK
RUN pip install -r requirements.txt

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}/

# Set the handler
CMD [ "lambda_function.handler" ]
              
```
 

Create a `requirements.txt` file: 

```

aws-durable-execution-sdk-python
              
```
  

**Java** 

Create a Dockerfile for Java 25: 

```

FROM --platform=linux/amd64 public.ecr.aws/lambda/java:25

# Install Maven
RUN dnf install -y maven

WORKDIR /var/task

# Copy Maven configuration and source code
COPY pom.xml .
COPY src ./src

# Build
RUN mvn clean package -DskipTests

# Move JAR to lib directory
RUN mv target/*.jar lib/

# Set the handler
CMD ["src.path.to.lambdaFunction::handler"]
              
```
   

Build and push the image: 

```

# Build the image
docker build -t my-durable-function .

# Tag for ECR
docker tag my-durable-function:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-durable-function:latest

# Push to ECR
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-durable-function:latest
      
```
 

Create the function with durable execution enabled: 

```

aws lambda create-function \
  --function-name myDurableFunction \
  --package-type Image \
  --code ImageUri=123456789012.dkr.ecr.us-east-1.amazonaws.com/my-durable-function:latest \
  --role arn:aws:iam::123456789012:role/lambda-execution-role \
  --durable-config '{"ExecutionTimeout": 3600, "RetentionPeriodInDays": 7}'
      
```
 

For more information about using container images with Lambda, see Creating Lambda container images in the Lambda Developer Guide. 

## Runtime considerations 

SDK version management: To maintain full control over your dependencies and to avoid possible version misalignment issues, we recommend you add all of your function's dependencies to your deployment package, even if versions of them are included in the Lambda runtime by default. This includes the durable execution SDK. Lock the durable execution SDK to a major version in your dependency file. A new major version can introduce changes that may result in failures of in-flight executions. Use numbered versions or aliases for production durable functions rather than `$LATEST` to ensure SDK version changes do not affect in-flight executions. 

Runtime updates: AWS updates managed runtimes to include security patches and bug fixes. These updates might include new SDK versions. To avoid unexpected behavior, include the SDK in your deployment package and test thoroughly before deploying to production. 

Container image size: Container images have a maximum uncompressed size of 10 GB. The durable execution SDK adds minimal size to your image. Optimize your container by using multi-stage builds and removing unnecessary dependencies. 

Cold start performance: Container images might have longer cold start times than managed runtimes. The durable execution SDK has minimal impact on cold start performance. Use provisioned concurrency if cold start latency is critical for your application.
