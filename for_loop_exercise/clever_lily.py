years_old = int(input())
price_for_washing_machine = float(input())
price_per_toy = int(input())
total_toys = 0
total_money = 10
saved_money = 0
for num in range(1, years_old + 1):
    if num % 2 == 0:
        saved_money += total_money
        total_money += 10
    else:
        total_toys += 1
for num in range(1, years_old + 1):
    if num % 2 == 0:
        saved_money -= 1
money_from_toys = total_toys * price_per_toy
all_money = money_from_toys + saved_money
diff = abs(all_money - price_for_washing_machine)
if all_money >= price_for_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")