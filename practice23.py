'''
Created on 2018/12/9

@author: onohdn

演習問題
社員番号と社員名を入力し、インスタンスに保持後、出力するプログラムを作成しなさい。

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

emp = Employee(input("社員番号を入力してください->"),input("社員名を入力してください->"))

print(emp.emp_no)
print(emp.emp_name)
