const mysql = require('mysql2/promise');
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
    
    console.log(`Loaded Configuration.`);


}

async function createSingleConnection() {
    
    if (connection !== null) {
        console.log(`Reuse Database Connection.`);
        return;
    }

    connection = await mysql.createConnection({
        host     : mysql_host,
        user     : mysql_user,
        password : mysql_password,
        database : mysql_dbname
    });

    connection.on('error', (err) => {
        if (err.code === 'PROTOCOL_CONNECTION_LOST') {
            // reconnect if connection is lost
            createSingleConnection();
            console.log(`Reconnected`);
        } else {
            throw err;
        }
    });
    
    console.log(`Connected to Database.`);

}

async function executeQuery(context) {

    try {
        const sql = "SELECT * FROM information_schema.PROCESSLIST";
        const [rows, fields] = await connection.query(sql);
        for (const row of rows) {
            //console.log(">>> ", row, row.ID, row.STATE);
            console.log(">>> ", row.ID, row.STATE);
        }
    } catch (e) {
        console.log(e);
        context.fail(e);
    } finally {
        //connection.end();
    }

}

exports.handler = async function(event, context) {
    
    context.callbackWaitsForEmptyEventLoop = false;
    
    count++;

    await readConfiguration();

    console.log(`Count: ${count}`);
    
    await createSingleConnection();
    
    await executeQuery(context);
    
    console.log(`Done`);

    context.done();
    
};