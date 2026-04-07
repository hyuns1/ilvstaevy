N = int(input())
trees = list(map(int, input().split()))

trees.sort(reverse=True)  # 생장기간 내림차순 정렬

last_day = 0
for i, t in enumerate(trees):
    last_day = max(last_day, (i + 1) + t)

print(last_day + 1)