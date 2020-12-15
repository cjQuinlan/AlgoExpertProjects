def twoNumberSum(array, targetSum):
    # Write your code here.
	Dict = {}
	for x in range(len(array)):
		Dict[targetSum - array[x]]=array[x]
	
	for x in range(len(array)):
		Y = Dict.get(array[x],False)
		if Y != False:
			if Y != array[x]:
				return [Y,array[x]]
	return []

print(twoNumberSum([99, 5, -4, 8, 11, 1, -1, 6],10))
