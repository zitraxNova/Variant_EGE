for n in range(1, 1000):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n = '1' + bin_n
    else:
        bin_n = bin_n + '11'
    r = int(bin_n, 2)
    if r % 2 != 0 and r < 540:
        print(n)
# 133