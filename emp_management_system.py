attempt = 0
filename = "Employee.txt"
while True:
    print("\n","==*=="*5+"Employee Management System"+"==*=="*5,"\n")
    print("==="*10+"Login Page"+"==="*10,"\n")
    username = input("                    Enter Username    :     ").strip()
    password = input("                    Enter Password    :     ").strip()
    if username == "admin" and password == "1234":
        print("Login Successfully!")
        break
    else:
        print("Invalid username or password Plz try again\n")
        attempt +=1
        if  attempt >= 5:
            print("You have no more attempts ")
            exit()

EmployeeID = 100
import os
while True:
    print("\n","==*=="*5+"Employee Management System"+"==*=="*5,"\n")
    print("=====***====="+"Welcome on Our Admin Panel"+"=====***=====\n")
    print("       =+=*=+=   Enter 1 View Employees    =+=*=+=")
    print("       =+=*=+=   Enter 2 Add Employees     =+=*=+=")
    print("       =+=*=+=   Enter 3 Remove Employees  =+=*=+=")
    print("       =+=*=+=   Enter 4 Update Employees  =+=*=+=")
    print("       =+=*=+=   Enter 5 Search Employees  =+=*=+=")
    print("       =+=*=+=   Enter 0 Exit              =+=*=+=\n")
    print("==="*18,"\n")

    try:
        choice = int(input("             Enter your Choice :      "))
    except ValueError:
        print("Invalid Error : ")
        input("\n          Press Enter to Continue........")
        continue
    except Exception as e:
        print(e)
    match choice:
        case 0:
            print("Program End")
            break
        case 1:
            print("\n    ==*==*==*==  Employee Data  ==*==*==*== \n")
            try:
                with open(filename,"r") as file:
                    count = 0
                    for record in file:
                        data = record.strip().split("||")
                        count +=1
                        print("=="*15,count,"=="*15)
                        print()
                        print("          Employee ID         :    ",data[0])
                        print("          Employee Name       :    ",data[1])
                        print("          Employee Age        :    ",data[2])
                        print("          Employee Department :    ",data[3])
                        print("          Employee Salary     :    ",data[4])
                        print("          Employee Email      :    ",data[5])
                        print()
            except FileNotFoundError:
                with open(filename,"x") as file:
                    print("File Created")
            except Exception as e:
                print(e)
            input("\n          Press Enter to Continue........")    
        case 2:
            print("\n    ==*==*==*==  Add Employee  ==*==*==*== \n")
            try:
                with open(filename,"r") as file:
                    records = file.readlines()
                if records:
                    last_record = records[-1].strip().split("||")
                    EmployeeID = int(last_record[0])
                else:
                    EmployeeID = 100
            except FileNotFoundError:
                with open(filename,"x") as file:
                    print("File Created")
            except Exception as e:
                print(e)
            with open(filename,"a") as file:
                EmployeeID +=1
                name = input("        Enter Name             :     ").strip()
                age = input("        Enter Age              :     ").strip()
                department = input("        Enter Department       :     ").strip()
                salary = input("        Enter Salary           :     ").strip()
                email = input("        Enter Email            :     ").strip()
                    
                records = f"{EmployeeID}||{name}||{age}||{department}||{salary}||{email}\n"
                file.write(records)
                record_exist = True
                print("            New Record added successfully!")
            input("\n          Press Enter to Continue........")    
        case 3:
            print("\n    ==*==*==*==  Remove Employee  ==*==*==*== \n")
            Emp_ID = int(input("         Enter Employee ID :      "))
            is_found = False
            with open(filename,"r") as file:
                Emp_list = file.readlines()
                for record in Emp_list:
                    Emp_record = record.strip().split("||")
                    if int(Emp_record[0]) == Emp_ID:
                        Emp_list.remove(record)
                        is_found = True
                        print(f"      Remove Employee {Emp_ID} Record Successfully")
                        break
            if is_found:
                with open(filename,"w") as file:
                    new_id = 101
                    for record in Emp_list:
                        Emp_record = record.strip().split("||")
                        name = Emp_record[1]
                        age = Emp_record[2]
                        department = Emp_record[3]
                        salary = Emp_record[4]
                        email= Emp_record[5]
                        file.write(f"{new_id}||{name}||{age}||{department}||{salary}||{email}\n")
                        new_id +=1
            else:
                print("Sorry! record in not found")
            input("\n          Press Enter to Continue........")   
        case 4:
            print("\n    ==*==*==*==  Update Employee  ==*==*==*== \n")
            Emp_ID = int(input("            Enter Employee ID   :     "))
            print()
            is_found = False
            with open(filename,"r") as file:
                record = file.readlines()
                for index,data in enumerate(record):
                    Emp_record = data.strip().split("||")
                    if int(Emp_record[0]) == Emp_ID:
                        is_found = True
                        name = input("        Enter Name             :     ").strip()
                        age = input("        Enter Age              :     ").strip()
                        department = input("        Enter Department       :     ").strip()
                        salary = input("        Enter Salary           :     ").strip()
                        email = Emp_record[5]
                        record[index] =f"{Emp_ID}||{name}||{age}||{department}||{salary}||{email}\n"
                        break
            if is_found:
                with open(filename,"w") as file:
                    file.writelines(record)
                    print("   Update Employee Record Successfully! ")
            else:
                print("Sorry! This Record is Not found")
            input("\n          Press Enter to Continue........")   
        case 5:
            print("\n    ==*==*==*==  Search Employee  ==*==*==*== \n")
            Emp_ID = int(input("          Enter Employee ID   :     "))
            print("\n","   ==*=="+f"  The Details of Employee {Emp_ID} is   "+"==*==","\n")
            emp_exist = False
            try:
                with open(filename,"r") as file:
                    Emp_list = file.readlines()   
                    for record in Emp_list:
                        data = record.strip().split("||")
                        if int(data[0]) == Emp_ID:
                            emp_exist = True
                            break
            except FileNotFoundError:
                with open(filename,"x") as file:
                    print("File Created")
            except Exception as e:
                print(e)
            else:
                if emp_exist:
                    print("          Employee ID         :    ",data[0])
                    print("          Employee Name       :    ",data[1])
                    print("          Employee Age        :    ",data[2])
                    print("          Employee Department :    ",data[3])
                    print("          Employee Salary     :    ",data[4])
                    print("          Employee Email      :    ",data[5])
            input("\n          Press Enter to Continue........")  
        case _:
            print("Invalid Entry ")
            input("\n          Press Enter to Continue........") 
    os.system("cls")