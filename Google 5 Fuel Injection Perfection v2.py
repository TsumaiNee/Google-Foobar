def solution(n):

    i = 0
    n = int(n)

    while n > 1:

        if n & 1 == 0:
            n //= 2
        elif n == 3 or n & 3 == 1:
            n -= 1
        else:
            n += 1
        i += 1

    return i

print(solution("127"))