def solution(x, y):
    x,y = int(x), int(y)
    m,n = (x,y) if x>y else (y,x)

    i=0
    while m*n > 1:
        if n == 1:
            return str(i+(m//n)-1)
        else:
            i += m//n
            m,n = n,m%n
    return "impossible"

print(solution('4', '7'))