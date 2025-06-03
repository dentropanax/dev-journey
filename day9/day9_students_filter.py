students = [
    {"이름": "철수", "나이": 17, "성적": 85},
    {"이름": "영희", "나이": 18, "성적": 92},
    {"이름": "민수", "나이": 16, "성적": 78}
]

for student in students:
    if student["성적"] >= 80:
          print(f"이름: {student["이름"]}, 성적: {student["성적"]}")
