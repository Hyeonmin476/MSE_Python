#!/usr/bin/env python
# coding: utf-8

# In[15]:


def 함수2(num) :  #함수2가 호출되면 지정된 행위를 한다
    num = num + 10  #num값에 10을 더한다 
    return 함수1(num) #함수1에 변한 num값을 넣어 호출 num=12

def 함수1(num) :  #함수1가 호출되면 지정된 행위를 한다
    return 함수0(num + 2) #받은 num값에 2를 더하고 함수0을 호출 num=14

def 함수0(num) :  #함수0가 호출되면 지정된 행위를 한다
    return num * 2 #받은 num값에 곱하기2를 한다  num=28


c = 함수2(2) #함수2의 num값에 2대입
print(c) # 함수2,1,0이 실행된 결과를 출력


# In[ ]:




