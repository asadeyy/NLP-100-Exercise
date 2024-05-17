# 34. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ

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

flag1 = ""
endedMeishi = False
meishiku=[]
meishikuList =[]

for i in sentence:
  if i["pos"] == "名詞":
    if flag1 != "":
      meishiku.append(i["surface"])
      endedMeishi = True
    else:
      flag1 = i["surface"]
      meishiku.append(flag1)
  else:
    if (flag1 != "")&(endedMeishi):
      joinMeishi = "".join(meishiku)
      meishikuList.append(joinMeishi)
    flag1 =""
    meishiku = []
    endedMeishi = False

print(meishikuList)