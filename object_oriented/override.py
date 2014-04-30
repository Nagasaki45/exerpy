import calendar


class MyTextCalendar(calendar.TextCalendar):

    def formatday(self, day, weekday, width):
        if day > 0 and ('7' in str(day) or day % 7 == 0):
            return ' *'
        return super(MyTextCalendar, self).formatday(day, weekday, width)


c = MyTextCalendar()
result = c.formatmonth(2014, 5)
print(result)

expected = '''      May 2014
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  *  8  9 10 11
12 13  * 15 16  * 18
19 20  * 22 23 24 25
26  *  * 29 30 31
'''
assert result == expected
