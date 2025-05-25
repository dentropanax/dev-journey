fruits = ["사과", "바나나", "포도", "딸기", "수박"]
for i in range(5):
    fruit = input("과일을 입력하세요:  ")
    if fruit in fruits:
        print(f"{fruit}는 목록에 있습니다")
    else:
        print(f"{fruit}는 목록에 없습니다")
