import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # N : 미로의 길이
    N = int(input())

    maze = []

    for _ in range(N):
        numbers = list(map(int, input()))
        maze.append(numbers)

    # 시작점
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i,j)
                # 시작점을 -1로 수정
                maze[i][j] = -1

    # bfs를 동작하기 위한 큐
    queue = []
    queue.append(start)

    # 상하좌우 델타값
    dx = [0, 0 ,-1, 1]
    dy = [-1, 1, 0 ,0]

    result = 0

    while len(queue):
        now = queue.pop(0)
        x, y = now[0], now[1]

        # 상하좌우를 바라보는 코드
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                # 길 == 0
                if maze[nx][ny] == 0:
                    queue.append((nx, ny))
                    maze[nx][ny] = maze[x][y] - 1
                # 도착지 == 3
                elif maze[nx][ny] == 3:
                    # 거리 계산 결과를 저장
                    result = abs(maze[x][y]) - 1
    
    print(result)