# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N,K = map(int , input().split());
picture = []
for j in range(N):# 写真の情報をリストにまとめる。
    picture.append(list(map(int, input().split())));#数値を" "で区切ってリスト化したものをリストに入れる。
    
row_sum = []; #変数名をfixedからrow_sumに変更しました。
for row in picture: #変数名iをrowに変更しました。
    #変数名をparts2からparts_row_sumに変更しました。
    # int(N/K)をN//Kに変えた。割り算の小数点以下切り捨て
    #行ごとの合計を内包表記で記述しました。
    parts_row_sum = [sum(row[ j*K : (j+1) * K]) for j in range(N//K)];#(j + 1) * Kまでというのは実際にはinedx(j + 1)*K-1まで
    row_sum.append(parts_row_sum);

reduced_img = []; #変数名をfixed2から「画素数の減った画像という意味のreduced_img」に変更しました。
for p in range(N//K):
    parts3 = []
    for i in range(N//K):
        block_sum = sum(row_sum[j + (p * K)][i] for j in range(K)); #sumを内包表記を使用して行数を減らしました。
        parts3.append(block_sum // (K*K))  #int(sum/ (K*K)) を sum // (K*K)に変更
    reduced_img.append(parts3)

for line in reduced_img: #アスタリスクを使ったアンパックを使ってみた。
    print(*line);