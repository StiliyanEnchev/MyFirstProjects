fruit = input()
set_size = input()
quantity = int(input())
total_price = 0
if fruit == 'Watermelon':
    if set_size == 'small':
        total_price = quantity * 2 * 56
    elif set_size == 'big':
        total_price = quantity * 5 * 28.70
elif fruit == 'Mango':
    if set_size == 'small':
        total_price = quantity * 2 * 36.66
    elif set_size == 'big':
        total_price = quantity * 5 * 19.60
elif fruit == 'Pineapple':
    if set_size == 'small':
        total_price = quantity * 2 * 42.10
    elif set_size == 'big':
        total_price = quantity * 5 * 24.80
elif fruit == 'Raspberry':
    if set_size == 'small':
        total_price = quantity * 2 * 20
    elif set_size == 'big':
        total_price = quantity * 5 * 15.20
if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50
print(f"{total_price:.2f} lv.")