'''
Created on 2018/10/28

@author: onohdn

演習問題
24から100までに存在する6の倍数の数値をすべて出力するプログラムを作成しなさい。

期待結果
24
30
36
42
48
54
60
66
72
78
84
90
96

'''
for i in range(24,100):
    if i%6 == 0:
        print(i)