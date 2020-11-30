a=set((11,11,11,22,3,33,"hi",False))
print(a)
b =  tuple((11,11,22,False,"hi"))
print(b)
c = {2:1,"b":3}
print(c["b"])
sequence= [1, 6, -1, 10]
q =  set(sequence)
l = tuple(sequence)
w = tuple(q)
x =tuple(w)
print(sorted(q))
print(sorted(l))
print(w)
print(x)
if w == x:
    print(True)