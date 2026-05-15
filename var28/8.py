from itertools import product
a = '01234'
nechet = '13'
k = 0

for x in product(a, repeat=6):
    s = ''.join(x)
    if s[0] != '0' and sum(s.count(d) for d in nechet) == 2:
        k += 1
print(k)
# 3780