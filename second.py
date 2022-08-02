def evenindict(n):
    dic = {}
    for i in range(1,n):
        if i % 2 == 0:
            dic[i] = i
    return dic
n = 11
print(evenindict(n))