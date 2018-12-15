'''
Created on 2018/11/24

@author: onohdn

演習問題
単価と税率を入力し税込価格を求めるプログラムを作成しなさい。
※単価のデフォルト値は100、税率のデフォルト値は8とする
※結果は関数の呼び出し側で出力すること

期待結果
※単価、税率ともに未入力の場合
税込価格：108

※税率未入力の場合（単価は1000と入力）
1080

※単価未入力の場合（税率は10と入力）
110

※単価、税率ともに入力の場合（単価1000、税率10）
1100

'''

def priceCalc(price=100,tax=8):
    return int(price * (1 + (tax/100)))

p = input("単価を入力してください->")
t = input("税率（％）を入力してください->")

try:
    if len(p) == 0 and len(t) == 0: #両方未入力の場合
        print("税込価格：",priceCalc())
    elif len(t) == 0: #税率が未入力の場合
        print("税込価格：",priceCalc(price=int(p)))
    elif len(p) == 0: #単価が未入力の場合
        print("税込価格：",priceCalc(tax=int(t)))
    else: #両方入力の場合
        print("税込価格：",priceCalc(price=int(p),tax=int(t)))
except ValueError:
    print("数値以外を入力しないでください")
