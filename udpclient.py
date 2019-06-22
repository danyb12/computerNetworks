# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:42:50 2019

@author: DHANUSH
"""

import sys, time
from socket import *
# Get the server hostname, port and data length as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]
count = argv[3]
# Command line argument is a string, change the port and count into integer
port = int(port)
count = int(count)
data = 'X' * count # Initialize data to be sent
# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket(AF_INET, SOCK_DGRAM)
# Sending data to server
print("Sending data to " + host + ", " + str(port) + ": " + data)
clientsocket.sendto(data.encode(),(host, port))
# Receive the server response
dataEcho, address = clientsocket.recvfrom(count)
# Display the server response as an output
print("Receive data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
#Close the client socket
clientsocket.close() 