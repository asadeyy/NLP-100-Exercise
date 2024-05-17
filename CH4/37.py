# 37. 「猫」と共起頻度の高い上位10語
# 「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

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

all_words = []
for i in sentence:
  if i["pos"] != "補助記号":
    all_words.append(i["base"])

def countup(target_word,nearby_word,d):
  if not(target_word in d.keys()):
    d[target_word]={}
  if not(nearby_word in d[target_word].keys()):
    d[target_word][nearby_word] = 0
  d[target_word][nearby_word] += 1

kyouki_dict={}
for i in range(0,len(all_words)-1):
  target_word = all_words[i]
  before_word = all_words[i-1]
  after_word = all_words[i+1]
  if not(i == 0):
    countup(target_word,before_word,kyouki_dict)
  if not(i == len(all_words)-1):
    countup(target_word,after_word,kyouki_dict)

# 共起頻度が高い10語
ten_kyouki_words = sorted(kyouki_dict["猫"].items(), key = lambda x : x[1], reverse=True)[0:9]

## グラフの描画
left = np.array([ten_kyouki_words[x][0] for x in range(len(ten_kyouki_words))])
height = np.array([ten_kyouki_words[x][1] for x in range(len(ten_kyouki_words))])
plt.bar(left, height)
