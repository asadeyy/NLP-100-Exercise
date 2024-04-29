#20 JSONデータの読み込み
#Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．

import json
jsonList = []
with open('jawiki-country.json') as f:
    for line in f.readlines():
        dic=json.loads(line)
        jsonList.append(dic)
for i in jsonList:
    if i['title']=='イギリス':
        print(i['text'])
        break