# def fact(n):
#     if n==0:
#         return (1)
#     if n==1:
#         return (1)
#     else:
#         return n*fact(n-1)
#
#
# factorial_required=[int(input()) for i in range(int(input()))]
# print(*list(map(lambda x:fact(x),factorial_required)),sep='\n')
import math
T = int(input())
for i in range(0,T,1):
    N = int(input())
    print (math.factorial(N))