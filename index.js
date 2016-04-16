var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
io.on('connection', handleConnection);
http.listen(3000);
function handleConnection(socket) {
  socket.on('message', handleMessage);
  function handleMessage(msg) {
    console.log('MSG: ' + msg);
  }
}
