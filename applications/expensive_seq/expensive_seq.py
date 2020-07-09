# Your code here


def expensive_seq(x, y, z):
    # Your code here
    cache = {}
    def inner(a, b, c):
        if (a, b, c) in cache:
            return cache[(a, b, c)]
        if a <= 0: 
            cache[(a, b, c)] = b + c
        else:
            cache[(a, b, c)] = inner(a-1,b+1,c) + inner(a-2,b+2,c*2) + inner(a-3,b+3,c*3)
        return cache[(a, b, c)]
    return inner(x, y, z)


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
