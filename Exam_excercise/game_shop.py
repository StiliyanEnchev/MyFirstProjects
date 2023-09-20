number_of_games = int(input())

hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0

for _ in range(number_of_games):
    game_name = input()

    if game_name == 'Hearthstone':
        hearthstone_counter += 1
    elif game_name == 'Fornite':
        fornite_counter += 1
    elif game_name == 'Overwatch':
        overwatch_counter += 1
    else:
        others_counter += 1

hearthstone_percantage = (hearthstone_counter / number_of_games) * 100
fornite_percantage = (fornite_counter / number_of_games) * 100
overwatch_percantage = (overwatch_counter / number_of_games) * 100
others_percantage = (others_counter / number_of_games) * 100

print(f'Hearthstone - {hearthstone_percantage:.2f}%')
print(f'Fornite - {fornite_percantage:.2f}%')
print(f'Overwatch - {overwatch_percantage:.2f}%')
print(f'Others - {others_percantage:.2f}%')