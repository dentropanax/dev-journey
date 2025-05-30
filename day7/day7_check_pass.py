def check_pass(scores):
    avg = sum(scores) / len(scores)
    if avg >= 70:
        return "합격"
    else: 
        return "불합격"

scores = [70, 80, 90]
print(check_pass(scores))
