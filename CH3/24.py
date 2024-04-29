# wikipedia help早見表:https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
# 24 ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

import json
import re
jsonList = []
with open('jawiki-country.json') as f:
    for line in f.readlines():
        dic=json.loads(line)
        jsonList.append(dic)

sectionWithLevelList = []
for i in jsonList:
    if i['title']=='イギリス':
        # ここまで20.pyと同じ
        for line in i['text'].split('\n'):
            if re.search(r'\[\[ファイル:.+\|thumb\|.+\]\]', line):
                #print(line) 確認用
                print(re.sub(r'\|thumb\|.+', '', line).replace('[[ファイル:', ''))