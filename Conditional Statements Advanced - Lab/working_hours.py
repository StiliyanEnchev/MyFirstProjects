hour = int(input())
week_day = input()
if hour >= 10 and hour <= 18:
    if week_day != 'Sunday':
        print('open')
    else:
        print('closed')
else:
        print('closed')