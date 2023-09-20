max_number_of_low_degrees = int(input())
average_degree = 0
total_degrees = 0
total_low_degrees = 0
is_failed = False
current_exam = input()
last_exam_name = ""
while current_exam != "Enough":
    degree = int(input())
    if degree <= 4:
        total_low_degrees += 1
        if total_low_degrees == max_number_of_low_degrees:
            is_failed = True
            break
    average_degree += degree
    total_degrees += 1
    last_exam_name = current_exam
    current_exam = input()
if is_failed:
    print(f"You need a break, {max_number_of_low_degrees} poor grades.")
else:
    average_degree /= total_degrees
    print(f"Average score: {average_degree:.2f}\nNumber of problems: {total_degrees}\nLast problem: {last_exam_name}")