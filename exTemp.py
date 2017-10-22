def fab(n):
    c, a, b = 0, 0, 1

    while (c <= n):
        a, b = b, a+b
        #print(a)
        yield a
        c += 1

for n in fab(6):
    print(n)

f = fab(5)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

