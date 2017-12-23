n=int(input())
results=[]
for i in range(n):
    first,second = input().split()
    first=int(first)
    second=int(second)
    results.append(first+second)

print(*results,sep='\n')