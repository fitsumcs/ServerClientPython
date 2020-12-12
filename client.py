import socket
import sys
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.10.120', 8080)) #IP is the server IP
 
for args in sys.argv:
    if args == "":
        args = "no args"
    else:
        byt= sys.argv[1].encode()
        #s.send(args)
        s.send(byt)
 
print('goodbye!')