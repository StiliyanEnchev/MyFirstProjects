number_of_easter_bread = int(input())
number_of_cores_of_eggs = int(input())
kilograms_of_cookies = int(input())
total_eggs = number_of_cores_of_eggs * 12

total_bread_price = number_of_easter_bread * 3.20
total_for_eggs = number_of_cores_of_eggs * 4.35
total_for_cookies = kilograms_of_cookies * 5.40
total_price_for_paint_for_eggs = total_eggs * 0.15

total_charge = total_bread_price + total_price_for_paint_for_eggs + total_for_eggs + \
               total_for_cookies
print(f"{total_charge:.2f}")
