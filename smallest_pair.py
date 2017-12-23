l = []
t = int(input())
while t > 0:
     n = int(input())
     l = [int(x) for x in input().split()]
     l.sort()
     print(l[0] + l[1])
     t -= 1


