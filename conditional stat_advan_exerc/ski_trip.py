days_total_stay = int(input())
type_of_room = input()
feedback = input()
total_nights = days_total_stay - 1
room_price_per_night = 18
apartment_price_per_night = 25
president_apt_price_per_night = 35
total_price_for_all_nights = 0
if type_of_room == "apartment":
    total_price_for_all_nights = total_nights * apartment_price_per_night
    if days_total_stay < 10:
        total_price_for_all_nights *= 0.70
    elif days_total_stay < 15:
        total_price_for_all_nights *= 0.65
    else:
        total_price_for_all_nights *= 0.50
elif type_of_room == "president apartment":
    total_price_for_all_nights = total_nights * president_apt_price_per_night
    if days_total_stay < 10:
        total_price_for_all_nights *= 0.90
    elif days_total_stay < 15:
        total_price_for_all_nights *= 0.85
    else:
        total_price_for_all_nights *= 0.80
else:
    total_price_for_all_nights = total_nights * room_price_per_night
if feedback == 'positive':
    total_price_for_all_nights *= 1.25
elif feedback == 'negative':
    total_price_for_all_nights *= 0.90
print(f'{total_price_for_all_nights:.2f}')