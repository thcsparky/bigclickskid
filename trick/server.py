import os
import socketserver
socketstate = 0

class tcpsocket(socketserver.BaseRequestHandler):
    def handle(self):
        global socketstate
        self.data = self.request.recv(1024).strip()

        dat = ''
        try:
            dat = self.data.decode()
        except Exception as e:
            print(e)

        if dat.find("Discordbot") > -1:
            a = open(os.getcwd() + '/txtresponse2.txt', 'rb')
            b = a.read()
            a.close()
            self.request.sendall(b)
            print(dat)

        elif dat.find("Discordbot") == -1:
            c = b"HTTP/1.1 302 Found\nLocation: https://thesaurus.com/browse/retard"
            self.request.sendall(c)
            print(dat)

def main():
    global socketstate
    HOST, PORT = "165.22.180.241", 80
    
    with socketserver.TCPServer((HOST, PORT), tcpsocket) as server:
        server.serve_forever()

if __name__ == "__main__":
    main()
