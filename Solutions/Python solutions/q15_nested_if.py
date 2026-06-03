def login(user, pwd):
    if user == "":
        print("Username cannot be blank")
    else:
        if pwd == "":
            print("Password cannot be blank")
        else:
            if user == "admin":
                if pwd == "pass123":
                    print("Login Successful")
                else:
                    print("Invalid Password")
            else:
                print("Invalid User")

user = "admin"
pwd = "pass123"
login(user, pwd)