def grade_result(score):
    if score >= 90:
        return("A등급")
    elif score >= 80:
        return("B등급") 
    elif score >= 70:
        return("C등급")
    elif score >= 60:
        return("D등급")
    else :
        return("불합격")

score = int(input("점수를 입력하세요: "))
print(grade_result(score))
