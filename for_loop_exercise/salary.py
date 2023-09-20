open_tabs_number = int(input())
salary = int(input())
for char in range(0, open_tabs_number):
    tab_name = input()
    if tab_name == "Facebook":
        salary -= 150
    elif tab_name == 'Instagram':
        salary -= 100
    elif tab_name == 'Reddit':
        salary -= 50
if salary > 0:
    print(salary)
elif salary <= 0:
    print("You have lost your salary.")