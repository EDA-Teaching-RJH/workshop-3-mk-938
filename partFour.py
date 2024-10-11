allowed_user = ["admin"]
allowed_pass = ["password123"]
allowed = "false"
while allowed != "true":
    username = input("Enter username: ")
    if username in allowed_user:
        password = input("Enter password")
        if password in allowed_pass:
            print ("welcome")
            allowed = ("true")
        else: 
            print ("password incorrect")
    else:
        print ("username incorrect")