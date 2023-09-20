actor_name = input()
points = float(input())
number_of_jury = int(input())
total_points_received = points
for current_grade in range(number_of_jury):
    name_of_the_jury = input()
    points_from_the_jury = float(input())
    total_points_received += (len(name_of_the_jury)) * points_from_the_jury / 2
    if total_points_received > 1250.5:
        break
if total_points_received > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points_received:.1f}!")
else:
    difference = 1250.5 - total_points_received
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")