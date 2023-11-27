#6씩 증가 1 -> 7(6증), 7 -> 19(12증)...
n = int(input())
cnt = 1
room_num = 1

while room_num < n:
    room_num = room_num + 6*cnt
    cnt = cnt + 1
print(cnt)