tournament_days = int(input())
games_won = 0
games_lost = 0
total_savings = 0

for current_day in range(tournament_days):
    current_number_of_wins = 0
    current_number_of_loses = 0
    current_money = 0
    while True:
        sport = input()

        if sport == 'Finish':
            break

        result = input()
        if result == 'win':
            games_won += 1
            current_money += 20
            current_number_of_wins += 1
        elif result == 'lost':
            games_lost += 1
            current_number_of_loses += 1

        if current_number_of_wins > current_number_of_loses:
            total_savings += current_money + (current_money * 0.10)
        else:
            total_savings += current_money
        games_lost += current_number_of_loses
if games_won > games_lost:
    total_savings += total_savings * 0.20
    print(f"You won the tournament! Total raised money: {total_savings:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_savings:.2f}")