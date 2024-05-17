# 31. 動詞
# 動詞の表層形をすべて抽出せよ．

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

for i in sentence:
  if i["pos"]=="動詞":
    print(i["surface"],end=",")