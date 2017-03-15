

//GetRequest

var r_http = require('http');
var r_host = 'localhost:5000';
var r_path = '/messages&seq=';
var r_seq = '1489523746';

var r_fullPath = r_path + r_seq;

console.log(fullPath);
console.log(path);

var r_options = {
  r_host,
  r_fullPath
};

//Get Policies

https.get(r_options, function (res) {
    var request = '';
    res.on('data', function (chunk) {
        policy += chunk;
    });
    res.on('end', function () {
        if (res.statusCode === 200) {
            try {
                var data = JSON.parse(json);
                // data is available here:
                console.log(data.html_url);
            } catch (e) {
                console.log('Error parsing JSON!');
            }
        } else {
            console.log('Status:', res.statusCode);
        }
    });
}).on('error', function (err) {
      console.log('Error:', err);
})


var p_http = require('http');
var p_host = '172.21.111.123';
var p_path = '/api/policies/';
var p_patientId = '577029111';

var p_fullPath = p_path + p_patientId;

console.log(fullPath);
console.log(path);

var p_options = {
  p_host,
  p_fullPath
};

//Get Policies

https.get(p_options, function (res) {
    var policy = '';
    res.on('data', function (chunk) {
        policy += chunk;
    });
    res.on('end', function () {
        if (res.statusCode === 200) {
            try {
                var data = JSON.parse(json);
                // data is available here:
                console.log(data.html_url);
            } catch (e) {
                console.log('Error parsing JSON!');
            }
        } else {
            console.log('Status:', res.statusCode);
        }
    });
}).on('error', function (err) {
      console.log('Error:', err);
})

//Compare
if (Object.equals = function( request, policy ) {
	for (var p in request ) {
		if ( ! request.hasOwnProperty( p ) ) continue;
  
		if ( ! policy.hasOwnProperty( p ) ) return false;
      
		if ( request[ p ] === policy[ p ] ) continue;

		if ( typeof( request[ p ] ) !== "object" ) return false;
      
		if ( ! Object.equals( request[ p ],  policy[ p ] ) ) return false;
      
	}
	return true;
})
