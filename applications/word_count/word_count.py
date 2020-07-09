def word_count(s):
    # Your code here
    # first clean the text of unwanted characters
    clean = []
    unwanted_chars = '":;,.-+=/\|[]}{()*^&'
    for c in s:
        if c not in unwanted_chars:
            clean.append(c)
    clean = ''.join(clean)
    clean = clean.split()
    table = {}
    # now populate the table
    for word in clean:
        word = word.lower()
        if word not in table:
            table[word] = 1
        else:
            table[word] += 1
    return table





if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))