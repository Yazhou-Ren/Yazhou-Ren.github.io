# 第一步 去任老师的学术主页
# https://scholar.google.com/citations?user=M7Ocw0YAAAAJ&hl=zh-CN&oi=ao
# 保存该主页
import os
import re
file_name = 'pub.txt'
file_target_name = 'pubwithoutcitation.txt'
pattern1 = '                <td class="gsc_a_c">'
with open(file_name, 'r', encoding='utf-8') as f:
    text = f.readlines()
f_target = open(file_target_name, 'w', encoding="utf-8")
flag = 0
for line in text:
    if line.startswith(pattern1):
        flag = 2
    elif flag == 0:
        f_target.writelines(line)
    else:
        flag -= 1
