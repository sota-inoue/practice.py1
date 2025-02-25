# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import math;
## 1/4の円の格子を求める。
r = float(input());
halfOfHarfSquart = 0;
for y in range(math.ceil(r)): ##高さ0,1,2の順に求めていく。
    xSq = r**2 - y**2;
    halfOfHarfSquart += math.ceil(math.sqrt(xSq));
print(halfOfHarfSquart * 4);