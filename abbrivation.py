#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:HenryLiu
# datetime:2019/9/14 下午 08:43
# Function:IEEE-transform


import pandas as pd
import re
import copy

# 固定格式期刊和会议的缩写生成 引用库
df = pd.DataFrame()
l = []
with open('123.txt', 'rb') as f:
    while True:
        s1 = f.readline()
        if not s1:
            break
        elif ('.' in str(s1)) and ('*' not in str(s1)):
            l.append(s1.decode('utf-8').strip())

l2 = []
with open('123.txt', 'rb') as f:
    while True:
        s1 = f.readline()
        if not s1:
            break
        elif (len(s1) > 7) and ('.' not in str(s1)):
            l2.append(s1.decode('utf-8').strip())

new = pd.DataFrame({'full': ['IEEE Computer Magazine', 'IEEE Concurrency', 'IEEE Expert', 'IEEE Micro Magazine',
                             'IEEE Potentials', 'IEEE Pulse', 'IEEE Security and Privacy'],
                    'abbr': ['IEEE Computer', 'IEEE Concurrency', 'IEEE Expert', 'IEEE Micro', 'IEEE Potentials',
                             'IEEE Pulse', 'IEEE Security Privacy']})

df['full'] = l2
df['abbr'] = l
df = df.append(new, ignore_index=True)

# 每一段选中
# with open('Ref.bib', 'r') as f:
#     s = f.read()
#     ref_position = [i.start() for i in re.finditer('@', s)]
#     # print(ref_position)
#     ref_position.append(len(s))
#     test = s[ref_position[0]:ref_position[1]]
#     print(test)
#

# 规定格式规则下的期刊和会议的缩写生成 引用库
df1 = pd.DataFrame()
l = []
with open('234.txt', 'rb') as f:
    while True:
        s1 = f.readline()
        if not s1:
            break
        elif ('.' in str(s1)):
            l.append(s1.decode('utf-8').strip())

l2 = []
with open('234.txt', 'rb') as f:
    while True:
        s1 = f.readline()
        if not s1:
            break
        elif ('.' not in str(s1)):
            l2.append(s1.decode('utf-8').strip().upper())
df1['full'] = l2
df1['abbr'] = l

# 读入文献库
with open('Ref.bib', 'r') as f:
    s = f.read()

# 改变journal的缩写
ref_list = re.findall('journal(.*?)\n', s, flags=re.IGNORECASE)
d = dict()
for item in range(len(ref_list)):
    journal_old = re.findall('{(.*?)}', ref_list[item])
    if not journal_old:
        journal_old = re.findall('"(.*?)"', ref_list[item])
    lookingfor = journal_old[0].strip()
    if df[df['full'] == lookingfor.upper()].empty:
        FUW = [i for i in lookingfor.split() if not i.islower()]
        for index, word in enumerate(FUW):
            if df1[df1['full'] == word.upper()].empty:
                pass
            else:
                FUW[index] = df1[df1['full'] == word.upper()].iloc[0, 1]
        print(' '.join(FUW))
        d[lookingfor] = ' '.join(FUW)
    else:
        print(df[df['full'] == lookingfor.upper()].iloc[0, 1])
        d[lookingfor.upper()] = df[df['full'] == lookingfor.upper()].iloc[0, 1]

# 文章名字中的大写字母组合两边加入大括号
ref_list = re.findall('title(.*?)\n', s, flags=re.IGNORECASE)
for item in range(len(ref_list)):
    stemp = copy.deepcopy(ref_list[item])
    journal_old = re.findall('{(.*?)}', ref_list[item])
    if not journal_old:
        journal_old = re.findall('"(.*?)"', ref_list[item])
    lookingfor = journal_old[0].strip()
    lookingfor = [re.sub('[^a-zA-Z]', '', i) for i in lookingfor.split() if i.isupper() and len(i) > 1]
    if lookingfor:
        for short in lookingfor:
            ref_list[item] = ref_list[item].replace(short, '{' + short + '}')

        d[stemp] = ref_list[item]

# 进行全局修改
for item in d:
    reg = re.compile(re.escape(item), re.IGNORECASE)
    s = reg.sub(d[item], s)

# 写入新的文献库
with open('new.bib', 'w') as f:
    f.write(s)
