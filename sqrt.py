from math import sqrt
input_list = [int(input()) for i in range(int(input()))]
print(*list(map(

    lambda x:int(sqrt(x)),input_list
)



),sep='\n')