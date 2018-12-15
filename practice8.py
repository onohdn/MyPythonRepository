'''
Created on 2018/10/28

@author: onohdn

演習問題
月の種類（"4月","5月","6月","7月","8月","9月"）を降順に並び替え、2番目に大きい月名を出力するプログラムを作成しなさい。

期待結果
8月

'''
monthList = ["4月","5月","6月","7月","8月","9月"]

#並び替え結果を返す関数を使う場合
sorteList = sorted(monthList,reverse = True)
print(sorteList[1])

#区切り用の捨て改行
print()

#リスト自身を並び替える場合
monthList.sort(reverse = True)
print(monthList[1])