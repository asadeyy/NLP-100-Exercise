#06. 集合
#“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

def n_gram(n, sequence):
    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]

def main():
    s1 = "paraparaparadise"
    s2 = "paragraph"
    X = set(n_gram(2, s1))
    Y = set(n_gram(2, s2))
    print("X:", X)
    print("Y:", Y)
    print("和集合:", X | Y)
    print("積集合:", X & Y)
    print("差集合:", X - Y)
    print("Xにseが含まれるか:", 'se' in X)
    print("Yにseが含まれるか:", 'se' in Y)

if __name__ == '__main__':
    main()