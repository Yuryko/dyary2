#!/usr/bin/env python
# -*- coding: utf-8 -*-
# скрипт для парсинга файлов org.mode
with open('dyary4.org') as file_in:
    text = file_in.read()

text = text.replace(" вс", " воскресенье")
text = text.replace(" сб", " суббота")
text = text.replace(" пт", " пятница")
text = text.replace(" чт", " четверг")
text = text.replace(" ср", " среда")
text = text.replace(" вт", " вторник")
text = text.replace(" пн", " понедельник")

with open('dyary4.txt', "w") as file_out:
    file_out.write(text)
    print (u'Все нормально')




