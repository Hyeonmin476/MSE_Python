#!/usr/bin/env python
# coding: utf-8

# In[25]:


class Account:  #account의 class함수 생성
    # class variable
    account_count = 0

    def __init__(self, name, balance): #인자 생성
        self.deposit_count = 0
        self.deposit_log = []   #self.deposit_log란 이름의 빈 리스트 생성
        self.withdraw_log = [] #self.withdraw_log란 이름의 빈리스트 생성

        self.name = name     #인자 정의
        self.balance = balance #인자 정의


    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  

    def deposit(self, amount):  #deposit이란 함수를 생성
        if amount >= 1:      #deposit이란 함수에서 받은 amount 값이 1보다 크거나 같으면 
            self.deposit_log.append(amount) # self.deposit_log에 받은 값을 대입
        
    def withdraw(self, amount):  #withdraw이란 함수를 생성
        if self.balance > amount:  #blance의 값이 amount 값보다 크면
            self.withdraw_log.append(amount) #  self.withdraw_log에 amount 값을 저장

    def withdraw_history(self): # withdraw_history란 함수 생성
        for amount in self.withdraw_log: #amount의 값은 self.withdraw_log을 차례로 1개씩 가진다
            print('출금',amount) #출금과 아까의 amount값을 출력

    def deposit_history(self):  #def deposit_history란 함수 생성
        for amount in self.deposit_log: #amount의 값은 self.deposit_log을 차례로 1개씩 가진다
            print('입금',amount)  #입금과 아까의 amount값을 출력


k = Account("Kim", 1000)
k.deposit(100)    #deposit이란 함수를 실행,  amount=100
k.deposit(200)    #deposit이란 함수를 실행, amount=200
k.deposit(300)    #deposit이란 함수를 실행,  amount=300 
k.deposit_history()  #def deposit_history란 함수 실행

k.withdraw(100)    #withdraw이란 함수를 실행, amount=100
k.withdraw(200)    #withdraw이란 함수를 실행, amount=200
k.withdraw_history()  # withdraw_history란 함수 실행


# In[ ]:




