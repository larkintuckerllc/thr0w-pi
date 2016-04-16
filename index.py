import sys
import time
import Adafruit_MPR121.MPR121 as MPR121
from socketIO_client import SocketIO, LoggingNamespace
with SocketIO('localhost', 3000, LoggingNamespace) as socketIO:
	cap = MPR121.MPR121()
	if not cap.begin():
	    print('Error initializing MPR121.  Check your wiring!')
	    sys.exit(1)
	last_touched = cap.touched()
	while True:
	    current_touched = cap.touched()
	    for i in range(12):
		pin_bit = 1 << i
		if current_touched & pin_bit and not last_touched & pin_bit:
                    socketIO.emit('message', '{{"point": {0}, "action": "touched"}}'.format(i))
		if not current_touched & pin_bit and last_touched & pin_bit:
                    socketIO.emit('message', '{{"point": {0}, "action": "released"}}'.format(i))
	    last_touched = current_touched
	    time.sleep(0.1)

