'''
오리는 매일 오전, 당근이 없으면 심고, 있으면 영양제를 준다.
토끼는 매일 오후, 최대 1개의 당근을 훔칠 수 있다.
d일 오후 당근 i의 맛 = wi + (d - 1) * pi

1. 같은 당근을 두 번 먹는 것은 손해이다.
중간에 뽑으면 영양제 누적이 리셋 (또한 심는 날에는 영양제 누적이 없음 -> 영양제 하나 손해)
wi <= pi 조건에 의해 항상 손해이거나 본전
따라서 최대 한 번만 먹는 것이 최적이다.

2. 최대한 늦게 먹을수록 이득이다.
"당근 i의 맛 = wi + (d - 1) * pi"에서 d가 클수록 맛이 커지므로
마지막 N일에 먹는 것이 이득

3. pi가 큰 당근일수록 늦게 먹기.
늦게 먹을수록 영양제 누적이 커지므로 
pi 값을 오름차순 정렬 후 순서대로 배정하기
(d가 클 수록 이득인 당근 -> pi가 큰 당근)
'''


import sys
input = sys.stdin.readline

N, T = map(int, input().split())

carrots = []
for _ in range(N):
    w, p = map(int, input().split())
    carrots.append((w, p))

# p 오름차순 정렬
carrots.sort(key=lambda x: x[1])

total = 0
for i, (w, p) in enumerate(carrots):
    d = T - N + 1 + i  # 당근을 먹는 배정된 날짜
    total += w + (d - 1) * p

print(total)