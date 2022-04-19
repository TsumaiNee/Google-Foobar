def nearPow2(x):

    pos = ((log(x)/log(2))//1, (log(x)/log(2))//1+1)
    return min(pos, key= lambda z: abs(x-2**z))

def log(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)

def solution(n):
    
    n = int(n)

    i=0
    while n > 1:

        x = nearPow2(n)
        if (n & (n-1) == 0) and n != 0:
            return int(i+x)
        else:
            i += abs(2**x - n)
            n = int(2**x)

print(solution('4'))
