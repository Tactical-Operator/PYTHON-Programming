
import socket
host = input("Website\n")
try:
    addr=socket.gethostbyname(host)
    print('IP ADDRESS ='+addr)
except socket.gaierror:
    print('DOES NOT EXIST')    
input("")    