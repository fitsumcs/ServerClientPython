import socket
import sys
 
HOST = '192.168.10.120' #this is your localhost
PORT = 8080
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.socket: must use to create a socket.
#socket.AF_INET: Address Format, Internet = IP Addresses.
#socket.SOCK_STREAM: two-way, connection-based byte streams.
print('socket created')
 
#Bind socket to Host and Port
try:
    s.bind((HOST, PORT))
except socket.error as err:
    print('Bind Failed, Error Code: ')
    sys.exit()
 
print('Socket Bind Success!')
 
 
#listen(): This method sets up and start TCP listener.
s.listen(10)
print('Socket is now listening')
 
 
while 1:
    conn, addr = s.accept()
    print('Connect with ' + addr[0] + ':' + str(addr[1]))
    buf = conn.recv(1024)
    print(buf.decode("utf-8"))
s.close()
 
