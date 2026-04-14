N = int(input())
A = list(map(int, input().split()))

a = A.count(1)  # 1의 개수
b = A.count(2)  # 2의 개수

if a >= b and (a - b) % 3 == 0:
    print("Yes")
else:
    print("No")