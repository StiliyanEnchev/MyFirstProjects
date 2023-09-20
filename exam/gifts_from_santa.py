address_numbers_N = int(input())
address_numbers_M = int(input())
address_num_S = int(input())

for address in reversed(range(address_numbers_N, address_numbers_M + 1)):
    if address % 2 == 0 and address % 3 == 0:
        if address == address_num_S:
            break
        else:
            print(address, end= " ")