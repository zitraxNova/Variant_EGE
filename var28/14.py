for x in range(1,300):
    n = 5 ** 2024 - 5 ** 1005 + 25 ** 650 + 3 * 5 ** 9 - x
    k = 0
    while n > 0:
        d = n % 5
        if d == 4:
            k += 1
        n = n // 5
    if k == 300:
        print(x)
# 157
