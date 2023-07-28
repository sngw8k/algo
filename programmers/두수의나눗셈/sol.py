def solution(num1, num2):
    answer = (num1 / num2) * 1000
    answer = int(answer)
    return answer

print(solution(3, 2))
print(solution(7, 3))