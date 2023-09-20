student_name = input()
current_class = 0
exam_failure = 0
average_grade = 0
while True:
    grade = float(input())
    if grade >= 4.00:
        current_class += 1
        average_grade += grade
        if current_class == 12:
            average_grade = average_grade / 12
            print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
            break
    elif grade < 4.00:
        exam_failure += 1
        if exam_failure == 2:
            current_class += 1
            print(f"{student_name} has been excluded at {current_class} grade")
            break