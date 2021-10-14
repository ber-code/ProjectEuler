from collections import Counter

message = [i for i in map(int, open("59_cipher.txt").read().split(","))]
# assume " " is most common character, hence XOR^ with " " to find 3 digit key
key = [Counter(message[i::3]).most_common(1)[0][0] ^ ord(" ") for i in range(3)]
print(sum(message[i] ^ key[i % 3] for i in range(len(message))))
