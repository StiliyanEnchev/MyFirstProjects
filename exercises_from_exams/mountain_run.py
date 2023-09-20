import math

current_record = float(input())
meters_long = float(input())
time_for_one_meter = float(input())

total_distance_in_seconds = meters_long * time_for_one_meter
delay = math.floor(meters_long / 50) * 30
final_time = total_distance_in_seconds + delay
diff = abs(final_time - current_record)
if final_time < current_record:
    print(f" Yes! The new record is {final_time:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower.")