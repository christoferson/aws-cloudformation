const mysql = require('mysql2');
const ssm = new (require('aws-sdk/clients/ssm'))();

let configurationLoaded = false;
let mysql_host = process.env.DATABASE_ENDPOINT;
let mysql_user = process.env.DATABASE_USER;
let mysql_dbname = process.env.DATABASE_NAME;
let mysql_password = process.env.DATABASE_PASSWORD;

let count = 0;
let connection = null;

async function readSsmParameters(parameterNames, withDecryption) {

    let parameterMap = new Map();
    
    let response = await ssm.getParameters({ Names: parameterNames, WithDecryption: withDecryption }).promise();
	
	for (const parameter of response.Parameters) {
	    parameterMap.set(parameter.Name, parameter.Value);
	    //console.log(`Read Parameter ${parameter.Name}=${parameter.Value}.`);
	}

	return parameterMap;
	
}

async function readConfiguration() {

    count++;

    if (configurationLoaded) {
        return;
    }
    
    let parameterNames = [
        "/demo/database/endpoint",
        "/demo/database/name",
        "/demo/database/user",
        "/demo/database/password"
    ];

    let parameterMap = await readSsmParameters(parameterNames, true);
    
    mysql_host = parameterMap.get("/demo/database/endpoint");
    mysql_user = parameterMap.get("/demo/database/user");
    mysql_dbname = parameterMap.get("/demo/database/name");
    mysql_password = parameterMap.get("/demo/database/password");

    configurationLoaded = true;
    
    return parameterValue;

}


exports.handler = async function(event, context) {
    
    context.callbackWaitsForEmptyEventLoop = false;

    await readConfiguration();

    console.log(`Count: ${count}`);
    
    
    
    console.log(`Done`);

};