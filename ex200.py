#!/usr/bin/env python
# coding: utf-8

# In[47]:


ohlc = [["open", "high", "low", "close"],
         예시로 [100, 110, 70, 100]이고 ,
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
수익금 = 0
for row in ohlc[1:]:   #ohlc의 값을 [1:]을 통해 문자를 생략, for문을 사용하여 ohlc값을 분해
    수익금 += (row[3] - row[0]) #row값은 예시로 [100, 110, 70, 100]이고 row[3]은 마지막 값 row[0]은 첫번째값 +=을 사용해 총합을 구함
print(수익금) #for문에서 구한 수익금을 출력


# In[ ]:




