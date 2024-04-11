#16. ファイルをN分割する
#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

user_input = input("自然数Nを入力してください: ")
with open("popular-names.txt") as f:
    lines = f.readlines()
    n = len(lines) // int(user_input)
    for i in range(int(user_input)):
        with open(f"16-output/popular-names_{i}.txt", mode="w") as f:
            f.write("".join(lines[i*n:(i+1)*n]))

# 確認コマンド： split -l 10 popular-names.txt