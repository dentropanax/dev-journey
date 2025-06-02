grades ={
    "철수": 87,
    "영희": 92,
    "민수": 76
}

name = input("학생 이름을 입력하세요: ")
if name in grades:
    print(f"{name}의 점수는 {grades[name]}점입니다.")
else:
    print("학생을 찾을 수 없습니다.")