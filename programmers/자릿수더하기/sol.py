# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을
# return하도록 solution 함수를 완성해주세요


def solution(n):
    answer = 0
    while n >= 1:
        if n < 10:
            answer += n
            n = n / 10
        else:
            answer += (n % 10)
            n = n // 10
            
    return answer

print(solution(930211))

# str 활용

def solution(n):
    answer = 0

    for i in str(n):
        answer += int(i)

    return answer

print(solution(1234))



