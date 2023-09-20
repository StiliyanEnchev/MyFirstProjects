total_num = int(input())
total_sum = 0
while total_sum < total_num:
    current_number = int(input())
    total_sum += current_number
    if total_sum >= total_num:
        print(total_sum)
        break