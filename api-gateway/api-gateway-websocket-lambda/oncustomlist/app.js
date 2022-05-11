const AWS = require('aws-sdk');

const ddb = new AWS.DynamoDB.DocumentClient({ apiVersion: '2012-08-10', region: process.env.AWS_REGION });

const { TABLE_NAME } = process.env;

exports.handler = async event => {
  console.log(event);
  let connectionData;
  
  if (event.body === undefined) {
	 console.log("received empty message, returning");
     return { statusCode: 200, body: 'noop' };
  }
  
 let postData = "invalid";
  try {
      console.log(event.body);
      let o = JSON.parse(event.body);
     
        if (o && typeof o === "object") {
            postData = "list: " +  o.data;
        } else {
	          console.log("received non json input");
            return { statusCode: 200, body: 'noop' };
        }
  } catch (e) {
    console.log(e);
    return { statusCode: 500, body: 'input must be json with data attribute' };
  }
  
  
  try {
    connectionData = await ddb.scan({ TableName: TABLE_NAME, ProjectionExpression: 'connectionId' }).promise();
  } catch (e) {
    console.log(e);
    return { statusCode: 500, body: e.stack };
  }
  
  const apigwManagementApi = new AWS.ApiGatewayManagementApi({
    apiVersion: '2018-11-29',
    endpoint: event.requestContext.domainName + '/' + event.requestContext.stage
  });

  const postCalls = connectionData.Items.map(async ({ connectionId }) => {
    try {
      await apigwManagementApi.postToConnection({ ConnectionId: connectionId, Data: postData }).promise();
    } catch (e) {
      console.log(e);
      if (e.statusCode === 410) {
        console.log(`Found stale connection, deleting ${connectionId}`);
        await ddb.delete({ TableName: TABLE_NAME, Key: { connectionId } }).promise();
      } else {
        throw e;
      }
    }
  });
  
  try {
    await Promise.all(postCalls);
  } catch (e) {
    console.log(e);
    return { statusCode: 500, body: e.stack };
  }
  
  console.log("complete");

  return { statusCode: 200, body: 'Data sent.' };
};