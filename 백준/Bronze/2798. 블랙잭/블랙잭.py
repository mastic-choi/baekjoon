import itertools

n, m = map(int, input().split())
card = list(map(int, input().split()))
nCr = list(itertools.combinations(card, 3))
error = float('inf')
result = 0
for i in nCr:
    if sum(i) <= m:
        if error > (m- sum(i)):
            error = m - sum(i)
            result = sum(i)
print(result)