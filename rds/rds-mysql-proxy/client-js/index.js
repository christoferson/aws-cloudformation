const AWS = require('aws-sdk');
var mysql2 = require('mysql2');
let fs  = require('fs');
import * as path from 'path';

// This example is when you need to login using IAM credentials
// Proxy needs to enable IAM and TLS

let connection;

exports.handler = async(event, context) => {
	const promise = new Promise(function(resolve, reject) {
        
		console.log("Starting query ...\n");
	  	console.log("Running iam auth ...\n");
      
        const regionid = "us-west-1";
        const username = "admin";
        const proxyendpoint = "my-xx.us-west-1.rds.amazonaws.com";
      	const databasename = "demo";
      	
      	const sslOptions = {
				  ca: fs.readFileSync(path.join(__dirname, 'AmazonRootCA1.pem')),
				  rejectUnauthorized: true
				};

    	var signer = new AWS.RDS.Signer({
	        region: regionid,
	        hostname: proxyendpoint,
	        port: 3306,
	        username: username
  		});
        
	    let token = signer.getAuthToken({
	      username: username
	    });
    
        console.log(token);
        console.log ("IAM Token obtained\n");
    
        let connectionConfig = {
          host: proxyendpoint, // Store your endpoint as an env var
          user: username,
          database: databasename,
          ssl: sslOptions, //'Amazon RDS', //ssl: { rejectUnauthorized: false},
          password: token,
          authPlugins: {
				    mysql_clear_password: () => { 
						    	console.log('mysql_clear_password plugin init'); 
						    	
                  return () => {
						         signer.getAuthToken({
								          region: regionid,
								          hostname: proxyendpoint,
								          port: 3306,
								          username: username
											});
                  };
						  }
				   }
        };
   		

        
        connection = mysql2.createConnection(connectionConfig);
		
		connection.connect(function(err) {
			if (err) {
				console.log('error connecting: ' + err.stack);
				return;
			}
			
			console.log('connected as id ' + connection.threadId + "\n");
		 });

		//const [rows, fields] = connection.query("SELECT 1");
        //console.log(rows);
        var sql ="SELECT * FROM information_schema.PROCESSLIST";
        
	    // Execute
	    connection.query(sql, function(err, rows, fields) {
	        if (err) {
	            console.log("Execute Error");
	            context.fail(err);
	            throw err;
	        } else {
	            console.log("Execute Success");
	            console.log(rows);
	        }
	        context.done();
	    });
    
	});
	return promise;
};