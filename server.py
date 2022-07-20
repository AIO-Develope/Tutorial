import socket
import sys

HOST = '' # Server
PORT = 8888	# Port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket erstellt'

#Bind socket
try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print 'Bind fehler : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	
print 'Socket bind fertig'

#Start Socket listening
s.listen(10)
print 'Socket ist online'

#keep talking Funktion
while 1:
    #akzeptieren
	conn, addr = s.accept()
	print 'Verbunden mit ' + addr[0] + ':' + str(addr[1])
	
s.close()
