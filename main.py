#!/usr/bin/env python
# -*- coding: utf-8 -*-
# скрипт для парсинга файлов org.mode
import re

#regex1=r" вс"
with open('dyary4.org') as file_in:
    text = file_in.read()

#matches = re.finditer(regex, text)

text = re.sub(
    r'\b вс',
    r' воскресенье',
    text
)

text = re.sub(
    r'\b сб',
    r' сбуббота',
    text
)

text = re.sub(
    r'\b пт',
    r' пятница',
    text
)
text = re.sub(
    r'\b чт',
    r' четверг',
    text
)
text = re.sub(
    r'\b ср',
    r' среда',
    text
)
text = re.sub(
    r'\b вт',
    r' вторник',
    text
)
text = re.sub(
    r'\b пн',
    r' понедельник',
    text
)

with open('dyary4.txt', "w") as file_out:
    file_out.write(text)
    print (u'Все нормально')




