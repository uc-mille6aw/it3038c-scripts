var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

	var servertime = os.uptime();
	var minutes = servertime/60
	var hours = minutes/60
	var days = hours/24

	servertime = Math.floor(servertime)
	minutes = Math.floor(minutes)
	hours = Math.floor(hours)
	days = Math.floor(days)

	
	hours = hours%24;
	minutes = minutes%60;
	servertime = servertime%60;


	var memBytes = os.totalmem
	var memMB = memBytes*0.000001
	var memory = memMB.toFixed(2)

	memoryUsed = os.freemem();
	memused = memoryUsed*0.000001
	MBused = memused.toFixed(2)

	var cpu = os.cpus();
	var cpuNum = cpu.length


http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: Days: ${days}, Hours: ${hours}, Minutes: ${minutes}, Seconds: ${servertime}</p>
            <p>Total Memory: ${memory} MB </p>
            <p>Free Memory: ${MBused} MB</p>
            <p>Number of CPUs: ${cpuNum}</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");
