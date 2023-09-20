volume_of_pool_in_liters = int(input())
debit_of_pipe_1_on_hour = int(input())
debit_of_pipe_2_on_hour = int(input())
hours_that_will_be_on = float(input())
total_water_from_pipe_1 = debit_of_pipe_1_on_hour * hours_that_will_be_on
total_water_from_pipe_2 = debit_of_pipe_2_on_hour * hours_that_will_be_on
total_water = (total_water_from_pipe_2 + total_water_from_pipe_1) * hours_that_will_be_on
if volume_of_pool_in_liters <= total_water:
    print(f"The pool is {запълненост на басейна в проценти}% full. Pipe 1: {процент вода от първата тръба}%. Pipe 2: {процент вода от втората тръба}%.")
