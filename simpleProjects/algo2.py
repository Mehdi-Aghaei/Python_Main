def isValidSubsequence(array, sequence):
    i = 0
    j = 0
    # i id of index array index and j is id of index of sequence 
    while i < len(array) and j < len(sequence):
        if array[i] == sequence[j]:
            j += 1
        i += 1
    return j == len(sequence)

a = [1,22,33,55,68,88,101,-1]

b = [121,22,33,55,68]
print(isValidSubsequence(a,b))