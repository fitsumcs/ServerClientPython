import socket
import sys
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.10.101', 8080))                   #IP is the server IP

#replace your text here
text_To_Send=  "Hello There !!!"

#send to server ..
s.sendall(text_To_Send.encode())
 
print('goodbye!')