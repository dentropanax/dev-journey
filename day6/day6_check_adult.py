def check_adult(age):
    if age >= 20:
        return("성인입니다")
    else:
        return("미성년자입니다")
    
age = int(input("나이를 입력하세요: "))
print(check_adult(age))
