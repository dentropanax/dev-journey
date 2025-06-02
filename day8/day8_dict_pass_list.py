grades = {
    "철수": 87,
    "영희": 58,
    "민수": 76,
    "지우": 45,
    "수빈": 92
}

for name in grades:
    if grades[name] >= 60:
        print(f"{name}: {grades[name]}점")
