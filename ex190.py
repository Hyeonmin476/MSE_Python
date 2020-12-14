#!/usr/bin/env python
# coding: utf-8

# In[45]:


apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart: #for루프 [101, 102]/  [201, 202]/  [301, 302]가 row의 값이 된다.
    for col in row: #or루프로 예를들어 i는 루프가 101,102의 값을 갖고 루프는 끝난다
        print(col, "호") # col의 값과 호를 출력한다.
print("-" * 5)  #------를 출력(for루프 관련 없다)


# In[ ]:




