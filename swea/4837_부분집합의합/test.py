numbers = [2, 5, 3, 1, 8]

# 부분집합을 구하는 배열의 길이
n = len(numbers)

# 모든 부분집합의 경우의 수 만큼 반복문을 실행
for i in range(1<<n):

    temp = []
    for j in range(n):
        if i & (1<<j):
            temp.append(numbers[j])

    print(temp)