var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var thr0w = require('thr0w-api');
thr0w.setBase('192.168.1.19');
thr0w.login('admin', 'monkey', handleLogin);
function handleLogin(error) {
  if (error) {
    process.exit(1);
  }
// TODO: INDENT
io.on('connection', handleConnection);
http.listen(3000);
function handleConnection(socket) {
  socket.on('message', handleMessage);
  function handleMessage(data) {
    var message = JSON.parse(data);
    thr0w.thr0w([0], message);
  }
}
}


