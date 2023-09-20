budget = float(input())
season = input()
destination = ''
spend_sum = 0
type_of_vacation = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        spend_sum = budget * 0.30
    elif season == 'winter':
        spend_sum = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        spend_sum = budget * 0.40
    elif season == 'winter':
        spend_sum = budget * 0.80
elif budget > 1000:
    destination = 'Europe'
    spend_sum = budget * 0.90
    type_of_vacation = 'Hotel'
if season == 'summer' and destination != 'Europe':
    type_of_vacation = 'Camp'
elif season == 'winter'and destination != 'Europe':
    type_of_vacation = 'Hotel'
print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {spend_sum:.2f}")