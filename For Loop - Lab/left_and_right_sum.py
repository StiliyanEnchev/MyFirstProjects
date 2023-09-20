numbers_to_sum = int(input())
sum1 = 0
sum2 = 0

for i in range(numbers_to_sum):
    sum1 += int(input())

for i in range(numbers_to_sum):
    sum2 += int(input())

if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
if sum1 != sum2:
    print(f'No, diff = {abs(sum1 - sum2)}')