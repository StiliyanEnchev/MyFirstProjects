day_of_the_week = input()
if day_of_the_week == 'Monday' or day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday' or day_of_the_week == 'Friday' or day_of_the_week == 'Thursday':
    print('Working day')
elif day_of_the_week == 'Sunday' or day_of_the_week == 'Saturday':
    print('Weekend')
else:
    print('Error')