#!/usr/bin/env python

# This is a simple cgi script to search for data sheets using google.
#
#

import json
import urllib2
import urllib
import cgi


    


def page_no_query():
    print "Content-Type: text/html"     # HTML is following
    print
    print '''
<html>
    <h1>SheetSearch: Simple Datasheet Search Engine</h1>
    <form name="input" method="get">
        <input type="text" name="q">
        <input type="submit" value="Search!">
    </form>
</html>
'''
    return

def page_query(query):
    print "Status: 302 Found"     # start redirect
    google_query = 'http://ajax.googleapis.com/ajax/services/search/web?q={0}&v=1.0'.format(query)
    failed_query = 'http://google.com/search?q={0}'.format(query)
    response = urllib2.urlopen(google_query)
    results = json.loads(response.read())
    for result in results['responseData']['results']:
        if 'fileFormat' in result and result['fileFormat'] == 'PDF/Adobe Acrobat':
            print "Location: {0}".format(result['url'])
            print
            return
    print 'Location: {0}'.format(failed_query)
    print

####START OF SCRIPT!

form = cgi.FieldStorage()

if 'q' not in form:
    # we were not asked for a query. 
    page_no_query()
else:
    page_query(urllib.quote_plus(form['q'].value))
