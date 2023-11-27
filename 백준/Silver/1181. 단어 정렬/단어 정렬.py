T = int(input())
word_list = []
for _ in range(T):
    word = input()
    word_list.append(word)
word_list = list(set(word_list))
word_list.sort(key=lambda x: (len(x), x))
for i in word_list:
    print(i)