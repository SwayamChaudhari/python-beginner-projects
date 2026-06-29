count = 1
while True:
    print('''
       ===== Student Record Manager =====

      1. Add Student
      2. Show Students
      3. Exit''')
    try:
        user = int(input("Enter number -> "))
    except:
        print("Enter a valid Number")
        continue
    if user == 1:
        student_name = input("Enter Student Name -> ")
        if student_name == "":
            print("Student Name cannot be empty")
            continue
        with open("stu_data.txt", "a") as f:
            f.write(student_name + "\n")
            print("✅ Student Added Successfully") 
    elif user == 2:
        with open("stu_data.txt" , "r") as f:
             data = f.readlines()
             if data == []:
                 print("No student records found")
             else:
                count = 1
                for student in data:
                    print(f"{count}: {student}" , end="")
                    count += 1
                print(f"Total no of Students: {len(data)}")
    elif user == 3:   
        print("Goodbye!!!")        
        break
    else:
        print("Invalid Input")
