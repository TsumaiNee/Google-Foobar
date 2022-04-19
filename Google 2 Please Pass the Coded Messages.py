
def solution(l):

    def remove(l):

        if l: return l.pop(0)
        else:
            return 0

    l.sort()

    a = [[],[],[]]

    for i in range(len(l)): a[l[i]%3].append(l[i])

    n = sum(l)
    if n%3 > 0:
        if remove(a[n%3]) == 0:
            if remove(a[2-((n%3)+1)%2]) == 0: return 0
            if remove(a[2-((n%3)+1)%2]) == 0: return 0

    if not any(a): return 0

    b = sorted([str(i) for sub in a for i in sub])

    return int("".join(b)[::-1])

print(solution([3, 1, 4, 1]))