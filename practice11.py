'''
Created on 2018/11/11

@author: onohdn

演習問題
月の種類（"4月","5月","6月","7月","8月","9月"）をタプルで作成し、更新と削除の動作を確認しなさい。

期待結果
更新も削除もTypeErrorになる。タプルは要素の更新、削除が不可能な型である。


'''
monthList = ("4月","5月","6月","7月","8月","9月")

#更新するか削除するかを聞く
ans = input("タプルを更新する場合は1を、削除する場合は2を入力してください-->")

#回答に応じて、タプルの更新か削除を実施する
if ans == "1":
    monthList[1] = "12月"
else:
    del monthList[1]
