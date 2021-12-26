#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import calendar
weekdays = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
m,d,y=map(int,input().split())
a=calender.weekday(y,m,d)
print(weekdays[a])

