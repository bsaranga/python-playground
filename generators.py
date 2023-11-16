def naturalNumberGen(n):
    num = 1
    while num <= n:
        yield num
        num += 1

for i in naturalNumberGen(10):
    print(i)

print(sum(naturalNumberGen(1000)))