#11. タブをスペースに置換
#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

with open('popular-names.txt') as f:
    txt_data = f.read()

del_tab = txt_data.replace('\t', ' ')
print(del_tab)

#確認コマンド： sed 's/\t/ /g' popular-names.txt