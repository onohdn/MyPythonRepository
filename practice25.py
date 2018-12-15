'''
Created on 2018/12/9

@author: onohdn

演習問題
社員番号と社員名を入力し、インスタンスに保持後、出力するプログラムを作成しなさい.
※出力処理はメソッドを利用すること

期待結果
社員番号を入力してください->10
社員名を入力してください->sato
10
sato

'''

class Employee:
    def __init__(self,no,name):
        self.emp_no = no
        self.emp_name = name

    def show_detail(self):
        print(self.emp_no)
        print(self.emp_name)

emp = Employee(input("社員番号1を入力してください->"),input("社員名1を入力してください->"))

emp.show_detail()
