#!/usr/bin/env python
# coding: utf-8

# In[3]:


class 부모: # 부모 class 생성
   def __init__(self): #인자 만듬
       print("부모생성") #부모생성을 출력

class 자식(부모):  #자식이라는 class생성
   def __init__(self):   #인자 생성 
       print("자식생성")  # 자식생성을 출력
       super().__init__()  #부모class 실행

나 = 자식()  #class 자식 실행


# In[ ]:




