# 36. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

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
## matplotlibが日本語対応していないので入れる
# pip install japanize-matplotlib

index = 0
words = []
number = []
for j in wordCounter:
  words.append(j[0])
  number.append(j[1])
  index += 1
  if index == 10:
    break



import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

left = np.array(words)
height = np.array(number)
plt.bar(left, height)