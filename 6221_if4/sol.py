import sys
sys.stdin = open('input.txt', encoding='utf-8')
#encoding='utf-8'

man1 = input()
man2 = input()


# if man1 == '가위' and man2 == '가위':
#     print('Result : Draw')
# elif man1 == '가위' and man2 == '바위':
#     print('Result : Man2 win!')
# elif man1 == '가위' and man2 == '보':
#     print('Result : Man1 win!')
# elif man1 == '바위' and man2 == '가위':
#     print('Result : Man1 win!')
# elif man1 == '바위' and man2 == '바위':
#     print('Result : Draw')
# elif man1 == '바위' and man2 == '보':
#     print('Result : Man2 win!')
# elif man1 == '보' and man2 == '가위':
#     print('Result : Man2 win!')
# elif man1 == '보' and man2 == '바위':
#     print('Result : Man1 win!')
# elif man1 == '보' and man2 == '보':
#     print('Result : Draw')


# 가위, 바위, 보
#  0  ,  1  , 2

# 보, (가위)   win2   2
#(바위), 가위  win1   1
# (보), 바위   win1   1
# (가위), 바위 win2   -1
# (바위), 보   win2   -1
# 가위, (보)   win1   -2
rcp = ['가위', '바위', '보']

man1_idx = rcp.index(man1)
man2_idx = rcp.index(man2)

result = man1_idx - man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
else:
    if result == -1:
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')