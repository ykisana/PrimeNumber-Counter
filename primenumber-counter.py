import random

def main():
    #setting intial value
    #intial value of 2 takes care of the first prime

    intial = 2
    k = 4

    #setting for while loop and prompt before start
    run = True
    input("Press Any Key To Start")

    #takes care of first prime
    print(intial)

    while run:
        intial += 1
        if isPrime(intial,k):
            print(intial)

#millerRabin and PrimeCheck implemented from GeeksforGeeks.org
#https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/

def millerRabin(d,n):
    a = 2 + random.randint(1,n - 4)
    x = pow(a,d)%n

    if (x==1 or x==n - 1):
        return True;

    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;

        if (x == 1):
            return False;
        if (x == n - 1):
            return True;

    return False;

def isPrime(n, k):

    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;

    d = n - 1;
    while (d % 2 == 0):
        d //= 2;

    for i in range(k):
        if (millerRabin(d, n) == False):
            return False;

    return True;

main()