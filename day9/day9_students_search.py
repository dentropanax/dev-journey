students = [
    {"이름": "철수", "나이": 17, "성적": 85},
    {"이름": "영희", "나이": 18, "성적": 92},
    {"이름": "민수", "나이": 16, "성적": 78}
]

target = input("이름을 입력하세요: ")
found = False

for student in students:
    if student["이름"] == target:
           print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")
           found = True
           break
    
if not found:
        print("학생을 찾을 수 없습니다.")