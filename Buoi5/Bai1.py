student_gpa = {
    "001": 3.7,
    "002": 2.5,
    "003": 3.4,
    "004": 0.7,
    "005": 3.1,
    "006": 0.1
}

student_gpa["007"] = 1.5

count = 0

low_gpa_students = []

for student_id, gpa in student_gpa.items():
    if 3.0 <= gpa <= 3.5:
        count += 1
    if gpa < 2.0:
        low_gpa_students.append(student_id)

print("Số sinh viên có điểm tổng kết trong [3.0, 3.5]:", count)

for student_id in low_gpa_students:
    student_gpa.pop(student_id)

print(student_gpa)
