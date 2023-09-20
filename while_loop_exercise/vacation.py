needed_money = float(input())
current_money = float(input())
spend_days_counter = 0
spend_counter = 0
while current_money < needed_money:
    action = input()
    current_sum = float(input())
    spend_days_counter += 1
    if action == 'spend':
        spend_counter += 1
        current_money -= current_sum
        if spend_counter == 5:
            print(f"You can't save the money.\n{spend_days_counter}")
            break
        elif current_money <= 0:
            current_money = 0
    elif action == 'save':
        current_money += current_sum
        spend_counter = 0
        if current_money >= needed_money:
            print(f"You saved the money for {spend_days_counter} days.")
            break