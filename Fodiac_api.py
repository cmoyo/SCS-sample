#Fodiac_api.py

import os
import socket
import sys
import binascii


#Functions to determine how to send data

def send_BOOL(SD):
    '''61499 BOOL case'''
    if type(SD)==bool:
        if (SD==True):
            SD_out=b'\x41'

        if (SD==False):
            SD_out=b'\x40'
            
    else:
        raise ValueError('Value is not Bool type')
    
    return SD_out


def send_INT(SD):
    '''61499 INT case'''
    if type(SD)==int:
        if (SD>=-32768)and(SD<=32767):
            s1=bytearray(b'\x47')
            s2=bytearray(struct.pack('h',SD))
            s2[:]=s2[::-1]
            SD_out=bytes(s1+s2)
    
    else:
        raise ValueError('Value is not INT type')
    
    return SD_out
    

def send_UINT(SD):
    '''61499 UINT case'''
    if type(SD)==int:
        if (SD>=0)and(SD<=65535):
            s1=bytearray(b'\x47')
            s2=bytearray(SD.to_bytes(4, byteorder='big'))
            SD_out=bytes(s1+s2)

    else:
        raise ValueError('Value is not UINT type')

    return SD_out

def send_REAL (SD):
    '''61499 REAL case'''
    if type(SD)==float:
        s1=bytearray(b'\x4A')
        s2=bytearray(struct.pack('f',SD))
        s2[:]=s2[::-1]
        SD_out=bytes(s1+s2)
        
    else:
        raise ValueError('Value is not REAL type')

    return SD_out

def send_LREAL (SD):
    '''61499 REAL case'''
    if type(SD)==float:
        s1=bytearray(b'\x4B')
        s2=bytearray(struct.pack('d',SD))
        s2[:]=s2[::-1]
        SD_out=bytes(s1+s2)
        
    else:
        raise ValueError('Value is not LREAL type')

    return SD_out
        
    
rules= (('BOOL', send_BOOL),
        ('INT', send_INT),
        ('UINT', send_UINT),
        ('REAL', send_REAL),
        ('LREAL', send_LREAL),
        )

def data_convert(SD, datatype):
    for data_type, conv_func in rules:
        if datatype== data_type:
            return conv_func(SD)


def send_to_FDIAC (device_addr,datatype,SD):
    TCP_IP = '127.0.0.1'
    TCP_PORT = device_addr
    BUFFER_SIZE = 1024


    TX=data_convert(SD,datatype)


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((TCP_IP, TCP_PORT))

    s.send(TX)

    data = s.recv(BUFFER_SIZE)

    s.close()

    #man=bytearray (binascii.hexlify(data)) - check if required

    print ('received data:', binascii.hexlify(data))

    return (binascii.hexlify(data))

