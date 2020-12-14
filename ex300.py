#!/usr/bin/env python
# coding: utf-8

# In[46]:


per = ["10.31", "", "8.00"] # 10.31/8 은 정상적으로 실행 ""은 실행 안됨 

for i in per: #i는 10.31/ /8의 값을 갖는다
    try: #실행될때 print(float(i))를 실행
        print(float(i)) #i의 값을 출력
    except: #실행 안될때 print(0)를 실행
        print(0) #0을 출력 print("clean data") 실행
    else: #예외 없을 때
         print("clean data") #clean data 출력
    finally: #항상 실행됨, print("변환 완료") 시행
          print("변환 완료") #변환 완료 출력


# In[ ]:




