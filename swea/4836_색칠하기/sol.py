import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    # 칠하는 횟수
    paint = int(input())
    matrix = []
    paper = []
    

    # 종이 여백
    for row in range(10):
        # 새로운 내부 배열 선언
        paper.append([])
        for col in range(10):
            # 해당 내부 배열에 0값 추가
            paper[row].append(0)
    
    
    # 칠하는 횟수만큼 반복
    for _ in range(paint):
        info = list(map(int, input().split()))
        # matrix.append(info)
        
        x1 = info[0]
        x2 = info[2]
        y1 = info[1]
        y2 = info[3]

        # print(x1,x2,y1,y2)
        
        # if info[4] == 1:
        #     for i in range(x1, x2+1):
        #         for j in range(y1, y2+1):
        #             if paper[i][j] == 1:
        #                 pass
        #             else:
        #                 paper[i][j] += 1
        # else:
        #     for i in range(x1, x2+1):
        #         for j in range(y1, y2+1):
        #             if paper[i][j] == 2:
        #                 pass
        #             else:
        #                 paper[i][j] += 2
    

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if paper[i][j] == info[4]:
                    pass
                else:
                    paper[i][j] += info[4]


    count = 0
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 3:
                count += 1
    
    print(f'#{tc} {count}')

        


    