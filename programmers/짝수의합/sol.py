def solution(n):
    answer = 0
    while n > 0:
        if n % 2 == 0:
            answer += n 
            n -= 2
        else:
            answer += (n - 1)
            n -= 2
            
    return answer

print(solution(10))
print(solution(5))