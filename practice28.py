'''
Created on 2018/12/9

@author: onohdn

演習問題
カードのポイントと換算率を入力し、ポイントの計算を行うプログラムを作成しなさい。
このとき、インスタンスの内容には影響がないことも確認しなさい。

期待結果
カード所有者名を入力してください->sato
sato
0
計算したいポイント数を入力してください->200
計算したい倍率を入力してください->3
600

インスタンスの内容に影響がないことの確認
sato
0

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

    @staticmethod
    def calc_point(point,rate):
        return rate * point

user = Card(input("カード所有者名を入力してください->"))
user.show_detail()

print(Card.calc_point(int(input("計算したいポイント数を入力してください->")),int(input("計算したい倍率を入力してください->"))))

print("インスタンスの内容に影響がないことの確認")
user.show_detail()