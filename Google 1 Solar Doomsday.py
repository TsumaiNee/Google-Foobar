import math

def solution(area):
    
    f = []
    a = area
    while area != sum(f):
        
        f.append(int(((a**0.5)//1)**2))
        a -= f[-1]
        
    return f

print(solution(15324))
print(solution(12))