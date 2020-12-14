#!/usr/bin/env python
# coding: utf-8

# In[5]:


def message1(): #함수 정의 message1()이 나오면  A 출력
    print("A")

def message2():   #함수 정의 message2()이 나오면  B 출력
    print("B")

def message3():  #함수 정의 message3()이 나오면  for문 실행
    for i in range (3) :  # i는 0,1,2이므로 3번 반복되는 for문 
        message2() #함수에의해 B출력 
        print("C") #C를 출력   (for문 끝나고 반복시킴)
    message1() #for문이 끝나면 함수에의해 A출력

message3()


# In[ ]:




