name            = input('Enter employee name: ')
employee_id     = int(input('Enter employee Id: '))
basic_salary    = float(input('Enter employee salary: '))
allowances      = float(input('Enter employee allowances: '))
bonus_percentage= float(input('Enter employee bonus_percentage: '))
monthly_gross_salary = basic_salary + allowances
annual_gross_salary  = monthly_gross_salary * 12 + (bonus_percentage / 100 * (monthly_gross_salary * 12) )
standard_deduction=50000
taxable_income=annual_gross_salary-standard_deduction


print('Employee details are:')
print('-' * 50)
print('Name = ', name)
print('Id = ', employee_id)
print('Basic Salary = ', basic_salary)
print('Allowances = ', allowances)
print('Bonues percentage = ', bonus_percentage)
print('Monthly Gross Salary = ', monthly_gross_salary)
print('Annual Gross Salary = ', annual_gross_salary)
print('-' * 50)

print('Employee details are:')
print('-' * 50)
print(f'%-20s = {name}'%('Name'))
print(f'%-20s = {employee_id}'%('Id'))
print(f'%-20s = {basic_salary}'%('Basic Salary'))
print(f'%-20s = {allowances}'%('Allowances'))
print(f'%-20s = {bonus_percentage}'%('Bonus percentage'))
print(f'%-20s = {monthly_gross_salary}'%('Monthly Gross Salary'))
print(f'%-20s = {annual_gross_salary}'%('Annual Gross Salary'))
print(f'%-20s = {standard_deduction}'%('standard_deduction'))

print(f'%-20s = {taxable_income}'%('taxable_incomevar
                                   '))
