def cgpa_calculator():
    total_score_obtainable = 0
    obtained_grade = 0

    number_of_courses = int(input("Please enter the number of courses you offered: "))
    for _ in range(number_of_courses):
        course_code = input("Enter the course code: ")
        unit = int(input("Enter the number of units for the course: "))
        score = int(input("Enter your score: "))

        total_score_obtainable += unit * 5

        if score >= 90:
            grade = 10
        elif score >= 80:
            grade = 9
        elif score >= 70:
            grade = 8
        elif score >= 60:
            grade = 7
        elif score >= 50:
            grade = 1
        else:
            grade = 0

        obtained_grade += unit * grade

    cgpa = (obtained_grade / total_score_obtainable) * 5
    print(f"Your CGPA is: {cgpa:.2f}")

cgpa_calculator()
