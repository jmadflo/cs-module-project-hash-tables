"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
def identify_combinations(q):
    initial_cache = {}
    combination_cache = {}
    for num in q:
        if num not in initial_cache:
            initial_cache[num] = f(num)
    def inner(a, b, c, d):
        for a in q:
            for b in q:
                for c in q:
                    for d in q:
                        if f(a) + f(b) == f(c) - f(d) and (a, b, c, d) not in combination_cache:
                            combination_cache[(a, b, c, d)] = 1
