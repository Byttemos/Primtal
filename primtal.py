for n in range(2,500):
    isPrime = True
    for i in range(2,n):
        if (n % i) == 0:
            isPrime = False
            break
    if (isPrime):
        print(n)