#basic Version
age = int(input("Enter Your Age : "))
if(age >= 18):
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

#Bonus 1
age = int(input("Enter Your Age : "))
if(age >= 18):
    print("Eligible to Vote")
else:
    print(f"You Can Vote After {18 - age} year")

#Bonus 2
age = int(input("Enter Your Age : "))
if(age >= 18):
    if(age >= 60):
        print("Eligible to Vote")
        print("Senior Citizen")
    else:
        print("Eligible to Vote")
        print("Adult")
else:
    print("Minor")
