n = int(input("Enter the limit: "))
a = 0
b = 1
sum = 0
list = []
while(sum <= n):
    list.append(sum)
    a = b
    b = sum
    sum = a + b
print("fibonacci list upto limit :",list)