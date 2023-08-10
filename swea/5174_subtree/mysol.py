import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    
    # E : 간선 수 / N : 루트 노드
    E, N = list(map(int, input().split()))

    numbers = list(map(int, input().split()))

    tree = []
    for i in range(E):
        P, C = numbers[2*i], numbers[2*i + 1]
        tree.append([P,C])

    Add = []
    now = N
    Add.append(now)
    stack = []
    stack.append(now)
    result = 0

    while len(stack):
        now = stack.pop()
        for i in range(E):
            if tree[i][0] == now:
                Add.append(tree[i][1])
                stack.append(tree[i][1]) 

    result = len(Add)
    # print(tree)
    print(f'#{tc} {result}')
    # print(numbers)

    