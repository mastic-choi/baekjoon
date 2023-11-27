T = int(input())
grade = list(map(int, input().split()))
grade.sort()

for i in range(len(grade)):
    grade[i] = grade[i]/grade[-1] * 100

print(sum(grade)/len(grade))