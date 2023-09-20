num_of_floors = int(input())
num_of_rooms = int(input())
for floor in reversed(range(1, num_of_floors + 1)):
    print()
    for room in range(0, num_of_rooms):
        if floor == num_of_floors:
            print(f"L{floor}{room}", end=' ')
        elif floor % 2 == 0:
            print(f"O{floor}{room}", end=' ')
        elif floor % 2 != 0:
            print(f"A{floor}{room}", end=' ')