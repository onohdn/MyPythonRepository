'''
Created on 2018/11/11

@author: onohdn

演習問題
月の種類（"4月","5月","6月","7月","8月","9月"）を全て出力した後、"10月"を末尾に追加、追加後の全ての要素を出力するプログラムを作成しなさい。

期待結果
4月
5月
6月
7月
8月

4月
5月
6月
7月
8月
9月

'''
monthList = ["4月","5月","6月","7月","8月","9月"]

#要素の全出力
for i in monthList:
    print(i)

#区切り用の捨て改行
print()

#末尾に10月を追加
monthList.append("10月")

#要素の全出力
for i in monthList:
    print(i)

#区切り用の捨て改行
print()

#あえてinsertを使って、末尾に11月を追加
monthList.insert(7, "11月")

#要素の全出力
for i in monthList:
    print(i)
