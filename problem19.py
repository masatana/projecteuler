# -*- coding: utf-8 -*-

first_day_list = [0]

for year in range(1900, 2001):
    if year % 4 == 0:
        if year % 400 == 0:
            is_leap = True
        elif year % 100 == 0:
            is_leap = False
        else:
            is_leap = True
    else:
        is_leap = False
    
    for month in range(1, 13):
        last_month_first = first_day_list[-1]
        if month == 2 and is_leap:
            first_day_list.append(last_month_first + 29)
        elif month == 2:
            first_day_list.append(last_month_first + 28)
        elif month in [9, 4, 6, 11]:
            first_day_list.append(last_month_first + 30)
        else:
            first_day_list.append(last_month_first + 31)
print len([x for x in first_day_list if x % 7 == 6]) - len([x for x in first_day_list if x % 7 == 6 and x < 364])
