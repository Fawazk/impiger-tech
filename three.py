
def strinlist(list):
    newlist = []
    for i in list:
        if type(i) == int:
            newlist.append(i)
        else:
            return newlist,("str found")
    if list == newlist:
        return newlist,('no str found')

list = [1,2,3,'r']
print(strinlist(list))