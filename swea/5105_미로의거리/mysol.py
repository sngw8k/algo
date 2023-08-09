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

    
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i,j)
            elif maze[i][j] == 3:
                end = (i,j)


    # bfs를 동작하기 위한 큐
    queue = []
    # check_list = [ [0] * (N) for _ in range(N) ]

    queue.append(start)
    # check_list[Si][Sj] = 1

    # result = 0

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

            # 미로 범위 안에 있다면 진행
            if 0 <= nx < N and 0 <= ny < N:

                # 길이라면 한 칸 이동할 때 +2
                if maze[nx][ny] == 0:
                    queue.append((nx, ny))
                    maze[nx][ny] = maze[x][y] + 2

                # 도착지점이라면 통로의 수 반환
                elif maze[nx][ny] == 3:
                    result = (maze[x][y] // 2) -1
                    break
        

    print(f'#{tc} {result}')
