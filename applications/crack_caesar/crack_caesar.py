# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
with open("ciphertext.txt") as f:
    words = f.read()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
given_frequencies = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
letter_frequency = {}
# first get letter frequencies from file
for char in words:
    if char in letters:
        if char not in letter_frequency:
            letter_frequency[char] = 1
        else:
            letter_frequency[char] += 1
# sort and get list of letters from most frequent to least frequent
letter_frequency = [pair[0] for pair in sorted(letter_frequency.items(), key=lambda pair: -pair[1])]
# make a ciphertext key table with letter_frequency and given_frequencies
ciphertext_key = {key: value for key, value in zip(letter_frequency, given_frequencies)}
print(ciphertext_key)
# convert the text
words = list(words)
for i, char in enumerate(words):
    if char in letters:
        words[i] = ciphertext_key[char]
print(''.join(words))

