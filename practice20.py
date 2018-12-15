'''
Created on 2018/11/25

@author: onohdn

演習問題
引数すべての値を足し算する関数を作成し、引数がそれぞれ３、２、１、０個の場合でも
実行可能かどうかを確認する。
※結果は関数の呼び出し側で出力すること

期待結果
数値を入力してください->10
引数なし = 0
引数１個 = 10
引数２個 = 20
引数３個 = 30

'''

def plus(**args):
    result = 0
    for i in args.values():
        result += i

    return result

x = int(input("数値を入力してください->"))

ans1 = plus()
ans2 = plus(a = x)
ans3 = plus(a = x,b = x)
ans4 = plus(a = x,b = x,c = x)

print("引数なし = ",ans1)
print("引数１個 = ",ans2)
print("引数２個 = ",ans3)
print("引数３個 = ",ans4)
