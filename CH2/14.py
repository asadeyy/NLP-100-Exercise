#14. 先頭からN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

user_input = input("自然数Nを入力してください: ")
with open("popular-names.txt") as f:
    lines = f.readlines()
    for i in range(int(user_input)):
        print(lines[i], end="")


# 確認コマンド： head -n N popular-names.txt