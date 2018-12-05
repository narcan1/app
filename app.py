import os, time
import requests
#import webbrowser

def ing():
    try:
        #webbrowser.open('http://origano.clik.polito.it:8888/api/v1/users/1/56/products')
        r = requests.get("http://origano.clik.polito.it:8888/api/v1/users/1/56/products")   #tutti gli ingredienti di user1 scanner56
        for i in r:
            print(i, end="\n\n")
    except:
        print("Error on API request.")

def sen():
    try:
        #webbrowser.open('http://origano.clik.polito.it:8888/api/v1/users/1/scanners/56')
        r = requests.get("http://origano.clik.polito.it:8888/api/v1/users/1/scanners/56")   #user1 scanner56
    except:
        print("Error on API request.")

while(1):
    print ("Premi:\n    i per vedere gli ingredienti;\n    s per vedere i valori dei sensori;\n")
    a = input()
    if a == "i":
        ing()
    elif a == "s":
        sen()
    else:
        print ("Try again! You have pushed the wrong button\n")
