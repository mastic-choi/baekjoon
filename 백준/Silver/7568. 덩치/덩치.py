import sys
input = sys.stdin.readline

T = int(input())
list_1 = [0]*(T)
for i in range(T):
    usr_input = list(map(int, input().split()))
    list_1[i] = usr_input
grade = []
grade_count = 1
for q in range(len(list_1)):
    grade_count = 1
    j = list_1[q]
    new_list = list_1[:]
    del new_list[q]
    for k in new_list:
        if j[0] < k[0]:
            if j[1] < k[1]:
                grade_count += 1
    grade.append(grade_count)
for l in grade:
    print(l, end = " ")