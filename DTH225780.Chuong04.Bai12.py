def oscillate(start, stop):
    for i in range(start, 0, 1):
        yield i
        yield -i

    for i in range(0, stop): 
        yield i
        yield -i

for n in oscillate(-3, 5):
    print(n, end=' ')
