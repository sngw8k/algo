import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    
    # P : 책의 장수(마지막 페이지)
    # A : A가 찾아야 하는 목적페이지
    # B : B가 찾아야 하는 목적페이지
    P, A, B = list(map(int, input().split()))
    
    count_a = 0
    left = 1
    right = P

    while True:
        middle = int((left + right)/2)

        # 목적페이지가 가운데 보다 왼쪽에 있는 경우
        if A < middle:
            right = middle  
        elif middle < A:
            left = middle
        else:
            break

        count_a += 1

    count_b = 0
    left = 1
    right = P

    while True:
        middle = int((left + right)/2)

        # 목적페이지가 가운데 보다 왼쪽에 있는 경우
        if B < middle:
            right = middle  
        elif middle < B:
            left = middle
        else:
            break

        count_b += 1

    if count_a < count_b:
        result = 'A'
    elif count_a > count_b:
        result = 'B'
    else:
        result = 0
        
    
    print(f'#{tc} {result}')
        


    
