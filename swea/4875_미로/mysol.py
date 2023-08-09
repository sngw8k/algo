import sys
from pathlib import Path

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

    
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i,j)
            elif maze[i][j] == 3:
                end = (i,j)

    # dfs를 동작하기 위한 스택
    stack = []
    # check_list = [ [0] * (N) for _ in range(N) ]

    stack.append(start)
    # check_list[Si][Sj] = 1

    # result = 0

    # 상하좌우 델타값
    dx = [0, 0 ,-1, 1]
    dy = [-1, 1, 0 ,0]

    # 방문한 좌표
    visited = []

    result = 0

    while len(stack):

        now = stack.pop()
        x, y = now[0], now[1]

        visited.append((x,y))

        # 상하좌우를 바라보는 코드 (다음에 이동할 좌표)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 안에 있고 visited 안에 없다면
            if 0 <= nx < N and 0 <= ny < N and (nx,ny) not in visited:
                # 길이라면
                if maze[nx][ny] == 0:
                    stack.append((nx, ny))
                # 도착지점이라면
                elif maze[nx][ny] == 3:
                    result = 1
                    break
                


    print(f'#{tc} {result}')

