# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N,K = map(int , input().split());
picture = []
for j in range(N):# 写真の情報をリストにまとめる。
    parts1 = [] #パーツを初期化
    for i in input().split():
        parts1.append(i)
    picture.append(parts1)
        
fixed = [];

for i in picture:
    parts2 = [];
    for j in range(int(N/K)):
        sum = 0;
        for m in range(K):
            sum += int(i[m + (j * K)]);
        parts2.append(sum);
    fixed.append(parts2);

fixed2 = [];
for p in range(int(N/K)):
    for i in range(int(N/K)):
        sum = 0;
        for j in range(K):
            sum += fixed[j + (p * K)][i];
        fixed2.append(int(sum/ (K*K)))
for i in range(int(N/K)):
    for j in range(int(N/K)):
        print(fixed2[j + (i * int(N/K))] , end = "")
        if j < (N/K)-1:
            print(" ", end = "");
    print("")
    