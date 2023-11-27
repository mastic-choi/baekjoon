import string
s = list(input())
for k in list(string.ascii_lowercase):
    if k in s:
        print(s.index(k), end=" ")
    else:
        print(-1, end = " ")