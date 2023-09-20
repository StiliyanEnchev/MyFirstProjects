number = int(input())
total_results = 0
for num1 in range(0, number + 1):
    for num2 in range(0, number + 1):
        for num3 in range(0, number + 1):
            result = num1 + num2 + num3
            if result == number:
                total_results += 1
print(total_results)
