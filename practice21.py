'''
Created on 2018/11/25

@author: onohdn

演習問題
大人の人数と子供の人数を入力し、それぞれの料金を表示させるプログラムを作成しなさい。
大人の料金は１人当たり1,000円、子供料金は１人当たり800円とする。

期待結果
大人の人数を入力してください->3
子供の人数を入力してください->2
大人料金合計：3000
子供料金合計：1600

'''

def setPrice(price):
    def getPrice(num):
        return price*num
    return getPrice

adultNum = int(input("大人の人数を入力してください->"))
childNum = int(input("子供の人数を入力してください->"))

adultPrice = setPrice(1000)
childPrice = setPrice(800)

print("大人料金合計：",adultPrice(adultNum))
print("子供料金合計：",childPrice(childNum))

