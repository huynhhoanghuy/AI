def ReadFile(fi):
	with open(fi,"r") as inp:
		N = int(inp.readline(2))
		Start = (int(inp.readline(2)),int(inp.readline(2)))
		Goal  = (int(inp.readline(2)),int(inp.readline(2)))
		A=[]
		for i in range(0,N):
			tmp = inp.readline()
			tmp = tmp.split()
			tmp = list(map(int,tmp))
			A.append(tmp)
			
	return N, Start, Goal, A