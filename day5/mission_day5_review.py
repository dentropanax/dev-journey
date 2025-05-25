scores = [95, 67, 88, 42, 76]
for score in scores:
    if score >= 80:
          result = "우수"
    elif score >= 60:
          result = "보통"
    else:
          result = "재시험"
    print(f"{score}점: {result}")
    
