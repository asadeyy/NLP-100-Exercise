#10. 行数のカウント
#行数をカウントせよ．確認にはwcコマンドを用いよ．

count = 0
with open('popular-names.txt') as f:
    for line in f:
        count += 1
print(count)

# 確認コマンド： wc -l popular-names.txt
