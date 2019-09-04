#!/usr/bin/env python

import os
import socket
import sys
import binascii
import struct

TCP_IP = '127.0.0.1'
TCP_PORT = 61501

BUFFER_SIZE = 4096

''' value range = 0 to 65535'''

SD =[2000, -1800, 200,55]
for val in SD:
    
    BUFFER_SIZE = 4096

    ''' value range = 0 to 65535'''

    s1=bytearray(b'\x4A')
    s2=bytearray(struct.pack('f',val))
    s2[:]=s2[::-1]
    TX=bytes(s1+s2)


    print ('sending:', binascii.hexlify(TX))


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((TCP_IP, TCP_PORT))

    s.send(TX)

    data = s.recv(BUFFER_SIZE)

    s.close()


    man=bytearray (binascii.hexlify(data))

    TCP_PORT = TCP_PORT+1

    print ('received data:', binascii.hexlify(data))

print ('loop complete')

