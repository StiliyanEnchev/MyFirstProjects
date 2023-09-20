chicken_menu_orders = int(input())
fish_menu_orders = int(input())
vegan_menu_orders = int(input())
chicken_menu_price = 10.35 * chicken_menu_orders
fish_menu_price = 12.40 * fish_menu_orders
vegan_menu_price = 8.15 * vegan_menu_orders
delivery_price = 2.50  # at the end, after the dessert
total_without_dessert = chicken_menu_price + fish_menu_price + vegan_menu_price
desert_price = total_without_dessert * 0.20
total_price_with_delivery = total_without_dessert + desert_price + delivery_price
print(total_price_with_delivery)