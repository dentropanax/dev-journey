def filter_pass(scores):
    passed = []
    for score in scores:
        if score >= 60:
            passed.append(score)
    return passed
scores = [45, 89, 72, 53, 94, 38, 66]
print(filter_pass(scores))
