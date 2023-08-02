import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 배열의 항목 수
    # M : 구간의 길이
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_total = 0
    min_total = 1000000000
    result = 0
    idx = 0

    while idx < N-M+1:
        for i in range(idx, M+idx):
            result += numbers[i]

        if min > result:
            min = result
        
        if max < result:
            max = result
        
        result = 0
        idx += 1

    # for문 활용할 때

    #  for i in range(N-M+1):
    #     total = 0

    #     for j in range(M):
    #         total = total + numbers[i+j]




    # print(numbers)
    print(f'#{tc} {max - min}')






