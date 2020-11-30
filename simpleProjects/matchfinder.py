def matchFinder(list1,list2):
    check =  False
    for i in list1:
        for j in list2:
            if i == j :
                check =True
                return check
    return check

a = [1,2,3]
b = [3,2,4]
print(matchFinder(a,b))
