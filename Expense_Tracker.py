
while True:
    print('''===== Expense Tracker =====

    1. Add Expense
    2. Show Expenses
    3. Show Total Expense
    4. Show Highest Expense
    5. Exit''')
    try:
        user = int(input("Enter Number -> "))
    except:
        print("Enter a Valid Number...")
        continue
    if user == 1:
        amount = input("Enter Amount->")
        category = input("Enter Cateogory->")
        with open("expenses.txt" , "a") as f:
            amt = str(amount)
            f.write((amt + "," + category )+ "\n")
    elif user == 2:
        num = 1
        with open("expenses.txt", "r") as f:
            for line in f:
                parts = line.split(",")
                print(f"{num}. ₹{parts[0]} - {parts[1]}" , end="")
                num = num + 1
    elif user == 3:
        total = 0
        with open("expenses.txt", "r") as f:
            for line in f:
                parts = line.split(",")
                parts[0] = int(parts[0])
                total = total + parts[0]
            print(total)
    elif user == 4:
        Highest = 0
        with open("expenses.txt", "r") as f:
            for line in f:
                parts = line.split(",")
                parts[0] = int(parts[0])
                if parts[0] > Highest:
                   Highest = parts[0]
        print(Highest)
    elif user == 5:
        print("byee....")
        break
    else:
        print("Invalid Input")


