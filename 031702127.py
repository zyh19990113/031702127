#!/usr/bin/python
# -*- coding: utf-8 -*-
# \d{11}��ʾʮһλ����  {n}��ʾǰ����ַ�����Ҫn����\d��ʾ����
import re
import json

customer = {
    '����': '',
    '�ֻ�': '',
    '��ַ': [],
}



s = input('')

op1 = s.split(r'!')
tag = op1[0]  # ��ȡ�Ѷȱ�ʶ


tel = re.findall(r'\d{11}', s)  # �ҳ�����
tel = tel[0]  # ������ת��Ϊ�ַ���
s = re.sub(r'\d{11}', '', s)  # ɾȥ����

num = re.sub(r',.*$', "", s)  # ��ȡ����

s = re.sub(num, '', s)  # ɾȥ����
s = re.sub(r',', '', s)  # ɾȥ����

customer['����'] = num
customer['�ֻ�'] = tel

# һ����ַ
director = ['����', '�Ϻ�', '���', '����']
if "������" in s:
    first = re.sub(r'������.*$', "", s)  # ��ȡ������
    first += '������'
    s = s.replace(first, '', 1)  # ɾȥ������
elif 'ʡ' not in s:
    for direc in director:
        if direc in s:
            first = direc
            break
        else:
            first = ""  # �ü���ַΪ��
else:
    first = re.sub(r'ʡ.*$', "", s)
    first += 'ʡ'
    s = s.replace(first, '', 1)  # ɾȥһ����ַ
customer['��ַ'].append(first)

# ����
two = ['��', '����', '��', '������']
for tw in two:
    if tw in s:

        second = re.sub(tw + '.*$', "", s)
        second += tw
        s = s.replace(second, '', 1)  # ɾȥ������ַ
        break
    else:
        second = ""

customer['��ַ'].append(second)

# ������ַ
county = ['��', '��', '��', '������', '��', '������', '����']
for tr in county:
    if tr in s:
        third = re.sub(tr + '.*$', "", s)
        third += tr
        s = s.replace(third, '', 1)  # ɾȥ������ַ
        break
    else:
        third = ""

customer['��ַ'].append(third)

# �ļ���ַ
town = ['�ֵ�', '��', '��', '������', '��ľ', '������ľ']
for fr in town:
    if fr in s:
        fouth = re.sub(fr + '.*$', "", s)
        fouth += fr
        s = s.replace(fouth, '', 1)  # ɾȥ�ļ���ַ
        break
    else:
        fouth = ""
customer['��ַ'].append(fouth)

s = s.replace('.', '', 1)  # ɾȥ���
# �弶��ַ
village = ['��', '·', '��']
if tag == '1':
    fifth = s
    customer['��ַ'].append(fifth)
elif tag == '2' or '3':  # ���������弶�Ժ�ĵ�ַ
    for fv in village:
        if fv in s:
            fifth = re.sub(fv + '.*$', "", s)
            fifth += fv
            customer['��ַ'].append(fifth)
            s = s.replace(fifth, '', 1)  # ɾȥ�弶��ַ
            break
        else:
            fifth = ""
    # ������ַ
    if '��' not in s:
        sixth = ""
    else:
        sixth = re.sub(r'��.*$', "", s)
        sixth += '��'
        s = s.replace(sixth, '', 1)  # ɾȥ������ַ

    customer['��ַ'].append(sixth)

    # �߼���ַ
    seventh = s
    customer['��ַ'].append(seventh)

json_str = json.dumps(customer, ensure_ascii=False)
print(json_str)