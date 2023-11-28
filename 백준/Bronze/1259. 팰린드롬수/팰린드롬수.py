while True:
    num = list(map(int, input()))
    if num[0] == 0:
        break
    idx=int(len(num)/2)
    if len(num)%2==0:
        answer1 = num[:idx]
        answer2 = num[idx:]
    else:
        answer1 = num[:idx+1]
        answer2 = num[idx:]
    if answer1 == list(reversed(answer2)):
        print("yes")
    else:
        print("no")