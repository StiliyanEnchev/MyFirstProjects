destination = input()
min_budget = float(input())
total_savings = 0
while destination != 'End':
    total_savings += float(input())
    if total_savings >= min_budget:
        print(f'Going to {destination}!')
        total_savings = 0
        destination = input()
        if destination == 'End':
            break
        min_budget = float(input())