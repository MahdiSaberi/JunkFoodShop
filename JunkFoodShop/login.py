import json
import menu
import os
import options
import register
import options


def login_page(username,password):

    login_user = True
    while(login_user):
        data_login = open("data_login.txt", "r")
        content = data_login.read()
        if content != "False":
            idx = content.find(",")
            username = content[0:idx]
            password = content[idx + 1:]

        elif content == "False":
            username = input("username: ")
            password = input("password: ")

        with open('user_pass.json', 'r') as json_file:
            content = json.load(json_file)
            pairs = content.items()

        key_nums = 0
        for key, value in pairs:
            flag = 0
            key_nums += 1
        for key, value in pairs:

            for keys in range(0, key_nums):

                if username == key and password == value:

                    print("Welcome,", username)
                    # create text file for data login flag!
                    data_login = open("data_login.txt", "w")
                    data_login.write(username+","+password)
                    data_login.close()
                    login_user = False
                    flag = 1
                    #client_user = username
                    break

                if keys == key_nums-1 and login_user:
                    login_user = True
                    flag = 1


        if flag == 1 and login_user != False:
            print("Your username or password is wrong!")
            flag = 0
            continue

        if flag == 1 and login_user == False:
            login_options(username)

    return username,password


def login_options(user):
    print("\nHello, "+ user)

    print("\n1. Menu\n2. Edit profile\n3. Logout")
    selection = 0
    try:
        selection = input()
        selection = int(selection)
    except ValueError:
        print("Please enter the correct number")
    if selection == 1:
        menu.Menu()
    if selection == 2:
        edit_profile(user)
    if selection == 3:
        print("GoodBye, "+user)
        data_login = open("data_login.txt","w")
        data_login.write("False")
        options.welcome(selection="")


def edit_profile(user):
    print("1. Edit username\n2. Edit password")

    selection = input()
    if selection == "1":
        print("Enter new username: ")
        new_username = str(input())
        with open('user_pass.json', 'r') as user_pass_data:
            #content
            upd = json.load(user_pass_data)
            #pairs
            pairs = upd.items()

            for key, value in pairs:
                #print(key+">"+user)
                if key == user:

                    with open('text.txt', 'w') as outfile:
                        json.dump(upd, outfile)

                    with open('text.txt','r') as file:
                        text = file.read()
                        if text.find('''"'''+new_username+'''"'''+":") == -1:
                            text = text.replace('''"'''+user+'''"'''+":",'''"'''+new_username+'''"'''+":")
                            print("Your username was changed successfully! Please login again")
                            data_login_content = open("data_login.txt","w")
                            data_login_content.write("False")
                            data_login_content.close()

                        elif text.find('''"'''+new_username+'''"'''+":") != -1:
                            print("This username was reserved!")

                    with open('text.txt','a') as f:
                        f.truncate(0)
                        f.write(text)

        os.remove('user_pass.json')
        os.rename(r'text.txt',r'user_pass.json')
        options.welcome(selection="")

    if selection == "2":
        print("Enter current password: ")
        current_password = str(input())
        with open('user_pass.json', 'r') as user_pass_data:
            upd = json.load(user_pass_data)
            pairs = upd.items()

            password_check = False
            for key, value in pairs:
                if key == user:
                    if value == current_password:
                        password_check = True
                        break
                    elif value != current_password:
                        print("Your current password that you entered is wrong!")
                        break

            user_pass_data.close()

            if password_check == True:
                print("Type new password: ")
                new_password = str(input())
                with open('user_pass.json', 'r') as user_pass_data:
                    # content
                    upd = json.load(user_pass_data)
                    # pairs
                    pairs = upd.items()

                    for key, value in pairs:
                        #print(key + ">" + user)
                        if key == user and value == current_password:
                            with open('text.txt', 'w') as outfile:
                                json.dump(upd, outfile)

                            with open('text.txt', 'r') as file:
                                text = file.read()
                                text = text.replace('''"'''+user+'''"'''+": "+'''"'''+current_password+'''"''', '''"'''+user+'''"'''+": "+'''"'''+new_password+'''"''')

                            with open('text.txt', 'a') as f:
                                f.truncate(0)
                                f.write(text)
                    print("Your password was changed successfully! Please login again")
                    data_login_content = open("data_login.txt", "w")
                    data_login_content.write("False")
                    data_login_content.close()

                os.remove('user_pass.json')
                os.rename(r'text.txt', r'user_pass.json')
                options.welcome(selection="")
            if password_check == False:
                edit_profile(user)