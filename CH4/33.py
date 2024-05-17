# 33. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．

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
flag2 = ""
meishikuList =[]
for i in sentence:
  if i["pos"] == "名詞":
    if (flag1 != "") & (flag2 != ""):
      meishikuList.append(flag1+flag2+i["surface"])
      flag1 = ""
      flag2 = ""
    else:
      flag1 = i["surface"]
  elif i["surface"]=="の":
    if flag1 != "":
      flag2 = "の"
  else:
    flag1 = ""
    flag2 = ""

print(meishikuList)