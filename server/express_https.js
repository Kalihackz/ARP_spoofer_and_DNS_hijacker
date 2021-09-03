const express = require("express");
const https = require('https');
const fs = require('fs');
const bodyParser = require("body-parser")
 
// New app using express module
const app = express();
app.use(bodyParser.urlencoded({
    extended:true
}));
 
app.get("/", function(req, res) {
  console.log(time()+"Route : "+app.mountpath)
 //res.sendFile(__dirname + "/dlink/firmware.html");
  res.send('Hello World!')
});

/**app.post("/login", function(req, res) {
  //var pass1 = Number(req.body.password1);
  //var pass2 = Number(req.body.password2);
  console.log(time()+"Route : "+app.mountpath)
  console.log(req.body)
   res.sendFile(__dirname + "/fap/upgrading.html");
});**/

app.get("*", (req, res) => { 
  console.log(time()+"Route : "+app.mountpath)  
   //res.sendFile(__dirname + "/dlink/firmware.html");
   res.send('Hello World!')
});
 
https.createServer({
  key: fs.readFileSync('server/server.key'),
  cert: fs.readFileSync('server/server.cert')
}, app).listen(443, function(){
  console.log("server is running on port 443");
})

function time(){
  const dateObj = new Date();
  return `${dateObj.toDateString()} | ${dateObj.toTimeString()} | `
}
