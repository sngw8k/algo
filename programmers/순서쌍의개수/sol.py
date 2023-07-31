# 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를
# return하도록 solution 함수를 완성해주세요.

# 순서쌍 개수 구하기
def solution(n):
    answer = 0

    for i in range(1, n+1):
        if n % i == 0:
            answer += 1

    return answer

print(solution(20))

# 순서쌍 출력하기
def solution(n):
    answer = []

    for i in range(1, n+1):
        if n % i == 0:
            result = (i, int(n / i))
            answer.append(result)

    return answer

print(solution(20))
