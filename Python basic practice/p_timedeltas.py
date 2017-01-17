from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

#construct a basic timedelta and print it
print timedelta(days = 365, hours=5, minutes=1)

#print today's date
print "today is : "+ str(datetime.now())

#print today's date one year from now
print "one year from now it will be: "+ str(datetime.now() + timedelta(days=365))

#create a timedelta that uses more than one argument
print "in two weeks and 3 days it will be : " + str(datetime.now() + timedelta(weeks=2, days=3))