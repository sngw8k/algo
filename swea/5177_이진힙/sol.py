import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    
    # N : 자연수 개수
    N = int(input())

    numbers = list(map(int, input().split()))

    # 힙큐 라이브러리 사용할 때
    # import heapq
    # heapq.heapify(numbers)
    # print(numbers)

    heap = [0] * (N+1)
    heap_size = 0

    for i in range(N):
        heap_size += 1
        # 맨 마지막 노드에 삽입하려는 데이터를 할당
        heap[heap_size] = numbers[i]

        child_idx = heap_size
        parent_idx = child_idx // 2

        # 힙에 조건에 맞도록 교환 반복
        while parent_idx and heap[parent_idx] > heap[child_idx]:
            # 부모 자식 값 교환
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]

            # 다음 조상 노드 확인
            child_idx = parent_idx
            parent_idx = child_idx // 2

    print(heap)

    node = N // 2
    total = 0

    # 조상 노드가 1보다 작을 때까지
    while node:
        total += heap[node]
        node //= 2

    print(total)