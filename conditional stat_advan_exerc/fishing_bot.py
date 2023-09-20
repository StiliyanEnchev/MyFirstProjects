budget_of_the_group = int(input())
season = input()
people_in_the_group = int(input())
price_for_the_boat = 0
if season == "Spring":
    price_for_the_boat = 3000
elif season == "Summer" or season == 'Autumn':
    price_for_the_boat = 4200
elif season == "Winter":
    price_for_the_boat = 2600
if people_in_the_group <= 6:
    price_for_the_boat *= 0.90
elif people_in_the_group <= 11:
    price_for_the_boat *= 0.85
elif people_in_the_group > 11:
    price_for_the_boat *= 0.75
if people_in_the_group % 2 == 0 and season != 'Autumn':
    price_for_the_boat *= 0.95
difference = abs(budget_of_the_group - price_for_the_boat)
if budget_of_the_group >= price_for_the_boat:
    print(f"Yes! You have {difference:.2f} leva left.")
elif budget_of_the_group < price_for_the_boat:
    print(f"Not enough money! You need {difference:.2f} leva.")
