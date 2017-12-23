for triangle in range(int(input())):
	A, B, C = map(int, input().split())
	print(['NO', 'YES'][(A+B+C==180) and A!=0 and B!=0 and C!=0])