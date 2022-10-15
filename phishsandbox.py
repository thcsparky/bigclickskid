import os
import re 
import socketserver

def main():
    str1 = os.getcwd()
    str2 = str1 + '/file.txt'
    print(str2)
    quit()

if __name__ == "__main__":
    main()