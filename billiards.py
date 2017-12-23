import numpy as np
n=int(input())
player1=[]
player2=[]
for i in range(n):

    s,t=input().split()
    s=int(s)
    t=int(t)
    player1.append(s)
    player2.append(t)

np_player1 = np.array(player1)
np_player2 = np.array(player2)

np_diff=(np_player1-np_player2)
np_abs_diff=abs(np_diff)
winner_index = np_abs_diff.argmax()

if np_diff[winner_index] < 0:

    print('2 ',abs(np_diff[winner_index]))
else:
    print("1 ",abs(np_diff[winner_index]))