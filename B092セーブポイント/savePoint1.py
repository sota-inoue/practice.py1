# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N, W, K = map (int, input().split());
Lines = []
N_adress = [];
SPAdress = {}; #Save_Point_Adressのこと
SPDis = {}#Save_Point_Distanceのこと
for i in range(N):
    Lines.append(input());
#print(Lines);
x = 0;
for Line in Lines:
    x += 1;
    y = 0;
    for i in Line:
        y += 1;
        if i == "N":
            N_adress =[x,y];
        elif i !="#":
            SPAdress[i] = [x,y];
    
    
#print(SPAdress);
#print(N_adress);
SPDis_min = abs(N_adress[0] - SPAdress["1"][0]) + abs(N_adress[1] - SPAdress["1"][1]);
for i in SPAdress:
    SPDis[i] = abs(N_adress[0] - SPAdress[i][0]) + abs(N_adress[1] - SPAdress[i][1]);
    if SPDis_min > SPDis[i]:
        SPDis_min = SPDis[i];
count = 0
for i in SPDis:
    if SPDis_min == SPDis[i]:
        count += 1;
print(count);

for i in range(K):
    if SPDis[str(i+1)] == SPDis_min:
        print(i+1);