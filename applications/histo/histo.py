# Your code here
with open("robin.txt") as f:
    words = f.read()

def generate_hist(words):
    ignored_chars = '":;,.-+=/\|[]}{()*^&'
    contains_ignored = False
    # check for at least one ignored char
    for c in ignored_chars:
        if c in words:
            contains_ignored = True
            break
    if contains_ignored == False:
        return
    # remove ignored
    words = ''.join([char.lower() for char in words if char not in ignored_chars])
    words = words.split()
    hist = {}
    longest_word = ''
    # make histogram
    for word in words:
        if word in hist:
            hist[word] += '#'
        else:
            hist[word] = '#'
            if len(longest_word) < len(word):
                longest_word = word
    # sort the hist with the word count being the primary key and the alphabetical order being the s
    hist = {key: value for key, value in sorted(hist.items(), key=lambda pair: (-len(pair[1]), pair[0]))}
    for key, value in hist.items():
        print(key + ' ' * (len(longest_word) - len(key)) + value)
    

generate_hist(words)
