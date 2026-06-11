# scaning one port

import socket


# to create a TCP/IPv4 connection endpoint: a socket object
sock= socket.socket(
    # the IPv4 one 
    socket.AF_INET, 
    # for ipv6 address family use:  AF_INET6
    # the tcp connection build
    socket.SOCK_STREAM
)

# ffor scanning professioanlly (both v4 and v6 protocols)
result0= socket.getaddrinfo("google.com" , 80)

# test only one port. use the connect exception method bcz for the connect(), you should throw excpetion manually
result= sock.connect_ex(
    # pass the host and the tuple
    ("google.com", 80)
)

print(result , "result0 = ",result0)

sock.close()