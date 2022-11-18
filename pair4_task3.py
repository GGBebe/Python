employeesCount = 0
while True:
    try:
        while employeesCount <= 0:
            employeesCount = int(input("Enter the number of employees: "))
    except:
        print("Incorrect entry!")
    else:
        break
file = open("employees.txt", "a+")
for employee in range(employeesCount):
    employeeName = input(f"Enter the {employee+1}. employee's name: ")
    employeeSurname = input(f"Enter the {employee+1}. employee's surname: ")
    while True:
        try:
            employeeSalary = float(input(f"Enter the {employee+1}. employee's salary:"))
        except:
            print("Incorrect entry!")
        else:
            break
    file.writelines(f"{employeeName.upper()} {employeeSurname.upper()} - {employeeSalary}\n")
file.seek(0)
print(file.read())
file.close()
