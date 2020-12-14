#!/usr/bin/env python
# coding: utf-8

# In[28]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for a in 리스트:  #for을 이용해 원소 한개씩 대입
    if a.endswith(('.h' , 'c')): i#f를 이용해 참거짓을 판별, endswith를 이용해 끝이 .h,.c인 것만 참 나머지는 거짓
                  print(a) #if가 참일때 그값을 출력


# In[ ]:




