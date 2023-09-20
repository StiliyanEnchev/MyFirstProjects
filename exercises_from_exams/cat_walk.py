minutes_of_walk = int(input())
number_of_walks = int(input())
calories = int(input())
total_minutes = minutes_of_walk * number_of_walks
total_used_calories = total_minutes * 5
needed_calories_to_burn = calories / 2
if total_used_calories >= needed_calories_to_burn:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_used_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_used_calories}.")