SheetSearch: The Simple Datasheet Search Engine
--------

Often when working on a new design, I find myself googling part
numbers, and immediately clicking on the datasheet.

SheetSearch speeds up this process by performing the google search for
you, and then redirecting you to the first pdf it finds.

It is implemented as a simple javascript bookmarklet. 

It is designed to be used as a  search engine in your browser.

INSTALLATION
-------------

To install in chrome, copy the contents of search.js into a new search engine, as per [this website](https://support.google.com/chrome/answer/95653?hl=en)

To install in firefox, you can simply drag [this link](javascript:function ss_cb(json) { var fail_url = json["responseData"]["cursor"]["moreResultsUrl"]; var results = json["responseData"]["results"]; for (var i = 0; i < results.length; i++) { var result = results[i]; if("fileFormat" in result) {  if(result["fileFormat"] == "PDF/Adobe Acrobat") { window.location = result["url"]; return;  } } } window.location = fail_url;}(function(){ var script = document.createElement('script'); query = '%s'; script.src = 'https://ajax.googleapis.com/ajax/services/search/web?q='+query +'&v=1.0&callback=ss_cb'; document.body.appendChild(script);})();) into your bookmarks folder.


