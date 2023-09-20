first_match_result = input()
second_match_result = input()
third_match_result = input()
result_of_the_team, opposite_team = (first_match_result[0]), (first_match_result[2])
result_of_the_team_2, opposite_team_2 = (second_match_result[0]), (second_match_result[2])
result_of_the_team_3, opposite_team_3 = (third_match_result[0]), (third_match_result[2])

wins = int(result_of_the_team > opposite_team) + int(result_of_the_team_2 > opposite_team_2) + int(result_of_the_team_3 > opposite_team_3)
loses = int(result_of_the_team < opposite_team) + int(result_of_the_team_2 < opposite_team_2) + int(result_of_the_team_3 < opposite_team_3)
drawn = int(result_of_the_team == opposite_team) + int(result_of_the_team_2 == opposite_team_2) + int(result_of_the_team_3 == opposite_team_3)

print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {drawn}")