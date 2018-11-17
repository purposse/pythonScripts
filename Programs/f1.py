def fibonacci(max):        # generator (not a function, since return replaced on yield)
    a, b = 0, 1
    while a < max:
        yield a            # return a, + remember the place of restart for the next call
        a, b = b, a + b    # parallel assignment, that is performed simultaneously and in parallel

for n in fibonacci(100):   # using generator fibonacci() as an iterator
    print (n)               # print all Fibonacci numbers less than 100 through the gap