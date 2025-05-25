people = [
    {"이름": "민수", "나이": 12},
    {"이름": "영희", "나이": 17},
    {"이름": "철수", "나이": 25},
    {"이름": "지은", "나이": 8}
]
for person in people:
    name = person["이름"]
    age = person["나이"]
    if age >= 20:
          print(f"{name}는 성인입니다.")
    elif age >= 14:
          print( f"{name}은 청소년입니다.")
    else:
          print( f"{name}은 어린이입니다.")



