const http = require('http');

// Module scope runs once, during the image BUILD. The values below are captured
// in the snapshot, so every MicroVM launched from this image version reports
// the same builtAt and snapshotValue. That is the snapshot-uniqueness trap.
const builtAt = new Date().toISOString();
const snapshotValue = Math.random().toString(36).slice(2, 10);

// In-memory state. It survives suspend/resume, and starts at 0 in every new MicroVM.
let requestCount = 0;

const server = http.createServer((req, res) => {
  requestCount += 1;
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    message: 'hello from a Lambda MicroVM',
    path: req.url,
    environment: process.env.APP_ENV,
    builtAt,
    snapshotValue,
    requestCount,
    now: new Date().toISOString(),
  }));
});

server.listen(8080, () => {
  console.log('Listening on port 8080');
});
