

def isValidSubsequence(array, sequence):
    # Write your code here.
	sqInx=0
	for x in range(len(array)):
		if array[x] == sequence[sqInx]:
			sqInx += 1
	
	if sqInx==len(sequence):
		return True
	else:
	    return False

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],  [1, 6, -1, 10]))