var http = require('http');
var host = '172.21.111.123';
var path = '/api/policies/577029111';
var patientId = '';

var fullPath = path + patientId;

console.log(fullPath);
console.log(path);

var options = {
  host,
  path
};

http.request(options, function(res) {
  console.log('STATUS: ' + res.statusCode);
  console.log('HEADERS: ' + JSON.stringify(res.headers));
  res.setEncoding('utf8');
  res.on('data', function (chunk) {
    console.log('BODY: ' + chunk);
  });
}).end();