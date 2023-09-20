total_steps = 0
target_steps = 10000
while total_steps <= target_steps:
    action = input()
    if action == 'Going home':
        current_steps = int(input())
        total_steps += current_steps
        break
    else:
        total_steps += int(action)
difference = abs(target_steps - total_steps)
if total_steps >= target_steps:
    print(f"Goal reached! Good job!\n{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")