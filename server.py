#Name: Vineeth Xavier
#ID: 1001169649
#http://www.w3resource.com/python/python-tutorial.php
#http://stackoverflow.com/questions/2846653/how-to-use-threading-in-python
#https://docs.python.org/2/library/threading.html
#https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python
#http://ilab.cs.byu.edu/python/threadingmodule.html
#https://www.youtube.com/watch?v=XiVVYfgDolU

from socket import * #impporting required header files 
import sys
import thread

def serving(conSoc,ipAddress):                                                      
    try:

        msgContent =  conSoc.recv(1024)
        print "msg = "+ msgContent #printing the message content
        print 'connected ipAddress is:',ipAddress # printing IP address
        print 'hostname of the client:localhost' # printing the details
        print '----------------'

        print 'protocol : TCP'
        print 'Socket family: AF_INET'
        print 'Socket type: SOCK_STREAM'
        

        if msgContent.split()[0] == "GET": #comparing with GET method
              fName = msgContent.split()[1] #getting file name without extension 

        else:
              fName = msgContent  #assigining the file name as content
        fp = open(fName[1:]) #open function to read the content of the file bye opening it
        outputdata = fp.read() # after opening, the content is read and stored in outputdata
        
        for i in range(0,len(outputdata)): # for loop to send the data till the last line of the file
            conSoc.send(outputdata[i])
        conSoc.close()

    except IOError: # when ther is no file name specified, leads to not found
        
        print "404 Error:  File Not Found!!!"
        print "-----------------------------"
        conSoc.send('HTTP/1.1 404 File Not Found\r\n') 
        conSoc.send('Content-Type: text/html\r\n\r\n<html><h1>404 File Not Found</h1></html>')
        conSoc.close()                                    

def main(): # main function
    srvSock = socket(AF_INET, SOCK_STREAM)
    hostname='' # hostname variable 
    portID= 8080 # variable port hols port number
    srvSock.bind((hostname,portID)) #binding port and host name
    print "Socket Number: ",srvSock.getsockname()[1] #printing socket number
    srvSock.listen(10)

    while True:
        print 'connection establishing...Ready to serve... '
        conSoc, ipAddress =  srvSock.accept()
        thread.start_new_thread(serving, (conSoc,ipAddress)) #starting new thread 

if __name__=="__main__":
        main()