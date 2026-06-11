# scaning multiple ports with user selectint the host adress

import socket
host= input('please enter the host name = ')
ip= socket.gethostbyaddr(host)
for i in range (1,101):
    result= socket.getaddrinfo(
    str(ip) , i
    )

print(result)