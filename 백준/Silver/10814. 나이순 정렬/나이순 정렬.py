"""
입력 값을 튜플로 나이와 이름을 묶어서 받고 0번(나이) 인덱스를 기준으로 정하고 2번 인덱스(input_count)을 차순위로 하여 정렬

"""

import sys
input = sys.stdin.readline

T = int(input())
list_1 = [0]*(T)
input_count = 0


for i in range(T):
    ageAndname = list(map(str, input().split()))
    ageAndname[0] = int(ageAndname[0])
    ageAndname.append(input_count)
    ageAndname = tuple(ageAndname)
    list_1[i] = ageAndname
    input_count += 1

list_1.sort(key = lambda x : (x[0], x[2]))
for tuple in list_1:
    print(tuple[0], tuple[1])