#21 カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ

import json
import re
jsonList = []
with open('jawiki-country.json') as f:
    for line in f.readlines():
        dic=json.loads(line)
        jsonList.append(dic)
for i in jsonList:
    if i['title']=='イギリス':
        # ここまで20.pyと同じ
        for line in i['text'].split('\n'):
            if re.search(r'\[\[Category:.+\]\]', line):
                print(line)