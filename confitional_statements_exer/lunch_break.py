from math import ceil

name_of_the_show = input()
lenght_of_episode = int(input())
lenght_of_the_break = int(input())
lunch_time = lenght_of_the_break / 8
rest_time = lenght_of_the_break / 4
time_left = lenght_of_the_break - lunch_time - rest_time
if time_left >= lenght_of_episode:
    print(f"You have enough time to watch {name_of_the_show} and left with {ceil(time_left - lenght_of_episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_the_show}, you need {ceil(lenght_of_episode - time_left)} more minutes.")