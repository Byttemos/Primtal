n = 2
while (n != 300):

    for i in range(2,n):
        if(n % i != 0):
            print(n)
        else:
            break
        n = n + 1