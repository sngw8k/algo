import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):

    N = 100
    M = 100
    total= 0
    matrix = []
    tc = int(input())

    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    max = 0

    # 가로줄 합
    for row in range(len(matrix)):
        temp = 0         
        for col in range(len(matrix[0])):
            temp += matrix[row][col]
        if temp > max:
            max = temp

    # 세로줄 합
    for col in range(len(matrix[0])):
        temp = 0         
        for row in range(len(matrix)):
            temp += matrix[row][col]
        if temp > max:
            max = temp

    # 좌상단 => 우하단 대각선
    temp = 0
    for i in range(N):
        temp += matrix[i][i]
    if max < temp:
        max = temp

    
    # 우상단 => 좌하단 대각선
    temp = 0
    for i in range(M):
        temp += matrix[i][M-1-i]
    if max < temp:
        max = temp


    print(f'#{tc} {max}')
    
    