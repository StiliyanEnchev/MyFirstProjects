max_num = -2147483648
command = input()
while command != 'Stop':
    command = int(command)
    if max_num <= command:
        max_num = command
    command = input()
if command == 'Stop':
    print(max_num)