n = int(input(" Enter number of words: "))

words = []

for i in range(n):
    word = input().lower()
    words.append(word)

counts = {}

for word in words:
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

print(counts)