#19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

from collections import Counter

with open("popular-names.txt") as f:
    col1 = f.readlines()
col1 = [c.split("\t")[0] for c in col1]
col1_counter = Counter(col1)
col1_counter = col1_counter.most_common()
for c in col1_counter:
    print(c)

#参考リンク：https://docs.python.org/ja/3/library/collections.html#collections.Counter

# 確認コマンド： cut -f 1 popular-names.txt | sort | uniq -c | sort -r