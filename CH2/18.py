#18. 各行を3コラム目の数値の降順にソート
#各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
#確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

with open("popular-names.txt") as f:
    lines = f.readlines()
lines = [line.split() for line in lines]
lines.sort(key=lambda x: int(x[2]), reverse=True)
for line in lines:
    print("\t".join(line))

    
# 確認コマンド： sort -k 3 -r popular-names.txt