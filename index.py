from socketIO_client import SocketIO, LoggingNamespace

def handleResponse(*args):
  print('MSG: ', args);

with SocketIO('localhost', 3000, LoggingNamespace) as socketIO:
  socketIO.on('response', handleResponse)
  socketIO.emit('message', 'hello client')
  socketIO.wait(seconds=30)
