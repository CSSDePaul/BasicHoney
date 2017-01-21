from threading import Thread
import socket

def fileToList(fName,delimiter):
    fState = open(fName,"r")
    fContent = fState.read().split(delimiter)
    fContent = [block.strip() for block in fContent]
    fState.close()
    return fContent

def getSocket(port):
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c.bind(("0.0.0.0",int(port)))
    c.listen(1)
    return c

def session(cfile,output):
    for block in output:
        block = block.replace("\n","\r\n")
        cfile.write(block+"\r\n")
        cfile.readline()

def startHoney(port,fName,delimiter):
    listener = getSocket(port)
    output = fileToList(fName,delimiter)
    print "\nBasicHoney running on port {}\n".format(port)
    while 1:
        csock,caddr = listener.accept()
        cfile = csock.makefile("rw",0)
        Thread(target=session,args=(cfile,output)).start()

if __name__ == "__main__":
    port = raw_input("Port: ")
    fName = raw_input("Filename: ")
    delimiter = raw_input("Delimiter: ")
    startHoney(port,fName,delimiter)
