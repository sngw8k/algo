import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())


### in 함수 사용

# for tc in range(1, T+1):
    
#     str1 = input()
#     str2 = input()
#     result = 0
    
#     if str1 in str2:
#         result = 1
#     else:
#         result = 0
    
#     print(result)
        
# -----------------------------

for tc in range(1, T+1):
    
    str1 = input()
    str2 = input()

    slen1 = len(str1)
    slen2 = len(str2)

    result = 0
    for i in range(slen2 - slen1 + 1):
        for j in range(slen1):
            if str2[i+j] == str1[j]:
                continue
            else:
                break
        
        else:
            result = 1

    print(f'#{tc} {result}')


