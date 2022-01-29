var mysql = require('mysql');

var mysql_host = process.env.DATABASE_ENDPOINT;
var mysql_user = process.env.DATABASE_USER;
let mysql_dbname = process.env.DATABASE_NAME;
var mysql_password = process.env.DATABASE_PASSWORD;

var connection = null;

function createSingleConnection() {
    connection = mysql.createConnection({
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
}

// Create database connection
createSingleConnection();

exports.handler = function(event, context) {

    var sql ="SELECT * FROM information_schema.PROCESSLIST";

    console.log("MySQL Server Name: " + mysql_host);
    console.log("MySQL User Name: " + mysql_user);
    console.log("MySQL Database Name: " + mysql_dbname);
    console.log("MySQL Exec SQL: " + sql);

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

    console.log('end');
};