import json
import login
import options

def register_user(user,password):

    with open('user_pass.json', 'r') as json_file:
        content = json.load(json_file)
        pairs = content.items()

    reserved = True
    while (reserved):

        user = input("Create your username: ")
        for key, value in pairs:
            flag = 0
            if user == key:
                print("This username reserved, Please create another username!")
                flag = 1
                reserved = True
                break
            elif user != key:
                if flag == 0:
                    reserved = False

    password = input("Type your password: ")
    Account_set = {user: password}

    print("Congratulations, Your registration was successful!")
    data_login_content = open("data_login.txt", "w")
    data_login_content.write("False")
    data_login_content.close()

    str_content = str(content)
    str_content = str_content.replace(" ", "")
    str_content = str_content.replace("'", '"')
    update_contents = json.loads(str_content)
    update_contents.update(Account_set)

    with open('user_pass.json', 'w') as json_file:
        json.dump(update_contents, json_file)
    options.welcome(selection="")
    #login.login_page(user,password)