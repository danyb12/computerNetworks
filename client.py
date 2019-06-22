import socket
#import urllib.request
import sys
from socket import*
import datetime
import os
import re
import webbrowser
#import http.client
#import requests

#accepting arguments then parsed them from the format of
    #localhost:8000/filename.html

def checkCache():
    try:
        if(os.stat("cache.html").st_size == 0):
            a=False
        else:
            a=True
    except Exception:
        a=False
    return a
    
    



argv = sys.argv
localhostport = argv[1]

host= (localhostport.split(":")[0])

port = int((localhostport.split(":")[1]). split("/")[0])
url = (localhostport.split(":")[1]). split("/")[1]
count=1000000


clientSocket = socket(AF_INET, SOCK_STREAM)
    
    # Create TCP connection to server
clientSocket.connect((host, port))


if checkCache()==False:
    
    RequestData = "GET /" + url + " HTTP/1.1" + "\r\n"
    RequestData += host + ":" + str(port) + "\r\n"
   # RequestData += "\r\n"
    
  
    # Create TCP client socket. Note the use of SOCK_STREAM for TCP packet
    
    
    # Send data through TCP connection
    clientSocket.send(RequestData.encode())
   
    
    # Receive the server response
    ResponseData = clientSocket.recv(4096)
    ResponseData = ResponseData.decode()
    print(ResponseData)
    
    
    with open("cache.html","w+") as cache:
        
        cache.write(ResponseData)
        cache.close();
#if "HTTP/1.1 404" in ResponseData:
#    #if the server returns a 404, that means the file does not exist.
#    print(ResponseData)
#    clientSocket.close()
else:
    #else, the file exist, as such contents will be printed
    #print(ResponseData+"\n")
    #clientSocket.close()

    #The client will now generate the conditional get request.
    #Uncomment the next line to slow the client down and modify the file
    #time.sleep(10) 
    if checkCache()==True:
        
        #Client extracts Last-Modified date to generate the uncoditional get request

        LastModDateTimeOld=""
        with open("cache.html","r") as c:
        
            for line in c.readlines():
                if "Last-Modified" in line:
                    LastModDateTimeOld=line[15:]
        
            c.close()
       
        RequestData = "GET /"+ url +" HTTP/1.1" + "\r\n"
        RequestData += host+":"+str(port)+"\r\n"
        RequestData +="If-Modified-Since: " + LastModDateTimeOld + "\r\n"
       # RequestData += "\r\n"
        
        clientSocket.send(RequestData.encode())
        ResponseData = clientSocket.recv(4096)
        ResponseData = ResponseData.decode()


            
        if "304" in ResponseData:
            print("THE FILE HAS NOT BEEN MODIFIED")
            print(ResponseData+"\n")
        elif "200" in ResponseData:
            print("THE FILE HAS BEEN MODIFIED")
            print(ResponseData+"\n")
            with open("cache.html","w") as c:
                c.write(ResponseData)
                c.close()
        elif "404" in ResponseData:
            print(ResponseData+"\n")

        else:
            print(ResponseData+"\n")
            
        
clientSocket.close()