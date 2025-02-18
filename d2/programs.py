'''input_number=int(input("enter a number to check if its even or odd:"))
if input_number%2==0:
    print("it is an even number")
else:
    print("it is an odd number")

employee_name=input("enter employee's name:")
employee_salary=int(input("enter employee's salary:"))
if employee_salary>300000:
    print("the employee has to pay tax")
else:
    print("the employee does not have to pay tax")

number_1=int(input("enter the 1st number:"))
number_2=int(input("enter the 2nd number:"))
number_3=int(input("enter the 3rd number:"))
if number_1>=number_2 and number_1>=number_3:
    print(number_1,"is the greatest")
elif number_2>=number_1 and number_2>=number_3:
    print(number_2,"is the greatest")
else:
    print(number_3,"is the greatest")

year=int(input("enter the year to check leap year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")

student_name=input("enter students's name:")
score1=int(input("enter score in subject 1:"))
score2=int(input("enter score in subject 2:"))
score3=int(input("enter score in subject 3:"))
total=score1+score2+score3
average=total/3
print("name of the student:",student_name)
print("total score:",total)
print("average score:",average)
if average>=60:
    print("1st class")
elif average>=50:
    print("2nd class")
elif average>=35:
    print("pass class")
else:
    print("fail")

employee_name=input("enter employee's name:")
employee_id=input("enter employee id")
basic_salary=int(input("enter the basic monthly salary:"))
special_allowance=int(input("enter monthly special allowance:"))
bonus_percentage=int(input("enter bonus percentage(annual):"))
gross_monthly_salary=basic_salary+special_allowance
annual_gross_salary=(gross_monthly_salary*12)+(gross_monthly_salary*bonus_percentage/100)
print("employee details:")
print("employee name:",employee_name)
print("employee id:",employee_id)
print("gross monthly salary:",gross_monthly_salary)
print("annual gross salary:",annual_gross_salary)'''







