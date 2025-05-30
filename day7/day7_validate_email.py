def validate_email(email):
    if "@" in email:
        return("올바른 이메일입니다")
    else :
        return("잘못된 이메일입니다")

email = input("이메일을 입력하세요: ")
print(validate_email(email))

