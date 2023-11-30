#counting sort을 진행해야 하는 문제
T = int(input())
usr_input = [0 for i in range(10001)]

for _ in range(T):
    usr_input[int(input())] += 1
for idx, count in enumerate(usr_input):
    if not count == 0:
        for _ in range(count):
            print(idx)
