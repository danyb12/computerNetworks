# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:53:42 2019

@author: DHANUSH
"""

import os,datetime, time, os.path,codecs,base64,webbrowser
from socket import*

server='127.0.0.1'
sport=8000
dataLen=10000000
#instructors hint
def getDate(filename):
    secs = os.path.getmtime("filename.html")   
    t = time.gmtime(secs)
    last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT", t)
    return last_mod_time


#mickey696 github
def getData(filename):
    Data=""
    with open(filename,"r") as f:
        for line in f.readlines():
            if '<p class="p1">' in line:
                Data+=line
    Data=Data.replace('<p class="p1">', '')
    Data=Data.replace('</p>','')
    Data=Data.replace('&lt;','<')
    Data=Data.replace('&gt;','>')
    return Data
    
    
serverSocket=socket(AF_INET, SOCK_STREAM)

serverSocket.bind((server, sport))

# Listen for incoming connection requests



serverSocket.listen(1)
print('The server is ready to serve on port: ' + str(sport))

while True:
    Lmdto=""
    ResponseData=''
    connectionSocket, address = serverSocket.accept()
    
    
    RequestData = connectionSocket.recv(dataLen).decode()
    
    t = datetime.datetime.utcnow()
    RequestDateTime = t.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print("REQUEST MESSAGE RECIEVED")
    print()
    
    print(RequestData)


    for item in RequestData.split():
        if item[0]=="/":
            filename=item[1:]
            break
        #stack overflow
    if not(os.path.isfile(filename)):
       
        notFound="HTTP/1.1 404 Not Found" + "\r\n"+"Date: " + RequestDateTime + "\r\n"+"\r\n"
        connectionSocket.send(notFound.encode())

        
        
    else:
       
        LMDTC = getDate(filename)
       
        for lines in RequestData.splitlines():
            if "If-Modified-Since" in lines:
                Lmdto=lines[15:]    
        
        if LMDTC in Lmdto:
             
            notModified="HTTP/1.1 304 Not Modified\r\n"+"Date: " + RequestDateTime + "\r\n"+"\r\n"
            connectionSocket.send(notModified.encode())
        else:
            ContentData = getData(filename)
            ContentLength = str(len(ContentData))
            OK="HTTP/1.1 200 OK" + "\r\n"+"Date: " + RequestDateTime  + "\r\n"+"Last-Modified: " + LMDTC + "\r\n"+"Content-Length: " + ContentLength + "\r\n"+"Content-Type: text/html; charset=UTF-8" + "\r\n"+"\r\n" + ContentData
            connectionSocket.send(OK.encode())




    connectionSocket.close()
