numbers_list =[int(input()) for i in range(int(input()))]
string_list  =list(map(str,numbers_list))
four_count=list(map(lambda x:x.count('4'),string_list))
print(*four_count,sep='\n')