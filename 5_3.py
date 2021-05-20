staff = dict()
min_salary = 20000
income = []
with open('employee_data.txt', 'r', encoding='utf-8') as f:
    employees = f.readlines()
    for el in employees:
        elem = el.split()
        staff[elem[0]] = float(elem[1])
print(f'Сотрудники, которые имеют оклад меньше {min_salary}:')
for name, salary in staff.items():
    if salary < min_salary:
        print(f'{name} - {salary}')
    income.append(salary)

print(f'Средний доход {len(income)} сотрудников: {sum(income)/len(income)}')
