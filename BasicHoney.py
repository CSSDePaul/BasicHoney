import socket

port = int(raw_input("Port Number: "))
outputFile = raw_input("Output File: ")
outputFile = open(outputFile,"r")
outputText = outputFile.read().split("\n\n")
outputFile.close()

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.bind(('0.0.0.0',port))
c.listen(1)

print "BasicHoney running on port {}".format(str(port))

while 1:
    csock, caddr = c.accept()
    cfile = csock.makefile('rw', 0)
    for output in outputText:
        cfile.write(output+"\n")
        print cfile.readline().strip()
