#!/usr/bin/env python

# This is a simple CGI script that simplifies searching for datasheets.
#
# See the README for more details
#
# GPLv2 license

import json
import urllib2
import urllib
import cgi


# Generates the basic webpage if no query is supplied. Provides a simple search box
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


# performs a google search for the requested search term, and
# redirects to the first page that provides a pdf, or to a google
# search page if the first page of results doesn't have any pdfs.
def page_query(query):
    print "Status: 302 Found"     # start redirect
    # the api query
    google_query = 'http://ajax.googleapis.com/ajax/services/search/web?q={0}&v=1.0'.format(query)
    # the search result webpage if we don't find any results
    failed_query = 'http://google.com/search?q={0}'.format(query)
    # perform the api query
    response = urllib2.urlopen(google_query)
    results = json.loads(response.read())
    # search through the json for a pdf page
    for result in results['responseData']['results']:
        if 'fileFormat' in result and result['fileFormat'] == 'PDF/Adobe Acrobat':
            # if we found it, print that pdf as the destination
            print "Location: {0}".format(result['url'])
            print
            return
    # Else, print the google search page as the source
    print 'Location: {0}'.format(failed_query)
    print

####START OF SCRIPT!

form = cgi.FieldStorage()

if 'q' not in form:
    # we were not asked for a query. 
    page_no_query()
else:
    page_query(urllib.quote_plus(form['q'].value))
