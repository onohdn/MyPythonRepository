'''
Created on 2018/11/24

@author: onohdn

演習問題
月の種類（"4月","5月","6月","7月","8月","9月"）をタプルで作成し、listに変換して表示する。その後、listから"6月"を
削除してタプルに変換して表示するプログラムを作成しなさい。

期待結果
months_list:["4月","5月","6月","7月","8月","9月"]
months_tuple:("4月","5月","7月","8月","9月")


'''
new_tuple = ("4月","5月","6月","7月","8月","9月")

#タプルをリストに変換して表示する
months_list = list(new_tuple)

print("months_list:",months_list)


#リストから"6月"を消す
del months_list[2]


#リストをタプルに変換して表示する
months_tuple = tuple(months_list)

print("months_tuple:",months_tuple)
