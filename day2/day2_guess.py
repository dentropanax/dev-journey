secret = 7
guess = int(input("1부터 10 사이 숫자를 맞춰보세요: "))
if guess == secret:
    print("정답!")
else:
    print("틀렸습니다. 정답은", secret)