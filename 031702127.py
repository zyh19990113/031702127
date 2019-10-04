#!/usr/bin/python
# -*- coding: utf-8 -*-
# \d{11}表示十一位数字  {n}表示前面的字符还需要n个；\d表示数字
import re
import json

customer = {
    '姓名': '',
    '手机': '',
    '地址': [],
}



s = input('')

op1 = s.split(r'!')
tag = op1[0]  # 提取难度标识


tel = re.findall(r'\d{11}', s)  # 找出号码
tel = tel[0]  # 将号码转化为字符串
s = re.sub(r'\d{11}', '', s)  # 删去号码

num = re.sub(r',.*$', "", s)  # 提取人名

s = re.sub(num, '', s)  # 删去人名
s = re.sub(r',', '', s)  # 删去逗号

customer['姓名'] = num
customer['手机'] = tel

# 一级地址
director = ['北京', '上海', '天津', '重庆']
if "自治区" in s:
    first = re.sub(r'自治区.*$', "", s)  # 提取自治区
    first += '自治区'
    s = s.replace(first, '', 1)  # 删去自治区
elif '省' not in s:
    for direc in director:
        if direc in s:
            first = direc
            break
        else:
            first = ""  # 该级地址为空
else:
    first = re.sub(r'省.*$', "", s)
    first += '省'
    s = s.replace(first, '', 1)  # 删去一级地址
customer['地址'].append(first)

# 二级
two = ['市', '地区', '盟', '自治州']
for tw in two:
    if tw in s:

        second = re.sub(tw + '.*$', "", s)
        second += tw
        s = s.replace(second, '', 1)  # 删去二级地址
        break
    else:
        second = ""

customer['地址'].append(second)

# 三级地址
county = ['区', '县', '市', '自治县', '旗', '自治旗', '林区']
for tr in county:
    if tr in s:
        third = re.sub(tr + '.*$', "", s)
        third += tr
        s = s.replace(third, '', 1)  # 删去三级地址
        break
    else:
        third = ""

customer['地址'].append(third)

# 四级地址
town = ['街道', '镇', '乡', '民族乡', '苏木', '民族苏木']
for fr in town:
    if fr in s:
        fouth = re.sub(fr + '.*$', "", s)
        fouth += fr
        s = s.replace(fouth, '', 1)  # 删去四级地址
        break
    else:
        fouth = ""
customer['地址'].append(fouth)

s = s.replace('.', '', 1)  # 删去句号
# 五级地址
village = ['街', '路', '村']
if tag == '1':
    fifth = s
    customer['地址'].append(fifth)
elif tag == '2' or '3':  # 继续划分五级以后的地址
    for fv in village:
        if fv in s:
            fifth = re.sub(fv + '.*$', "", s)
            fifth += fv
            customer['地址'].append(fifth)
            s = s.replace(fifth, '', 1)  # 删去五级地址
            break
        else:
            fifth = ""
    # 六级地址
    if '号' not in s:
        sixth = ""
    else:
        sixth = re.sub(r'号.*$', "", s)
        sixth += '号'
        s = s.replace(sixth, '', 1)  # 删去六级地址

    customer['地址'].append(sixth)

    # 七级地址
    seventh = s
    customer['地址'].append(seventh)

json_str = json.dumps(customer, ensure_ascii=False)
print(json_str)