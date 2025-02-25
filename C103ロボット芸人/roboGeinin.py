# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N,M = map(int, input().split());
move = [input().split() for i in range(M)]

for i in range(N):
    judge = True;
    output = [];
    for j in move:
        if (i + 1) % int(j[0]) == 0:
            output.append(j[1]);
            judge = False;
    if judge == True:
        print(i + 1);
    else:
        print(*output);