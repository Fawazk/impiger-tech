

def divisible(a,b,n):
    listofa=[]
    listofb = []
    for i in range(1,n+1):
        if i % a == 0:
            listofa.append(i)
        elif i % b == 0:
            listofb.append(i)
    return 'list of divisible of a: ',listofa, 'list of divisible of b',listofb
a = 5
b = 7
n = 100
print(divisible(a,b,n))