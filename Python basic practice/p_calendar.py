import calendar

#create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2013, 1, 0, 0)
print str

#create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2013, 1)
print str

#loop oer the days of a month
#zeroes means that the day of the week is in an overlapping month
for i in c.itermonthdays(2013, 8):
    print i