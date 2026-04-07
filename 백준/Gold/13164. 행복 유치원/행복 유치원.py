N, K = map(int, input().split())
h = list(map(int, input().split()))

gap = sorted(h[i+1] - h[i] for i in range(N - 1))

total = sum(gap)
for i in range(1, K):
    total -= gap[-i]

print(total)