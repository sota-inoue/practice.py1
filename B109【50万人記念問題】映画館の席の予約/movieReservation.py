# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N,H,W,P,Q = map(int,input().split());
Sheets = [[str(h),str(w)] for h in range(H) for w in range(W)];

ReservedSheets = [input().split() for h in range(N)];

EmptySheets = []
for Sheet in Sheets:
    TF = True;
    for ReservedSheet in ReservedSheets:
        if Sheet == ReservedSheet:
            TF = False;
    if TF == True:
        EmptySheets.append(Sheet);

manhattanMin = abs(P - int(EmptySheets[0][0])) + abs(Q - int(EmptySheets[0][1])); 
for EmptySheet in EmptySheets:
    manhattan = abs(P - int(EmptySheet[0])) + abs(Q - int(EmptySheet[1]));
    if manhattan < manhattanMin:
        manhattanMin = manhattan;

for EmptySheet in EmptySheets:
    if (abs(P - int(EmptySheet[0])) + abs(Q - int(EmptySheet[1]))) == manhattanMin:
        print(*EmptySheet);