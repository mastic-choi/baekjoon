#10816 숫자카드
# 이분분석 카테고리
import sys
from collections import Counter

M = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().split()))
'''
def binarySearch(list, target):
    list.sort()
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            return True
        elif list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
answer = []
for i in nList:
    count = 0
    while binarySearch(mList, i) is True:
        mList.remove(i)
        count += 1
    answer.append(count)
print(*answer)
'''

count_dic = Counter(mList)

answer = [count_dic[num] for num in nList]
print(*answer)
