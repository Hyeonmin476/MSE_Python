#!/usr/bin/env python
# coding: utf-8

# In[43]:


class Stock:  #stock이라는 클래스 생성
    def __init__(self, name, code, per, pbr, dividend):  #stock이라는 클래스 생성
        self.name = name #인자 정의  
        self.code = code #인자 정의  
        self.per = per  #인자 정의  
        self.pbr = pbr  #인자 정의  
        self.dividend = dividend  #인자 정의  

종목 = []  #빈 리스트 생성

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83) 
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27) 
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37) 

종목.append(삼성)    #종목에 삼성의 값을 넣음
종목.append(현대차)  #종목에 현대차의 값을 넣음
종목.append(LG전자)  #LG전자의 값을 넣음

for i in 종목: #for문을 사용해 i는 삼성/ 현대차/ LG전자의 값을 차래로 가짐
    print(i.code, i.per)  # stock에 정의된 값을 출력


# In[ ]:




