n = int(input("입력할 학생 수를 입력하세요: "))

students = []

for i in range(n):
    name = input(f"{i+1}번째 학생 이름: ")
    age = int(input(f"{i+1}번째 학생 나이: "))
    score = int(input(f"{i+1}번째 학생 성적: "))

    student = {
        "이름": name,
        "나이": age,
        "성적": score
    }

    students.append(student)

    print("--- 전체 명단 ---")
    for student in students:
        print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")
