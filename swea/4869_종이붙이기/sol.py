import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    
    N = int(input())

    def paper(N):
        if N == 10:
            return 1
        elif N == 20:
            return 3
        else:
            return paper(N-10)+(2*paper(N-20))
        
    result = paper(N)
        
    print(f'#{tc} {result}')

    # ----------------------------------------

    # memo = [0, 1, 3]

    # for tc in range(1, T+1):
    #     N = int(input()) // 10

    #     # memo 배열에 출력시킬 값이 없으면 추가
    #     while N >= len(memo):
    #         # n-2 배열에 가로로 작은 사각형 두개 쌓거나 큰 사각형 쌓는 방법
    #         # n-1 배열에 세로로 작은 사각형 쌓는 방법 하나
    #         temp = 2 * memo[len(memo)-2] + memo[len(memo)-1]
    #         memo.append(temp)

    #     print(memo(N))


