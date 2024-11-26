import sys


X = int(sys.stdin.readline())
lst = [list(map(int, input().split())) for _ in range(X)]
std = [set() for _ in range(X)]

# 5학년까지 비교
for i in range(5):
    for j in range(X):
        for k in range(j+1, X):
            # j와 k는 다른학생 (j < k)
            if lst[j][i] == lst[k][i]:
                # 같은 반인거 확인했으면 기록해야지
                std[j].add(k)
                std[k].add(j)
# 각 학생별로 겹치는 횟수 구하기
max_count = -1
candidate = -1
for i in range(X):
    if len(std[i]) > max_count:
        max_count = len(std[i])
        candidate = i + 1
print(candidate)