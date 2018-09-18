#输出杨辉三角

def triangle(k):
    a = []
    l = []
    i = 0
    while i < 40:
        l.append(0)
        i += 1
    i = 0
    while i < 40:
        a.append(l)
        i += 1

    j = 1
    while j <= k:

        a[j][1] = 1
        a[j][j] = 1

        if j >= 2:
            z = 1
            while z <= j:
                a[j][z] = a[j-1][z-1] + a[j-1][z]
                z += 1
        j += 1

    i = 1
    while i <= k:
        j = 1
        c = []
        while j <= i:
            c.append(a[i][j])
            j += 1
        print(c)
        i += 1

if __name__ == '__main__':

  triangle(3)



