num1 = int(input())
num2 = int(input())
magic_number = int(input())
combination_numbers = 0
number_is_found = False
first_num = 0
second_num = 0
for first_num in range(num1, num2 + 1):
    for second_num in range(num1, num2 + 1):
        result = first_num + second_num
        combination_numbers += 1
        if result == magic_number:
            number_is_found = True
            break
    if number_is_found:
        break
if number_is_found:
    print(f"Combination N:{combination_numbers} ({first_num} + {second_num} = {magic_number})")
else:
    print(f"{combination_numbers} combinations - neither equals {magic_number}")