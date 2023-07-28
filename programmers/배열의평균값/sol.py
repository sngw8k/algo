def solution(numbers):
    sum = 0
    for i in numbers:
        sum += i
    answer = sum / len(numbers)
    return answer

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(solution(l))

# total = sum(numbers)
# length = len(numbers)
# answer = total / len