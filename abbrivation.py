
# coding: utf-8

# In[38]:


import pandas as pd
import re


# In[2]:

df = pd.DataFrame()
l = []
with open('123.txt', 'rb') as f:
    while True:
        s1 = f.readline()
        if not s1:
            break
        elif ('.' in str(s1)) and ('*' not in str(s1)):
            l.append(s1.decode('utf-8').strip())

# In[3]:

df = pd.DataFrame()
l2 = []
with open('123.txt', 'rb') as f:
    while True:
        s1 = f.readline()
        if not s1:
            break
        elif (len(s1)>7) and ('.' not in str(s1)):
            l2.append(s1.decode('utf-8').strip())
# l2           


# In[4]:


len(l), len(l2)
new = pd.DataFrame({'full':['IEEE Computer Magazine', 'IEEE Concurrency','IEEE Expert','IEEE Micro Magazine','IEEE Potentials','IEEE Pulse','IEEE Security and Privacy'], 'abbr':['IEEE Computer','IEEE Concurrency','IEEE Expert','IEEE Micro','IEEE Potentials','IEEE Pulse','IEEE Security Privacy']})
new


# In[ ]:


df['full'] = l2
df['abbr'] = l
df = df.append(new, ignore_index=True)
# df.to_csv('1.csv', index=None)


# In[35]:


result = df[df['full'] == 'IEEE RFIC JOURNAL'].iloc[0,1]
result


# In[86]:

# 每一段选中
# with open('Ref.bib', 'r') as f:
#     s = f.read()
#     ref_position = [i.start() for i in re.finditer('@', s)]
#     # print(ref_position)
#     ref_position.append(len(s))
#     test = s[ref_position[0]:ref_position[1]]
#     print(test)
#


# In[136]:
with open('Ref.bib', 'r') as f:
    s = f.read()
    # ref_list = re.findall('journal(.*?)\n', s)
    # for item in range(len(ref_list)):
    #     journal_old = re.findall('{(.*?)}', ref_list[item])
    #     if not journal_old:
    #         journal_old = re.findall('"(.*?)"', ref_list[item])
    #     lookingfor = journal_old[0].strip()
    #     print(lookingfor)


# In[ ]:


    ref_list = re.findall('journal(.*?)\n', s)
    d = dict()
    for item in range(len(ref_list)):
        journal_old = re.findall('{(.*?)}', ref_list[item])
        if not journal_old:
            journal_old = re.findall('"(.*?)"', ref_list[item])
        lookingfor = journal_old[0].strip()
        if df[df['full'] == lookingfor.upper()].empty:
            print('未找到匹配项')
        else:
            print(df[df['full'] == lookingfor.upper()].iloc[0,1])
            d[lookingfor.upper()] = df[df['full'] == lookingfor.upper()].iloc[0,1]


# In[160]:


for item in d:
    # print(item)
    reg = re.compile(re.escape(item), re.IGNORECASE)
    s = reg.sub(d[item], s)
with open('new.bib', 'w') as f:
    f.write(s)

