digits = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def int2Base(n, b):

        if n < 0: sign = -1
        elif n == 0: return digits[0]
        else: sign = 1
        n*=sign

        d = []
        while n:
            d.append(digits[n%b])
            n //= b
        
        if sign < 0: d.append("-")

        d.reverse()

        return "".join(d)

def solution(n, b):

    m = []
    z = n
    i = None

    while i not in m:

        m.append(z)
        x, y = int("".join(sorted(m[-1], reverse=True)), b), int("".join(sorted(m[-1])), b)
        z = int2Base(x-y, b)
        i = z = "0"*(len(str(m[-1]))-len(str(z))) + str(z)

    return len(m) - m.index(i)