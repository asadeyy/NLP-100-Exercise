# 39. Zipfの法則
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ

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
import numpy as np
import matplotlib.pyplot as plt

target = []
for i in sentence:
  if i["pos"] == "名詞":
    target.append(i["base"])
wordCounter = Counter(target).most_common()
for j in wordCounter:
    print(j,end=",")

# ここまで35.pyと同じ
x =[i+1 for i in range(len(Counter(target).values()))]
y = sorted(Counter(target).values(),reverse=True)

fig, ax = plt.subplots()
ax.scatter(x,y)
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()