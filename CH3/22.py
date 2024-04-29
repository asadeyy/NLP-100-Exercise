#22 カテゴリ名の抽出
#記事中に含まれるカテゴリ名を（行単位ではなく名前で）抽出せよ．

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
                # ここまで21.pyと同じ
                print(line.replace('[[Category:', '').replace(']]', ''))