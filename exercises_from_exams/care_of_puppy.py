food_stack = int(input()) * 1000
action = input()
while action != 'Adopted':
    current_food = int(action)
    food_stack -= current_food
    action = input()
if food_stack < 0:
    print(f"Food is not enough. You need {abs(food_stack)} grams more.")
else:
    print(f"Food is enough! Leftovers: {food_stack} grams.")