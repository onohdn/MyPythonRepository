'''
Created on 2018/10/28

@author: onohdn

演習問題
入力した数値に対して、偶数の場合には数値を10倍にして出力するプログラムを作成しなさい。

期待結果
数値を入力してください->5
5

数値を入力してください->6
60

'''

try:
    x = int(input("数値を入力してください->"))

    if x%2 == 0:
        x = x * 10

    print(x)

except ValueError:

    print("数値を入力してください")
