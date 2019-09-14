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





未来版本预计：

1.0 本版本，实现一键全改变

2.0 逐个推荐改变，手动选择是否进行修改

3.0 利用词向量在未找到的匹配项的情况下推荐最相近的，并且手动选择是否进行修改

4.0 通过这么多信息，利用算法匹配缩写的规矩进行匹配，得到通过规则生成的合理的缩写规则生成结果，然后在手动修改中给出合理的建议，是否进行改变。