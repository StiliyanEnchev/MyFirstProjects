team = input()
type_souvenir = input()
number_of_souveninrs = int(input())
price = 0

if team == 'Argentina':
    if type_souvenir == 'flags':
        price = 3.25
    elif type_souvenir == 'caps':
        price = 7.20
    elif type_souvenir == 'posters':
        price = 5.10
    elif type_souvenir == 'stickers':
        price = 1.25
elif team == 'Brazil':
    if type_souvenir == 'flags':
        price = 4.20
    elif type_souvenir == 'caps':
        price = 8.50
    elif type_souvenir == 'posters':
        price = 5.35
    elif type_souvenir == 'stickers':
        price = 1.20
elif team == 'Croatia':
    if type_souvenir == 'flags':
        price = 2.75
    elif type_souvenir == 'caps':
        price = 6.90
    elif type_souvenir == 'posters':
        price = 4.95
    elif type_souvenir == 'stickers':
        price = 1.10
elif team == 'Denmark':
    if type_souvenir == 'flags':
        price = 3.10
    elif type_souvenir == 'caps':
        price = 6.50
    elif type_souvenir == 'posters':
        price = 4.80
    elif type_souvenir == 'stickers':
        price = 0.90
else:
    print("Invalid country!")

if price != 0:
    total_price = number_of_souveninrs * price
    print(f'Pepi bought {number_of_souveninrs} {type_souvenir} of {team} for {total_price:.2f} lv.')
elif price == 0:
    print("Invalid stock!")