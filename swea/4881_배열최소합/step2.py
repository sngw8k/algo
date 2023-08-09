import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def search(idx, visited):
    
    if idx == N:
        return
    
    # 모든 경우의 수를 탐색하는 경우
    for i in range(N):
        if visited[i] == False:
            result.append(numbers[idx][i])
            visited[i] = True
            search(idx+1, visited)
            result.pop()
            visited[i] = False

for tc in range(1, T+1):
    N = int(input())

    matrix = []
    for _ in range(N):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)

    result = []
    visited = [False] * N

    search(0, visited)


    