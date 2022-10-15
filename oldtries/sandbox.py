import requests
import os


def gokidsgo():
    a = input('Url? default: 127.0.0.1/').rstrip()
    if a == '':
        url = 'http://127.0.0.1/icons/folder.gif'
        print('grabbing: ' + url)

        req = requests.get(url, timeout=90)
        if req.ok:
            dat = req.text
            print(dat)
        else:
            print('error: ')
            print(str(req.status_code))
    
    else:
        url = a 
        req = requests.get(url, timeout=90)
        if req.ok:
            dat = req.text 
            print(dat)
        else:
            print('error: ')
            print(str(req.status_code))
            
    
def main():
    a = input('ready, type go, or type exit').rstrip()

    if a.find('exit') > -1:
        print('quitting')
        quit()

    if a.find('go') > -1:
        gokidsgo()

    if a == '':
        gokidsgo() 
    main()

if __name__ == "__main__":
    main()