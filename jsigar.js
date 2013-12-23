var express = require('express');
var sigar = require('sigar');
var app = express();
// invoke the library
var Sigar = sigar.init();

app.get('/', function(req, res){

	var info = new Date().toLocaleString();
	var version = sigar.version();
	info = info + '-- app version: ' + version.version + '<br/>';
	var mem = Sigar.mem();
	info = info + '--Usedmem: ' + mem.used + ',Totalmem: ' + mem.total + '<br/>';
	var cpu = Sigar.cpu();
	info = info + '--User: ' + cpu.user*100/cpu.total + '%,Sys: ' + cpu.sys*100/cpu.total + '%<br/>';
  res.send(info);

});

app.listen(3000);

console.log("Server listening at 3000...");
