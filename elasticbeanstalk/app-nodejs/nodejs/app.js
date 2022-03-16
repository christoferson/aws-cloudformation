let port = process.env.PORT || 3000;
let http = require('http');
let fs = require('fs');
let html = fs.readFileSync('index.html');

let log = function(entry) {
    let msg = new Date().toISOString() + ' - ' + entry + '\n';
    fs.appendFileSync('/tmp/sample-app.log', msg);
};

let server = http.createServer(function (req, res) {
 
    if (req.method === 'POST') {
        var body = '';

        req.on('data', function(chunk) {
            body += chunk;
        });

        req.on('end', function() {
            console.log(body);
            if (req.url === '/') {
                log('Received message: ' + body);
            } else if (req.url = '/scheduled') {
                log('Received task ' + req.headers['x-aws-sqsd-taskname'] + ' scheduled at ' + req.headers['x-aws-sqsd-scheduled-at']);
            }

            res.writeHead(200, 'OK', {'Content-Type': 'text/plain'});
            res.end();
        });
    } else {
        res.writeHead(200);
        res.write(html);
        res.end();
    }
});

// Listen on port 3000, IP defaults to 127.0.0.1
server.listen(port);

// Put a friendly message on the terminal
console.log('Server running at http://127.0.0.1:' + port + '/');
