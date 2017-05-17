#Name: Vineeth Xavier
#ID: 1001169649
#http://www.w3resource.com/python/python-tutorial.php
#http://stackoverflow.com/questions/2846653/how-to-use-threading-in-python
#https://docs.python.org/2/library/threading.html
#https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python
#http://ilab.cs.byu.edu/python/threadingmodule.html
#https://www.youtube.com/watch?v=XiVVYfgDolU
import socket #importing header files
from socket import *
import thread
import time
import sys 
def client():
    
    srvSock = socket(AF_INET, SOCK_STREAM)
    srvSock.connect(("localhost", 8080)) #getting ip and port number
    fileName= raw_input("Enter the path of file or filename if its in same directory: ") #getting filr name 
    startTime=time.time() # start time recorded when initialized 
    srvSock.send('GET /'+fileName+' HTTP/1.1')
   
    print 'Socket family: AF_INET \n sicket type: SOCK_STREAM \n host name of the server: Localhost'     
   
    print '-----HTTP responses-----' # print statement
    fileContent=srvSock.recv(4096) #storing file content in fileContent
    totalTime=time.time()-startTime # calculating total time/rrt
    
    print'rtt- round trip time',totalTime #printing rount trip time, i.e total time taken
    print("Client connected on Destination IP and Destination port -peer name\n" +str(srvSock.getpeername())) # printing peer name
    print 'timeout: 0' 
    print 'the file contents showed in web browser'
    print fileContent # printing the file conntents read 
    srvSock.close() # closing the socket 

if __name__== '__main__': # first line of code executed 
    client() #function that need to be executed at the start 
