#15. 末尾のN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

user_input = input("自然数Nを入力してください: ")
with open("popular-names.txt") as f:
    lines = f.readlines()
    lines.reverse()
    for i in range(int(user_input)):
        print(lines[i], end="")


# 確認コマンド： tail -n N popular-names.txt