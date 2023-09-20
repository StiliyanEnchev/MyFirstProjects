movie_budget = float(input())
statists_number = int(input())
price_of_uniform_per_one_statist = float(input())
decor_price = movie_budget * 0.10
total_price_for_uniforms = statists_number * price_of_uniform_per_one_statist
if statists_number > 150:
    total_price_for_uniforms = total_price_for_uniforms * 0.90
needed_budget = decor_price + total_price_for_uniforms
difference = abs(movie_budget - needed_budget)
if movie_budget >= needed_budget:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
