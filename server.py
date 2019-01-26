# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:25:37 2019

@author: Rathi
"""

import socket
port = 50006
s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.bind( ('0.0.0.0', port))
raw, addr = s.recvfrom(64000)
print (raw)
s.close()
