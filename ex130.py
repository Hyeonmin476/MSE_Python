#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests #request를 불러옴
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data'] #bct에 비트코인 정보를 가져옴

변동폭 = float(btc['max_price']) - float(btc['min_price']) #float는 빼기가 가능하도록 실수타입으로 바꾸어줌
시가 = float(btc['opening_price']) #bct에 있는 'opening_price'의 값을 실수로 바꿈
최고가 = float(btc['max_price'])   #bct에 있는'max_price'의 값을 실수로 바꿈

if (시가+변동폭) > 최고가:  #조건 설정 참이면 print("상승장") 거짓이면  print("하락장")
    print("상승장") #실행되면 상승장을 출력
else:
    print("하락장") #실행되면 하락장을 출력


# In[ ]:





# In[ ]:




