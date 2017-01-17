# exmaple file for working with date in python

from datetime import date
from datetime import time
from datetime import datetime

def main():
    ##date objects
    # get today's date from the simple today() method from the date class
    today = date.today()
    print "Today's date is ", today

    #print out the date's indivadule components
    print "Today's date is ", today.day, today.month, today.year

    #retrive today's weekday (0=Monday, 6=Sunday)
    print "Today's weekday #: ", today.weekday()

    ##datetime class
    today = datetime.now()
    print "The current time is ", today

    # get the current time
    t = datetime.time(datetime.now())
    print "The current time is ", t

if __name__=="__main__":
    main()