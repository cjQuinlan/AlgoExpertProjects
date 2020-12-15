def runLengthEncoding(string):
    # Write your code here.
	output=""
	piece=""
	count=1
	lastChar=""
	for cx in range(len(string)):
		char=string[cx]
		if char==lastChar:
			count += 1
		if count == 9:
			piece = str(count) + lastChar
			count = 0
			output += piece
			piece = ""
		if (char!=lastChar and lastChar != ""):
			if count>0:
				piece = str(count) + lastChar
			else:
				piece=""
			count = 1
			output += piece
			piece = char
		if cx==(len(string)-1):
			piece = str(count) + char
			output += piece
		lastChar = char
	return output

print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))
