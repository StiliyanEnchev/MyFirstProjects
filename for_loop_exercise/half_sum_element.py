import sys

count_of_numbers = int(input())
sum_of_all_elements = 0
max_elements = -sys.maxsize

for number in range(count_of_numbers):
    current_element = int(input())
    sum_of_all_elements += current_element
    if max_elements < current_element:
        max_elements = current_element
if max_elements == sum_of_all_elements - max_elements:
    print("Yes")
    print(f"Sum = {max_elements}")
else:
    diff = abs((max_elements - (sum_of_all_elements - max_elements)))
    print("No")
    print(f'Diff = {diff}')