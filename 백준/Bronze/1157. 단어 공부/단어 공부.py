string = input().lower()
string_set = list(set(string))
cnt = []

for i in string_set:
    a = string.count(i)
    cnt.append(a)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(string_set[(cnt.index(max(cnt)))].upper())