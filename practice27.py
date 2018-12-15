'''
Created on 2018/12/9

@author: onohdn

演習問題
演習26にポイントの倍率を入力したカード情報を表示するクラスメソッドを追加したプログラムを作成しなさい。
入力したポイントの倍率とポイントを入力した場合、現在のポイントに加算した合計ポイントを出力しなさい。
※ポイントの加算処理はメソッドを利用すること。
※倍率を設定するメソッドはクラスメソッドを使用すること。

期待結果
カード所有者名を入力してください->sato
追加ポイントを入力してください->1000
ポイントの倍率を入力してください->4
sato
1000
現在のポイント：4000

'''

class Card:
    rate = 1

    @classmethod
    def set_rate(cls,rate):
        cls.rate = rate

    def __init__(self,name):
        self.user_name = name
        self.point = 0

    def show_detail(self):
        print(self.user_name)
        print(self.point)

    def add_point(self,point):
        self.point += point

    def point_to_cash(self):
        print("現在のポイント：",self.point * self.rate)

user = Card(input("カード所有者名を入力してください->"))
user.add_point(int(input("追加ポイントを入力してください->")))
Card.set_rate(int(input("ポイントの倍率を入力してください->")))

user.show_detail()
user.point_to_cash()
