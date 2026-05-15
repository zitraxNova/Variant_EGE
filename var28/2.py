for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((not y) <= (w == (not x))) and (not(z <= (not(y <= x))))
                if f == 1:
                    print(y, x, z, w, '|', f * 1)
                    
# yxzw