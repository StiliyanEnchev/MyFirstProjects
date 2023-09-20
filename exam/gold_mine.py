num_of_locations = int(input())

for location in range(num_of_locations):
    total_gold_per_location = 0
    expected_average_gold_income_per_day = float(input())
    number_of_days_for_digging = int(input())

    for day in range(number_of_days_for_digging):
        digged_gold = float(input())
        total_gold_per_location += digged_gold

    average_gold_per_day = total_gold_per_location/number_of_days_for_digging
    needed_gold = expected_average_gold_income_per_day - average_gold_per_day

    if expected_average_gold_income_per_day <= average_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
    else:
        print(f"You need {needed_gold:.2f} gold.")
