本程序主要是为了替换LATEX引用中的IEEE期刊和会议的名称缩写问题，123.txt是从IEEE_style_manual.pdf中得到的规则。将程序和对应的Ref.bib放入同一文件夹下，在已经安装Python3环境后可以运行程序，随后会得到生成的new.bib， 如果有未匹配正确的可以手动进行修改，或者加入123.txt中作为新规则，规则为在最后加入新的两行，一行为原始的名称（不区分大小写，如IEEE TRANSACTIONS ON AEROSPACE AND ELECTRONIC SYSTEMS），另起一行输入新的名称（区分大小写，如IEEE Trans. Aerosp. Electron. Syst.）

```python
IEEE TRANSACTIONS ON AEROSPACE AND ELECTRONIC SYSTEMS
IEEE Trans. Aerosp. Electron. Syst.
```

随后在cmd中运行

```python
python abbrivation.py
```

得到结果