grade_points = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}
sum_credit = 0
sum_grade = 0

while True:
    try:
        name, credit, grade = map(str, input().split())
        credit = float(credit)
        if grade in grade_points:
            sum_grade = sum_grade+ credit*grade_points[grade]
            sum_credit = sum_credit + credit
        else:
            pass
    except:
        break
    
print(sum_grade/sum_credit)