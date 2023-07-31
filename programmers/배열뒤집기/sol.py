# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다.
# num_list의 원소의 순서를 거꾸로 뒤집은 배열을 
# return하도록 solution 함수를 완성해주세요.


# reverse 함수 활용
def solution(num_list):
    answer = []
    
    num_list.reverse()
    answer = num_list
        
    return answer

print(solution([1, 2, 3, 4, 5]))


# insert 함수 활용
def solution(num_list):
    answer = []

    for num in num_list:
        answer.insert(0, num)

    return answer

print(solution([1, 2, 3, 4, 5]))

# [::-1] 활용
def solution(num_list):
    answer = num_list[::-1]
    return answer

print(solution([1, 2, 3, 4, 5]))


# index 뒤에서 접근
def solution(num_list):
    answer = []
    for i in range(len(num_list)):
        data = num_list[len(num_list) - i - 1]
        answer.append(data) 

    return answer

print(solution([1, 2, 3, 4, 5]))