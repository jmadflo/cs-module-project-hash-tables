import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words = words.split()
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
table = {}
start_words = []
stop_words = []
for i, word in enumerate(words[:-1]):
    if word not in table:
        table[word] = [words[i+1]]
    else:
        table[word].append(words[i+1])
    # check to see if word is a start word or stop word
    if (word[0] in caps) or (word[0] == '"' and word[1] in caps):
        start_words.append(word)
    if (word[-1] in '.?!') or (word[-1] == '"' and word[-2] in '.?!'):
        stop_words.append(word)
stop_words.append(words[-1])
# print(start_words)
# print(table)
# TODO: construct 5 random sentences
# Your code here
start_word = random.choice(start_words)
print(start_word, end=" ")
prev = start_word
while True:
    next_word = random.choice(table[prev])
    print(next_word, end=" ")
    if next_word in stop_words:
        break
    else:
        prev = next_word
print("") # new line on console