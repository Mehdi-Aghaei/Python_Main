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
# Program to check if a Python list contains elements of another list
'''
def list_contains(List1, List2): 

    set1 = set(List1) 
    set2 = set(List2) 
    if set1.intersection(set2): 
        return True 
    else: 
        return False

# Test Case 1
List1 = ['a', 'e', 'i', 'o', 'u'] 
List2 = ['x', 'y', 'z', 'l', 'm'] 
print("Test Case#1 ", list_contains(List1, List2)) 

# Test Case 2  
List1 = ['a', 'e', 'i', 'o', 'u']  
List2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']  
print("Test Case#2 ", list_contains(List1, List2)) '''