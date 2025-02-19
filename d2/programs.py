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
while True:

    employee_name=input("enter employee's name:")
    if employee_name=='' or not employee_name.isalpha() or len(employee_name)>50:
        print("Error: Name must be non-empty, contain only alphabets, and be at most 50 characters long.")
    else:
        break

    employee_id=input("enter employee id")
    if not employee_id.isalnum() or not(5<=len(employee_id)<=10):
        print("Error: Employee ID must be alphanumeric and 5–10 characters long.")
    else:
        break


    basic_salary=int(input("enter the basic monthly salary:"))
    if not(basic_salary>0) or not(basic_salary<10000000):
         print("Error: Basic salary must be a positive number and not exceed ₹1,00,00,000.")
    else:
        break

    special_allowance=int(input("enter monthly special allowance:"))
    if not(special_allowance>0) or not(special_allowance<10000000):
         print("Error: special allowance must be a positive number and not exceed ₹1,00,00,000.")
    else:
        break
    bonus_percentage=int(input("enter bonus percentage(annual):"))
    if not (0<=bonus_percentage<=100):
         print("Error: Bonus percentage must be between 0 and 100.")
    else:
        break

    gross_monthly_salary=basic_salary+special_allowance
    if not(gross_monthly_salary>0):
        print("Gross Monthly Salary must be greater than zero.")
    else:
        break
annual_gross_salary=(gross_monthly_salary*12)+(gross_monthly_salary*bonus_percentage/100)
print("employee details:")
print("employee name:",employee_name)
print("employee id:",employee_id)
print("gross monthly salary:",gross_monthly_salary)
print("annual gross salary:",annual_gross_salary)

standard_deduction=50000
taxable_income=annual_gross_salary-standard_deduction
print("standard deduction:",standard_deduction)
print("taxable income:",taxable_income)

taxable_income=int(input("enter taxable income:"))
temp=taxable_income
tax=0

if taxable_income>1500000:
    tax+=(taxable_income-1500000)*0.3
    taxable_income=1500000
if taxable_income>1200000:
    tax+=(taxable_income-1200000)*0.2
    taxable_income=1200000
if taxable_income>900000:
    tax+=(taxable_income-900000)*0.15
    taxable_income=900000
if taxable_income>600000:
    tax+=(taxable_income-600000)*0.1
    taxable_income=600000
if taxable_income>300000:
    tax+=(taxable_income-300000)*0.05
if temp<=700000:
    tax=0
cess=tax*0.04
total_tax=cess+tax
print("total taz=",total_tax)
annual_net_salary=annual_gross_salary-total_tax
print("annual net salary:",annual_net_salary)
print("total tax=",total_tax)
print("annual gross salary=",annual_gross_salary)

print("\n---employee tax report---\n")
print(f"{'field':<25}{'details':<20}")
print('-'*45)
print(f"{'name':<25}{employee_name:<20}")
print(f"{'empid':<25}{employee_id:<20}")
print(f"{'gross monthly salary':<25}{gross_monthly_salary:<20}")
print(f"{'annual gross salary':<25}{'annual_gross_salary':<20}")
print(f"{'taxable income':<25}{taxable_income:<20}")
print(f"{'tax payable':<25}{tax:<20}")
print(f"{'annual net salary':<25}{annual_net_salary:<20}")'''







