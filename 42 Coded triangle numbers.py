f = open("42_words.txt", "r").read()
words = f.replace('"', "").split(",")
print(words)


def word_sum(word):
    ret = 0
    for char in word:
        ret += ord(char) - 64
    return ret


def triangler(n):
    return n * (n + 1) / 2


longest_word = 0
for word in words:
    if len(word) > longest_word:
        longest_word = len(word)
cap = longest_word * 26

triangle_nums = set()
check = 1
while triangler(check) < cap:
    triangle_nums.add(triangler(check))
    check += 1

answer = 0
for word in words:
    if word_sum(word) in triangle_nums:
        answer += 1

print(answer)
