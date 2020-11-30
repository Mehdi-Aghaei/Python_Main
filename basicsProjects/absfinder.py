def smallestDifference(arrayOne, arrayTwo):
	A = sorted(arrayOne)
	B = sorted(arrayTwo)
	smallest=float("inf")
	current=float("inf")
	i = 0
	j = 0
	result = []
	while i < len(arrayOne) and j < len(arrayTwo):
		# move smaller value
		fn = A[i] #first Number
		sn = B[j] #secondNumber
		if (fn < sn):
			current = sn - fn
			i +=1
		elif (sn < fn):
			current = fn - sn
			j +=1
		else:
			return [fn,sn]
		if smallest > current :
			smallest = current
			result = [fn,sn]
			
	return result

