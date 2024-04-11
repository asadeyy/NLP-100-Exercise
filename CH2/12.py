#12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

col1_list = []
col2_list=[]
with open("popular-names.txt") as f:
    for line in f:
        col1_list.append(line.split("\t")[0])
        col2_list.append(line.split("\t")[1])
col1 = "\n".join(col1_list)
col2 = "\n".join(col2_list)

#col1の書き込み
with open("col1.txt", mode="w") as f:
    f.write(col1)

#col2の書き込み
with open("col2.txt", mode="w") as f:
    f.write(col2)

# 確認コマンド： cut -f 1,2 popular-names.txt