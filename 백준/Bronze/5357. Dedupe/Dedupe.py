#백준 5357번 / Dedupe
t = int(input())  

for _ in range(t):
    s = input()

    result = []

    for char in s:
        if not result or result[-1] != char:
            result.append(char)

    print(''.join(result))
