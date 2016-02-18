from threading import Thread
import socket

def getPort():
    return int(raw_input("Port Number: "))

def getOutput():
    fileName = raw_input("Output File: ")
    fileState = open(fileName,"r")
    fileContent = fileState.read().split("\n\n")
    fileState.close()
    return fileContent

def getSocket():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.bind(('0.0.0.0',port))
    c.listen(1)
    return c

def session(cfile):
    for line in output:
        cfile.write(line+"\n")
        print cfile.readline().strip()

if __name__ == "__main__":
    port = getPort()
    output = getOutput()
    connection = getSocket()

    print "\nBasicHoney running on port {}\n".format(str(port))

    while 1:
        csock, caddr = connection.accept()
        cfile = csock.makefile('rw', 0)
        Thread(target=session,args=(cfile,)).start()
