#!/usr/bin/env python
# coding: utf-8

# In[ ]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")  #input을 사용하여 값을 받음
if user in fruit.values():   #input을 이용해 받은 값이 fruit의 valuer값에따라 참거짓 판별.
    print("정답입니다.") #값이 있을 경우 정답입니다 출력
else: #거짓일때
    print("오답입니다.") #값이 없을 경우 오답입니다 출력


# In[ ]:




