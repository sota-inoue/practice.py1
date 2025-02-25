# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
S = input()
line = [s for s in S]

if line[0] == line[1] == line[2] == line[3]:
    print("FourCard")
elif line[0] == line[1] == line[2] or line[0] == line[1] == line[3] or line[0] == line[2] ==line[3] or line[1] == line[2] == line[3]:
    if line[0] == "*" or line[1] == "*" or line[2] == "*" or line[3] == "*":
        print("FourCard");
    else:
        print("ThreeCard");
elif line[0] == line[1] or line[0] == line[2] or line[0] == line[3] or line[1] == line[2] or line[1] == line[3] or line[2] == line[3]:
    if line[0] == "*" or line[1] == "*" or line[2] == "*" or line[3] == "*":
        print("ThreeCard");
    elif line[0] == line[1] and line[2] == line[3] or line[0] == line[2] and line[1] == line[3] or line[0] == line[3] and line[1] == line[2]:
        print("TwoPair");
    else:
        print("OnePair");
elif line[0] == "*" or line[1] == "*" or line[2] == "*" or line[3] == "*":
    print("OnePair");
else:
    print("NoPair")