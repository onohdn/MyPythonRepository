'''
Created on 2018/10/28

@author: onohdn

演習問題
入力した数値に対して、符号（正／0／負）を判定して表示するプログラムを作成しなさい。

期待結果
数値を入力してください->8
4の倍数です

数値を入力してください->9
4の倍数ではありません

'''

try:
    x = int(input("数値を入力してください->"))

    if x > 0:
        print("正の値です")
    elif x < 0:
        print("負の値です")
    else:
        print("0です")

except ValueError:

    print("数値を入力してください")
