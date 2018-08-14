

def is_prime(n):
    for i in range(2,n+1):
        print('...'+str(i))

        if(n % i == 0):
            return False
        else:
            return True

print(is_prime(5))