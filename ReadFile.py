import os
def ReadFile(fi):
	
	if os.path.isfile(fi)==False:
		print("Error file input")
		exit(1)
	with open(fi,"r") as inp:
		N = int(inp.readline())
		Start = (inp.readline())
		Start = Start.split()
		Start = list(map(int,Start))
		Goal  = (inp.readline())
		Goal  = Goal.split()
		Goal  = list(map(int,Goal))
		Start = tuple(Start)
		Goal  = tuple(Goal)
		A=[]
		for i in range(0,N):
			tmp = inp.readline()
			tmp = tmp.split()
			tmp = list(map(int,tmp))
			A.append(tmp)
		
	return N, Start, Goal, A