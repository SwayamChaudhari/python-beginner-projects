balance = 5000
'''
Press 1 For Checking Balance
Press 2 to Withdraw Money
'''
user = int(input("Enter Your Input ->"))
if user == 1:
    print(f"Current Balance: {balance}")
elif user == 2:
    wm = int(input("Enter Amount To Withdraw : "))
    if wm <= balance:
       print(f"Available Balance : {balance - wm}")
    else:
        print("Insufficient Balance")
else:
    print("Invalid Choice")

