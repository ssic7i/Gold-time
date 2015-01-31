__author__ = 'sshejko'
# -*- coding: utf-8 -*-

import datetime

def get_gold_time():
    cur_time = datetime.datetime.now()
    month = int(cur_time.date().month)
    day = int(cur_time.date().day)
    if day == 24:
        day = 0
    if int(cur_time.date().day) > 24:
        new_time = datetime.datetime(year=cur_time.date().year, month=cur_time.date().month, day=cur_time.date().day, hour=month, minute=day)
    else:
        new_time = datetime.datetime(year=cur_time.date().year, month=cur_time.date().month, day=cur_time.date().day, hour=day, minute=month)
    return new_time

#print(datetime.datetime.now())
#print(get_gold_time())