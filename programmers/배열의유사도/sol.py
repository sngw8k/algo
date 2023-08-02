# 두 배열이 얼마나 유사한지 확인해보려고 합니다. 
# 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 
# return하도록 solution 함수를 완성해주세요.

def solution(s1, s2):
    answer = 0
    set_s1 = set(s1)
    set_s2 = set(s2)

    answer = len(set_s1) + len(set_s2) - len(set_s1 | set_s2)

    return answer

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))