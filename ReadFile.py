def ReadFile(fi):
	with open(fi,"r") as inp:# fix gap khong doc 2 ky tu nua,
		# bo hardcode
		N = int(inp.readline())
		Start = (int(inp.readline(3)),int(inp.readline(3))) #
		Goal  = (int(inp.readline(3)),int(inp.readline(3))) #
		A=[]
		for i in range(0,N):
			tmp = inp.readline()
			tmp = tmp.split()
			tmp = list(map(int,tmp))
			A.append(tmp)
			
	return N, Start, Goal, A