import math

total_tournaments = int(input())
points = int(input())
w_wins = 0
f_wins = 0
sf_wins = 0
total_points = points
for num in range(total_tournaments):
    type_of_win = input()
    if type_of_win == "W":
        w_wins += 1
        total_points += 2000
    elif type_of_win == "F":
        f_wins += 1
        total_points += 1200
    elif type_of_win == "SF":
        sf_wins += 1
        total_points += 720
average_points = (total_points - points) / total_tournaments
percentage_of_wins = w_wins / total_tournaments * 100
print(f"Final points: {total_points}")
print(f"Average points: {math. floor(average_points)}")
print(f"{percentage_of_wins:.2f}%")