def fib(n, k):
    count = 1
    first_generation = 1
    population = 1
    while count < n+1:
        if count == 1 or count == 2:
            population += 3
            count += 1
        else:
            population += k
            count += 1
    return population


print(fib(5,3))
