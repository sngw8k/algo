import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # N : 노드의 수
    # M : 리프 노드의 수
    # L : 출력할 노드 번호

    N, M, L = list(map(int, input().split()))

    idx = []
    value = []
    tree = [0] * (N+1)

    for _ in range(M):
        node = list(map(int, input().split()))
        idx.append(node[0])
        value.append(node[1])

    
    count = 0
    for i in idx:
        tree[i] = value[count]
        count += 1
    
    while N != 0:
        start = N
        if start // 2 == 0:
            pass
        else:
            tree[start//2] += tree[start]
        
        N -= 1

    result = tree[L]

    # print(tree)
    # print(result)
    print(f'#{tc} {result}')
