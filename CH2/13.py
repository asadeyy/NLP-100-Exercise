#13. col1.txtとcol2.txtをマージ
#12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

col1 = []
col2 = []
with open("col1.txt") as f:
    for line in f:
        col1.append(line.strip())
with open("col2.txt") as f:
    for line in f:
        col2.append(line.strip())

with open("merge.txt", mode="w") as f:
    for c1, c2 in zip(col1, col2):
        f.write(f"{c1}\t{c2}\n")

# 確認コマンド： paste col1.txt col2.txt