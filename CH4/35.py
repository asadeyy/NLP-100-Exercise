# 35. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

sentence = []
with open("neko.txt.mecab") as f:
  for line in f:
      l1 = line.split("\t")
      if len(l1)>=2:
        if "-" in l1[4]:
          l2 = l1[4].split("-")
          sentence.append({"surface": l1[0], "base": l1[3], "pos": l2[0], "pos1": l2[1]})
        else:
            sentence.append({"surface": l1[0], "base": l1[3], "pos": l1[4], "pos1": ""})
# ここまで30.pyと同じ

from collections import Counter

target = []
for i in sentence:
  if i["pos"] == "名詞":
    target.append(i["base"])
wordCounter = Counter(target).most_common()
for j in wordCounter:
    print(j,end=",")