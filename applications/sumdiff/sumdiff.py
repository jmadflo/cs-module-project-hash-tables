"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

initial_cache = {}
left_cache = {}
right_cache = {}
combination_cache = set()
for num in q:
    if num not in initial_cache:
        initial_cache[num] = f(num)
# print(initial_cache)
for a in q:
    print(a)
    for b in q:
        for c in q:
            for d in q:
                if (a, b) not in left_cache:
                    left_cache[(a, b)] = initial_cache[a] + initial_cache[b]
                if (c, d) not in right_cache:
                    right_cache[(c, d)] = initial_cache[c] - initial_cache[d]
                if left_cache[(a, b)] == right_cache[(c, d)]:
                    # f(1) + f(1) = f(12) - f(7)    10 + 10 = 54 - 34
                    combination_cache.add(f'f({a}) + f({b}) = f({c}) - f({d})    {initial_cache[a]} + {initial_cache[b]} = {initial_cache[c]} - {initial_cache[d]}')
for entry in combination_cache:
    print(entry)

