import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    slen1 = len(str1)
    slen2 = len(str2)

    max_num = 0
    for i in range(slen1):
        count = 0
        for j in range(slen2):
            if str1[i] == str2[j]:
                count += 1
        if max_num < count:
            max_num = count
    
    print(f'#{tc} {max_num}')



