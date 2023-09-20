number_page = int(input())
pages_per_hour = int(input())
number_of_days = int(input())
needed_hours_per_whole_book = number_page / pages_per_hour
needed_hours_per_days = needed_hours_per_whole_book / number_of_days
print(int(needed_hours_per_days))