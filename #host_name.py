import socket

ipAddress = "8.8.8.8"

hostName = socket.gethostbyaddr(ipAddress)

print("Host Name for the IP address {} is {}".format(ipAddress, hostName))
