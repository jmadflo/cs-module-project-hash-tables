import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words = words.split()
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
table = {}
start_words = set()
stop_words = set()
for i, word in enumerate(words[:-1]):
    if word not in table:
        table[word] = [words[i+1]]
    else:
        table[word].append(words[i+1])
    # check to see if word is a start word or stop word
    if (word[0] in caps) or (word[0] == '"' and word[1] in caps):
        start_words.add(word)
    if (word[-1] in '.?!') or (word[-1] == '"' and word[-2] in '.?!'):
        stop_words.add(word)
stop_words.add(words[-1])
# print(start_words)
# print(table)
# TODO: construct 5 random sentences
# Your code here
print("\n") # new line on console
for x in range(5): # each iteration of the loop makes one sentence, so we run 5 interations for 5 sentences
    start_words = list(start_words)
    stop_words = list(stop_words)
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
print("\n") # new line on console