def no_dups(s):
    # Your code here
    repeats = {}
    words = s.split(' ')
    new_words = []
    for index, word in enumerate(words):
        # print(index, word)
        if word not in repeats:
            repeats[word] = True
            new_words.append(word)
        # print(repeats)
    return ' '.join(new_words)




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))