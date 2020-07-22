import numpy as np
from pprint import pprint


questions =[]
pow_vals = []


def multiply(times):
    mu, sigma = 14, 8 # mean and standard deviation
    s = np.random.normal(mu, sigma, 1000)

    s=s.astype(int)
    s = s[(s >= 7) & (s <= 19)]
    i = 0
    for _ in range(times):
        x = s[i]
        i += 1
        while(x <= 10):
            x = s[i]
            i += 1
        y = s[i]
        i += 1
        t1 = (str(x) + " x " + str(y) + " = ")
        t2 = (str(y) + " x " + str(x) + " = ")
        while(t1 in questions or t2 in questions or y == x or y >=10):
            y = s[i]
            i += 1
            t1 = (str(x) + " x " + str(y) + " = ")
            t2 = (str(y) + " x " + str(x) + " = ")
        if (i%2 == 0):
            q = (str(x) + " x " + str(y) + " = ")
        else:
            q = (str(y) + " x " + str(x) + " = ")

        questions.append(q)
        i+=1

def squares(times):
    sq = '\u00b2'
    mu, sigma = 17, 7 # mean and standard deviation
    s = np.random.uniform(low=11, high=26, size=1000)

    s=s.astype(int)
    s = s[(s >= 11) & (s <= 26)]
    i = 0
    for _ in range(times):
        x = s[i]
        i += 1
        while(x in pow_vals):
            if i == 999:
                print("out of unique squares in range")
                break
            x = s[i]
            i += 1
        pow_vals.append(x)
        q = str(x) + sq + " = "
        questions.append(q)


def cubes(times):
    sq = '\u00b3'
    mu, sigma = 8, 4 # mean and standard deviation
    s = np.random.uniform(low = 6, high = 12, size = 1000)

    s=s.astype(int)
    s = s[(s >= 6) & (s <= 12)]
    i = 0
    for _ in range(times):
        x = s[i]
        i += 1
        while(x in pow_vals):
            if i == 999:
                print("out of unique cubes in range ")
                return
            x = s[i]
            i += 1
        pow_vals.append(x)
        q = str(x) + sq + " = "
        questions.append(q)



def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1

def prime_mult(times):
    used = []
    primes = [i for i in range(4,19) if isPrime(i)]
    for _ in range(6):
        x = np.random.choice(primes)
        y = np.random.choice(primes)
        t = str(x) + "x" + str(y)
        while(y == x or y >=10 or x<= 10 or t in used):
            x = np.random.choice(primes)
            y = np.random.choice(primes)
            t = str(x) + "x" + str(y)
        ans = x * y
        print(x," , ", y)
        used.append(t)
        q = str(ans) + " = " #+ str(x) + " x " + str(y)
        questions.append(q)      



# cubes til 6 to 12
# squares till 11 to 26 mean 17
# make another file which sends email 
# automate for everyday at a time