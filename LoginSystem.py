Username = input("Enter Your Username : ")
Password = int(input("Enter Your Password : "))
if Username == "Swayam":
    if Password == 1234:
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Unknown User")
