#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "irc.csec.umiacs.umd.edu"   # IP address or URL
port = 4444     # port
binNewln = b'\n'
# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("connecting to " + host + "\n")
s.connect((host, port))

def arithmaticer(data):
    ls = data.split(binNewln)
    arithStr = ls[1].decode('utf-8')
    #print(arithStr)
    result = eval(arithStr)
    #print(result)
    hasher = hashlib.sha256()
    hasher.update(str(result).encode('utf-8'))
    theHashStr = hasher.hexdigest()
    return theHashStr

def receive():
    data = s.recv(1024)
    print("    received: ")
    print(data)
    return data

def send(theHashStr):
    print("sending: " )
    print(theHashStr)
    data = s.send((theHashStr + "\n").encode('utf-8'))
    pass

data = receive()
theHashStr = arithmaticer(data)
send(theHashStr)
data = receive()
theHashStr = arithmaticer(data)
send(theHashStr)
data = receive()
theHashStr = arithmaticer(data)
send(theHashStr)
data = receive()
#send('I love you... as a friend')
#data = receive()

"""
# receive some data
data = s.recv(1024)
print("    received: ")
print(data)
"""

"""
ls = data.split(binNewln)
arithStr = ls[1].decode('utf-8')
print(arithStr)
result = eval(arithStr)
print(result)
hasher = hashlib.sha256()
hasher.update(str(result).encode('utf-8'))
theHashStr = hasher.hexdigest()
"""

"""
print("sending: " )
print(theHashStr)
data = s.send((theHashStr + "\n").encode('utf-8'))

data = s.recv(1024)
print("    received: ")
print(data)
"""

# close the connection
s.close()
