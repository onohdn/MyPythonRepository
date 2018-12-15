'''
Created on 2018/12/9

@author: onohdn

演習問題
カードの所有者名を入力し、現在のポイントを出力するプログラムを作成しなさい。
追加ポイントを入力した場合、現在のポイントに加算した合計ポイントを出力しなさい。
※ポイントの加算処理はメソッドを利用すること。

期待結果
カード所有者名を入力してください->sato
sato
0
追加ポイントを入力してください->1000
sato
1000

'''

class Card:
    def __init__(self,name):
        self.user_name = name
        self.point = 0

    def show_detail(self):
        print(self.user_name)
        print(self.point)

    def add_point(self,point):
        self.point += point

user = Card(input("カード所有者名を入力してください->"))
user.show_detail()

user.add_point(int(input("追加ポイントを入力してください->")))
user.show_detail()
