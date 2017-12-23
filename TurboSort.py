t = int(input())
a = []
for i in range(t):

    a.append(int(input()))
a.sort()
print(*a, sep='\n')  