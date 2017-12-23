def check(list_element):
    if list_element<10:
        return "What an obedient servant you are!"
    else:
        return -1
servent_list=[int(input()) for i in range(int(input()))]

print(*list(map(lambda x:check(x),servent_list)),sep='\n')