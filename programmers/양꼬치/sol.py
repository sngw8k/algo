## 양꼬치 1인분에 12000원 음료수 2000원
# 양꼬치 10인분 먹으면 음료수 하나 서비스

def solution(n, k):
    sum = (12000 * n) + (2000 * k)
    if n // 10 > 0:
        sum -= 2000 * (n // 10)
    answer = sum
    return answer

print(solution(10, 3))

# answer = 0
# service = n // 10
# answer = (n * 12000) + (k - service) * 2000