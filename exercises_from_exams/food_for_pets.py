days = int(input())
food_stack = int(input())
dog_total = 0
cat_total = 0
eaten_food = 0
bisquits = 0
for day in range(1, days + 1):
    dog_portion = int(input())
    dog_total += dog_portion
    cat_portion = int(input())
    cat_total += cat_portion
    eaten_food += dog_portion + cat_portion
    if day % 3 == 0:
        bisquits += (dog_portion + cat_portion) * 0.10
percentage_eaten_food = (eaten_food / food_stack) * 100
percent_dog = (dog_total / eaten_food) * 100
percentage_cat = (cat_total / eaten_food) * 100
print(f"Total eaten biscuits: {round(bisquits)}gr.")
print(f"{percentage_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percentage_cat:.2f}% eaten from the cat.")