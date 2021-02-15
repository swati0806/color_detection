#!/usr/bin/env python
# coding: utf-8

# # IOT and COMPUTER VISION INTERN
# 
# # THE SPARKS FOUNDATION
# 
# 
# # TASK 2: COLOR DETECTION
# 
# 
# # Name: Swati Namdev

# In[1]:


import pandas as pd
import cv2


# In[2]:


img_path='colorpic.jpg'
csv_path='colors.csv'


# In[3]:


index=['color','color_name','hex','R','G','B']


# In[4]:


df=pd.read_csv(csv_path,names=index,header=None)


# In[5]:


img=cv2.imread(img_path)
img=cv2.resize(img,(800,600))


# In[6]:


clicked=False
r=g=b=ypos=0


# In[7]:


def get_color_name(R,G,B):
    minimum=1000
    for i in range(len(df)):
        d=abs(R-int(df.loc[i,'R']))+abs(G-int(df.loc[i,'G']))+abs(B-int(df.loc[i,'B']))
        if d<=minimum:
            minimum=d
            cname=df.loc[i,'color_name']
    return cname


# In[8]:


def draw(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global clicked,r,g,b,xpos,ypos
        clicked=True
        xpos=x
        ypos=y
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)


# In[ ]:


cv2.namedWindow('Image')
cv2.setMouseCallback('Image',draw)
while True:
    cv2.imshow('Image',img)
    if clicked:
        cv2.rectangle(img,(20,20),(600,60),(b,g,r),-1)
        text=get_color_name(r,g,b)+' R='+str(r)+' G='+str(g)+' B='+str(b)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if r+g+b>=600:
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
    if(cv2.waitKey(10) and 0xFF==27):
        break        
        


# In[ ]:




