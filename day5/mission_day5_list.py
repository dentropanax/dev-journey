fruits = ["사과", "바나나", "포도"]
fruits.append("수박")
fruits.remove("바나나")
fruits.insert(0,"딸기")
fruits.sort()
last = fruits.pop()
print("꺼낸 과일:", last)
print("남은 리스트:", fruits)
