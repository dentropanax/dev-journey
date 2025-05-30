def filter_even(numbers):
    passed = []
    for number in numbers:
          if number % 2 == 0:
              passed.append(number)
    return passed

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter_even(numbers)
print(result)
