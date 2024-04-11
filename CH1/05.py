#05. n-gram
#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
#この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．

import re

def n_gram(n, sequence):
    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]

def main():
    sentence = "I am an NLPer"
    words = re.sub(r'[,.]', '', sentence).split()
    print(n_gram(2, words))
    print(n_gram(2, sentence.replace(' ', '')))

if __name__ == '__main__':
    main()
