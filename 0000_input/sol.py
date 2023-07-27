import sys
sys.stdin = open('input.txt')

# N = int(input())

# if N % 2 == 1:
#     print('홀수')
# else:
#     print('짝수')

TC = int(input())    # txt 파일 맨위의 testcase 숫자를 받아옴

for i in range(TC):
    N = int(input())
    
    if N % 2 == 1:
        print('홀수')
    else:
        print('짝수')

# 1차원 리스트 input 받기

# numbers = input().split()
# for number in numbers:
#     int_num = int(number)

#     if int_num % 2 == 1:
#         print(f'{int_num}은 홀수')

numbers =list(map(int, input().split()))

for number in numbers:
    if number % 2 ==1:
        print(f'{number}은 홀수')


# 2차월 리스트 input 받기
N = int(input())
matrix = []

for i in range(N):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)

for row in matrix:
    for item in row:
        if item == 5:
            print('5가 있습니다.')
        
