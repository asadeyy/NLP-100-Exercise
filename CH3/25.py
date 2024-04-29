#25. テンプレートの抽出
#記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ

import json
import re
jsonList = []
with open('jawiki-country.json') as f:
    for line in f.readlines():
        dic=json.loads(line)
        jsonList.append(dic)

informationDict = {}
for i in jsonList:
    if i['title']=='イギリス':
        # ここまで20.pyと同じ
        for line in i['text'].split('\n'):
            if re.search(r'^\{\{基礎情報', line):
                for line in i['text'].split('\n'):
                    # print(line) 確認用
                    if re.search(r'^\}\}', line):
                        break
                    if re.search(r'^\|', line):
                        # print(line) 確認用
                        key = line.split('=')[0].replace('|', '').strip()
                        value = line.split('=')[1].strip()
                        informationDict[key] = value

print(informationDict)

