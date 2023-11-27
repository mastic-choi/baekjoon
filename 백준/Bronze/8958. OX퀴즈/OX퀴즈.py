t = int(input())
score = 0
sum_to_score = 0
for i in range(t):
    result = list(input())
    score = 0
    for j in range(len(result)):
        if result[j] == "O":
            if not j == 0:
                if result[j] == result[j-1]:
                    sum_to_score = sum_to_score + 1
                else:
                    sum_to_score = 1
            else:
                sum_to_score = 1
            score = score + sum_to_score
        elif result[j] == "X":
            sum_to_score = 0
            score = score + sum_to_score
    print(score)