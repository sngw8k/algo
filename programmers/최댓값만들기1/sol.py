# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 
# return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = 0
    max1 = max(numbers)
    numbers.remove(max(numbers))
    max2 = max(numbers)

    answer = max1 * max2 

    return answer

print(solution([1, 2, 3, 4, 5]))


# 모든 경우의 수
def solution(numbers):
    answer = 0

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result = numbers[i] * numbers[j]

            if answer < result:
                answer = result

    return answer

print(solution([1, 2, 3, 4, 5]))

# sort 활용
def solution(numbers):
    answer = 0

    numbers.sort()
    answer = numbers[-1] * numbers[-2]

    return answer

print(solution([1, 2, 3, 4, 5]))
