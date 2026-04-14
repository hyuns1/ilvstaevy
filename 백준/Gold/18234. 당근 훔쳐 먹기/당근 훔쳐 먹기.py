import sys
input = sys.stdin.readline

N, T = map(int, input().split())

carrots = []
for _ in range(N):
    w, p = map(int, input().split())
    carrots.append((w, p))

carrots.sort(key=lambda x: x[1])

total = 0
for i, (w, p) in enumerate(carrots):
    d = T - N + 1 + i
    total += w + (d - 1) * p

print(total)