# example of retrieving data from the internet

import urllib2
import json

def urlMethod():
  # open a connection to a URL using urllib2
  webUrl = urllib2.urlopen("http://joemarini.com")
  
  # get the result code and print it
  print "result code: " + str(webUrl.getcode())
  
  # read the data from the URL and print it
  data = webUrl.read()
  print data

def printResults(data):
    # use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # now we can access the contents of the json like any other Python object
    if "title" in theJSON["metadata"]:
        print theJSON["metadata"]["title"]

    # output the number of events, plus the magnitude and each event name 
    count = theJSON["metadata"]["count"]
    print str(count) + " events recorded"

  # for each event, print the place where it occurred
    for i in theJSON["features"]:
        print (i["properties"]["place"])

  # print the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
             print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"])

  # print only the events where at least 1 person reported feeling something
    print ("Events that were felt: ")
    for i in theJSON["features"]:
          feltReports = i["properties"]["felt"]
          if (feltReports != None):
             if (feltReports > 0):
                   print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times")

def jsonMethod():
    # define variable to hold the source URL
    # in this case we'll use the free data feed from the USGS
    # this feed lists all earthquakes for the last day larger than man 2.5

    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    #open the URL and read the data
    webUrl = urllib2.urlopen(urlData)
    print webUrl.getcode()
    if(webUrl.getcode() == 200):
        data=webUrl.read()
        # print out our customized results
        printResults(data)
    else:
        print "Received an error from server, cannot retrievve results" + str(webUrl.getcode())
# urlMethod()
jsonMethod()