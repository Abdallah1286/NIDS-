import socket
import time

# send one UDP packet 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'AAAAAAAAAAA', ("20.203.57.169", 443))  # 11 bytes same value OUT_BYTES
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'AAAAAAAAAAA', ("20.203.57.169", 443))  # 11 bytes same value OUT_BYTES
