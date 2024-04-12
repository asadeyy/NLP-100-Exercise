#17. １列目の文字列の異なり
#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．

with open("col1.txt") as f:
    col1 = f.readlines()
col1 = [c.strip() for c in col1]
col1_set = set(col1)
print(col1_set)

# 確認コマンド： cut -f 1 popular-names.txt | sort | uniq