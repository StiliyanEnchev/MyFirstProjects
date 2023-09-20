total_space = float(input())
action = input()
there_is_more_space = True
total_loaded_luggage = 0

while action != "End":
    current_volume = float(action)
    total_loaded_luggage += 1
    if total_loaded_luggage % 3 == 0:
        total_space -= (current_volume * 0.10)
    if total_space >= 0:
        total_space -= current_volume
    else:
        there_is_more_space = False
        break
    action = input()

if there_is_more_space:
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {total_loaded_luggage} suitcases loaded.")