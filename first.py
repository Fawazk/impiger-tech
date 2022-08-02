def evennumber(n):
    list = []
    for i in range(1,n):
        if i % 2 == 0:
            list.append(i)
    return list 
n = 11
print(evennumber(n))
