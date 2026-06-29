# Press 1 for Adding Note 
# Press 2 for Display Note
# Press 3 to Exit 
while True:
    print('''===== Notes App =====
        1. Add Note
        2. Show Notes
        3. Exit''')
    try:
        user = int(input("Enter a number -> "))     
    except:
        print("Enter a valid number")
        continue
    if user == 1:
        note = input("Enter note -> ")
        with open("notes.txt","a") as f:
         f.write(note + "\n")
         print("✅ Note Saved Successfully")
    elif user == 2:
        with open("notes.txt", "r") as f1:
         print(f1.read())
    elif user == 3:
        print("Exit")
        break
    else:
        print("Wrong Input")

 