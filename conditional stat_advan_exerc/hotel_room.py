month = input()
num_of_nights = int(input())
studio_price_per_night = 0
apartment_price_per_night = 0
if month == 'May' or month == "October":
    studio_price_per_night = 50
    apartment_price_per_night = 65
elif month == 'June' or month == "September":
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70
elif month == 'July' or month == "August":
    studio_price_per_night = 76
    apartment_price_per_night = 77
total_price_for_studio = studio_price_per_night * num_of_nights
total_price_for_apartment = apartment_price_per_night * num_of_nights
if month == 'May' or month == "October":
    if 14 > num_of_nights > 7:
        total_price_for_studio *= 0.95
    elif num_of_nights > 14:
        total_price_for_studio *= 0.70
if month == 'June' or month == "September":
    if num_of_nights > 14:
        total_price_for_studio *= 0.80
if num_of_nights > 14:
    total_price_for_apartment *= 0.90
print(f"Apartment: {total_price_for_apartment:.2f} lv.")
print(f"Studio: {total_price_for_studio:.2f} lv.")