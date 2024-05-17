# 38. ヒストグラム
# 単語の出現頻度のヒストグラムを描け．

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

from collections import Counter

target = []
for i in sentence:
  if i["pos"] == "名詞":
    target.append(i["base"])
wordCounter = Counter(target).most_common()
for j in wordCounter:
    print(j,end=",")

# ここまで35.pyと同じ
## matplotlibが日本語対応していないので入れる
# pip install japanize-matplotlib

import numpy as np
import matplotlib.pyplot as plt

plt.hist(Counter(target).values(),bins=100)
plt.show()

# これだと1200以上が一部あるが、見にくいので40までの範囲だけ見てみる
plt.hist(Counter(target).values(),bins=50,range=(0,40))
plt.show()