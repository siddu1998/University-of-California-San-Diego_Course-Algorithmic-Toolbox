test_cases = int(input())
entries=[]
max_min=[]
for i in range(test_cases):
    A,B=input().split(' ')
    A=int(A)
    B=int(B)
    max_min.append((max(A,B),A+B))


for i in range(test_cases):
    print(max_min[i][0],max_min[i][1])