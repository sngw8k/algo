import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    
    N = int(input())
    home = list(map(int, input().split()))
    count = 0

    for i in range(2, N-2):
        if home[i] > home[i-1] and home[i] > home[i-2] and home[i] > home[i+1] and home[i] > home[i+2]:
            count += home[i] - max(home[i-1], home[i-2], home[i+1], home[i+2])
        else:
            pass

    # print(count)
    print(f'#{tc} {count}')
    # print(home)

    
