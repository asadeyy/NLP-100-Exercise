# pip3 install mecab-python3 unidic-lite
with open("neko.txt") as f:
  neko = f.read()
  print(neko)

import MeCab
t = MeCab.Tagger()
with open("neko.txt.mecab",mode ="w") as f:
  f.write(t.parse(neko))

# 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
# 1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ

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