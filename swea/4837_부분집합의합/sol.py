import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    numbers = list(range(1, 13))

    count = 0
    for i in range(1 << len(numbers)):

        temp = []
        for j in range(len(numbers)):
            if i & (1 << j):
                temp.append(numbers[j])
        
        if len(temp) == N and sum(temp) == K:
            count += 1
    
    print(f'#{tc} {count}')

