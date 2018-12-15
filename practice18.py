'''
Created on 2018/11/24

@author: onohdn

演習問題
入力した数値に対して、符号（正／0／負）を判定する関数を作成し、結果を出力するプログラムを作成しなさい。
※結果は関数の呼び出し側で出力すること

期待結果
数値を入力してください->10
正の値です

数値を入力してください->0
0です

数値を入力してください->-6
負の値です

'''

def signDetermination(x):
    if x > 0:
        return("正の値です")
    elif x < 0:
        return("負の値です")
    else:
        return("0です")

try:
    x = int(input("数値を入力してください->"))

except ValueError:

    print("数値を入力してください")

ans = signDetermination(x)

print(ans)