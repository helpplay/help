#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s1 =int(input('请输入您去年成绩：'))
s2 =int(input('请输入您本次成绩：'))
r = ((s2-s1)/s1)*100
if r>0:
    print ('您本次成绩为',s2,'去年成绩为',s1,'比去年提升了%.1f %%'% r)
else:
    print('您本次成绩为',s2,'去年成绩为',s1,'比去年下降了%.1f %%'% r)
