#!/usr/bin/env python
# coding: utf-8

# In[44]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []  #리스트로 저장하기위해 리스트 생성
for i in range(len(low_prices)) :  #for루프 사용해 반복샐행, range,len을 사용해 원소의 개수대로 루프
     volatility.append(high_prices[i] - low_prices[i])  #변동값 측정(i는 0,1,2...으로 같은 순서의 값을 가져옴)
print(volatility) #변동값 출력


# In[ ]:




