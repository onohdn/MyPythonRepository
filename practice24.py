'''
Created on 2018/12/9

@author: onohdn

演習問題
複数の社員番号と社員名を入力し、それぞれ複数のインスタンスに保持後、出力するプログラムを作成しなさい。

期待結果
社員番号1を入力してください->200
社員名1を入力してください->kato
社員番号2を入力してください->300
社員名2を入力してください->iwai
200
kato
300
iwai

'''

class Employee:
    def __init__(self,no,name):
        self.emp_no = no
        self.emp_name = name

emp1 = Employee(input("社員番号1を入力してください->"),input("社員名1を入力してください->"))
emp2 = Employee(input("社員番号2を入力してください->"),input("社員名2を入力してください->"))

print(emp1.emp_no)
print(emp1.emp_name)

print(emp2.emp_no)
print(emp2.emp_name)
