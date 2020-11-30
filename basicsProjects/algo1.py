def twoNumberSum(array, targetSum):
    # Write your code here.
	for i in range(len(array)+1):
		firstNum = array[i]
		print(firstNum)
		for j in range(i+1,len(array)):
			secondNum = array[j]
			#print(secondNum)
			if firstNum + secondNum == targetSum:
				return( [firstNum, secondNum])
		
	print("FDF")

twoNumberSum([4,5,6],11) 
