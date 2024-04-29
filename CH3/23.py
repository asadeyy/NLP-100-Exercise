#23 セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

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
            if re.search(r'^==.+==*$', line):
                # print(line) 確認用
                name = line.replace('=', '')
                level = 0
                if "=====" in line:
                    level = 4
                elif "====" in line:
                    level = 3
                elif "===" in line:
                    level = 2
                elif "==" in line:
                    level = 1
                sectionWithLevelList.append((name, level))

for section in sectionWithLevelList:
    print(section)