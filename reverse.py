input_list=[input() for i in range(int(input()))]
print(*list(map(lambda actual:int(str(actual)[::-1]),input_list)),sep='\n')