import json
import options
import login

def Menu():
    with open('menu.json', 'r') as json_file:
        content = json.load(json_file)
        pairs = content.items()
        counter = 1
        for key, value in pairs:
            print(str(counter) + ". " + "Food: "+ key," - Price: "+ value)
            counter += 1
        print("0. back")
        Choose(choose="")

def Choose(choose):
    choose = int(input("Choose: "))
    with open('menu.json', 'r') as json_file:
        content = json.load(json_file)
        pairs = content.items()
        counter = 1
        for key, value in pairs:
            #print(str(counter) + ". " + "Food: "+ key," - Price: "+ value)
            if choose == counter:

                print("Your order is "+key+" with a price of "+value)
                print("1. Payoff\n2. Cancel")
                select = input()

                if select == "1":
                    pass
                elif select == "2":
                    Menu()
            if choose == 0:
                data_login = open("data_login.txt","r")
                content = data_login.read()
                if content != "False":
                    login.login_page(username=content,password="123")
                elif content == "False":
                    options.welcome(selection="")

            counter += 1