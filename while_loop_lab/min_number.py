min_num = 2147483648
command = input()
while command != 'Stop':
    command = int(command)
    if min_num >= command:
        min_num = command
    command = input()
if command == 'Stop':
    print(min_num)