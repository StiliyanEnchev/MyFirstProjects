city = input()
sells = float(input())
comission = 0
if 0 <= sells <= 500:
    if city == 'Sofia':
        comission = sells * 0.05
    elif city == 'Varna':
        comission = sells * 0.045
    elif city == 'Plovdiv':
        comission = sells * 0.055
elif 500 <= sells <= 1000:
    if city == 'Sofia':
        comission = sells * 0.07
    elif city == 'Varna':
        comission = sells * 0.075
    elif city == 'Plovdiv':
        comission = sells * 0.08
elif 1000 <= sells <= 10000:
    if city == 'Sofia':
        comission = sells * 0.08
    elif city == 'Varna':
        comission = sells * 0.10
    elif city == 'Plovdiv':
        comission = sells * 0.12
elif sells > 10000:
    if city == 'Sofia':
        comission = sells * 0.12
    elif city == 'Varna':
        comission = sells * 0.13
    elif city == 'Plovdiv':
        comission = sells * 0.145
if comission > 0:
    print(f"{comission:.2f}")
else:
    print('error')