# 인접 리스트  방식
import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # V : 노드 수 / E : 간선 수
    V, E = list(map(int, input().split()))

    nodes = [ [] * (V+1) for _ in range(V+1) ]

    # 인접 리스트 방식으로 그래프를 저장
    # 간선의 갯수만큼 반복을 진행
    for line in range(E):
        start, end = list(map(int, input().split()))
        nodes[start].append(end) 
    # pprint(nodes)

    # S : 출발노드 / G : 도착노드
    S, G = list(map(int, input().split()))

    # 방문 체크용 리스트
    check_list = [False] * (V+1)

    stack = []

    now = S
    check_list[now] = True
    stack.append(now)

    result = 0

    while len(stack):
        now = stack.pop()
        check_list[now] = True

        # 인접리스트를 기준으로 now와 연결된 link 노드들을 반복
        for link in nodes[now]:
            # 방문하지 않았다면
            if not check_list[link]:
                if link == G:
                    result = 1
                    
                stack.append(link)
    
    print(f'#{tc} {result}')
                    
                    
