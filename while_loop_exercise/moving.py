width = int(input())
length = int(input())
height = int(input())
total_volume = width * length * height
there_is_more_space = True
action = input()
while action != "Done":
    current_boxes = int(action)
    total_volume -= current_boxes
    if total_volume < 0:
        break
    action = input()
if total_volume >= 0:
    print(f"{total_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")