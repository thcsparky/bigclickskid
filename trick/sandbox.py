import socket
import os

def main():
    a = open(os.getcwd() + '/image0.png', 'rb')
    b = a.read()
    a.close()

    a = open(os.getcwd() + '/txtresponse.txt')
    c = a.read()
    a.close()

    d = c.encode()
    e = d + b

    a = open(os.getcwd() + '/txtresponse2.txt', 'wb')
    a.write(e)
    a.close()
    print('wrote to: " ' + os.getcwd() + '/txtresponse2.txt' + '"')
    

if __name__ == "__main__":
    main()
