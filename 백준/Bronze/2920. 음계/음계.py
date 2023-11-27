sound_of_music = list(map(int, input().split()))
ascending = list(range(1, 9))
descending = list(range(1, 9))
descending.reverse()

if sound_of_music == ascending:
    print("ascending")
elif sound_of_music == descending:
    print("descending")
else:
    print("mixed")