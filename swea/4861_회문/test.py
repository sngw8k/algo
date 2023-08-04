import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    
    # N : 글자판 길이
    # M : 찾아야 하는 회문의 길이
    N, M = list(map(int, input().split()))

    matrix = []
    for _ in range(N):
        words = list(map(str, input().split()))
        matrix.append(words)
        
    count = 0
    result = []

    
    # 가로로 인덱스 증가하면서 찾기
    for row in range(N):
        # 가로줄에서 옆으로 이동하면서 찾기
        for i in range(N-M+1):
            # 회문인지 찾기
            for j in range(M//2):
                if matrix[row][0][i+j] == matrix[row][0][i+M-1-j]:
                    count += 1
                else:
                    count = 0

                if count == M//2:
                    for k in range(M):
                        result += matrix[row][0][i+k]
                    break
                


    for col in range(N):
        for i in range(N-M+1):
            for j in range(M//2):
                if matrix[i+j][0][col] == matrix[i+M-1-j][0][col]:
                    count += 1
                else:
                    count = 0

                if count == M//2:
                    for k in range(M):
                        result += matrix[i+k][0][col]
                    break
    
    output = ''.join(result)
    ##pprint(matrix)
    print(output)