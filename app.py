import time, requests, json
#import webbrowser

def ing():
    try:            #DOESN'T WORK
        #webbrowser.open('http://origano.clik.polito.it:8888/api/v1/users/1/56/products')
        r = requests.get("http://origano.clik.polito.it:8888/api/v1/users/1/56/products")   #tutti gli ingredienti di user1 scanner56
        r = (r.json())
        print(r)
        #for i in r:
            #json.loads('r')
            #json.loads(r)
            #print(i)
    except:
        print("Error on API request.")

def sen():
    try:
        #webbrowser.open('http://origano.clik.polito.it:8888/api/v1/users/1/scanners/56')
        r = requests.get("http://origano.clik.polito.it:8888/api/v1/users/1/scanners/56")   #user1 scanner56
        print(r.json())
    except:
        print("Error on API request.")

def add():
    data = {}
    print ("Welcome!\nPlease insert your email:")
    data["email"]=input()
    print ("\nWhat is your Username?")
    data["username"]=input()
    print ("\nChoose your password:")
    data["password"] = input()
    print ("\nWhat is your name?")
    data["name"] = input()
    print ("\nWhat is your surname?")
    data["surname"] = input()
    print ("\nWhen were you born? Please insert into yyyy-mm-dd format:")
    data["birthday"] = input()
    print ("\nMale or Female? m/f")
    data ["gender"] = input()
    print ("\nAlmost done! Where do you live now?")
    data ["city"] = input()
    print ("\nWhat is your address?")
    data ["address"] = input()
    print ("\nWhat is your postal code?")
    data ["postalCode"] = input()
    print ("Thank you for your time! Adding user...\n")
    #print (data) test
    json_data=json.dumps(data)
    #print(json_data) test
    try:
        r = requests.post("http://origano.clik.polito.it:8888/api/v1/users", data=json_data)
        print(r.status_code, r.reason)
    except:
        print("Error on API request.")


while(1):
    print ("Press:\n    i to see all your ingredients;\n    s to see your fridge state;\n    a to add a new user;\n")
    a = input()
    # def switch(a):
    #     switcher = {
    #         0: "ing",
    #         1: "sen",
    #         2: "add",
    #     }
    #     print ("Invalid button!")
    #     return switcher.get(a, "nothing")

    if a == "i":
        ing()
    elif a == "s":
        sen()
    elif a == "a":
        add()
    else:
        print ("Try again! You have pushed the wrong button\n")
