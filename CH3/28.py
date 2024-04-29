#Help早見表:https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
#28 mediaWikiマークアップの除去
#27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

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
                        # ここまで25.pyと同じ
                        value = line.split('=')[1].strip().replace('\'', '').replace('[[', '').replace(']]', '').replace('*','').replace('{{','').replace('}}','').replace('ファイル:','')
                        informationDict[key] = value

for key, value in informationDict.items():
    print(key+"|"+value)

