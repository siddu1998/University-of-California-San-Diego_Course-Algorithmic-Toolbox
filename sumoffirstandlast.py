input_list=[input() for i in range(int(input()))]
answer=list(map(lambda name:int(name[0])+int(name[len(name)-1]),input_list))
print(*answer,sep='\n')