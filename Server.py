#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import cv2
import pickle
import struct


# In[ ]:


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)
port = 10050
socket_address = (host_ip,port)


# In[ ]:


server_socket.bind(socket_address)


# In[ ]:


server_socket.listen(5)
print("LISTENING AT:",socket_address)


# In[ ]:


while True:
    client_socket,addr = server_socket.accept()
    print('GOT CONNECTION FROM:',addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        
        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            
            cv2.imshow('VIDEO FROM SERVER',frame)
            key = cv2.waitKey(10) 
            if key ==13:
                client_socket.close()
                cv2.destroyAllWindows()

