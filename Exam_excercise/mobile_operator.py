contract_time = input()
type_of_contract = input()
mobile_internet = input()
number_of_months = int(input())
base_fee = 0
if contract_time == "one":
    if type_of_contract == "Small":
        base_fee = 9.98
    elif type_of_contract == "Middle":
        base_fee = 18.99
    elif type_of_contract == "Large":
        base_fee = 25.98
    elif type_of_contract == "ExtraLarge":
        base_fee = 35.99
elif contract_time == "two":
    if type_of_contract == "Small":
        base_fee = 8.58
    elif type_of_contract == "Middle":
        base_fee = 17.09
    elif type_of_contract == "Large":
        base_fee = 23.59
    elif type_of_contract == "ExtraLarge":
        base_fee = 31.79
if mobile_internet == "yes":
    if base_fee <= 10:
        base_fee += 5.50
    elif base_fee <= 30:
        base_fee += 4.35
    else:
        base_fee += 3.85
if contract_time == 'two':
    base_fee -= base_fee * 0.0375
total_fee = number_of_months * base_fee
print(f"{total_fee:.2f} lv.")