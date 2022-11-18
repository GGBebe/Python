employeesCount = 0
while employeesCount <= 0:
    employeesCount = int(input("Enter the number of employees: "))

file = open("employees.txt", "a")
for employee in range(employeesCount):
    employeeName = input(f"Enter the {employee+1}. employee's name: ")
    employeeSurname = input(f"Enter the {employee+1}. employee's surname: ")
    while True:
        try:
            employeeSalary = float(input(f"Enter the {employee+1}. employee's salary:"))
        except:
            print("Hatalı Giriş Yaptınız.")
        else:
            break
    file.writelines(f"{employeeName.upper()} {employeeSurname.upper()} - {employeeSalary}\n")
file.close()
file = open("employees.txt", "r")
print(file.read())
file.close()