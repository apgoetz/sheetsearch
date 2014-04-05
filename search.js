javascript:function ss_cb(json) {
    var fail_url = json["responseData"]["cursor"]["moreResultsUrl"];
    var results = json["responseData"]["results"];
    for (var i = 0; i < results.length; i++) {
	var result = results[i];
	if("fileFormat" in result) {
	    if(result["fileFormat"] == "PDF/Adobe Acrobat") {
		window.location = result["url"];
		return;
	    }
	}
    }
    window.location = fail_url;
}
(function(){
    var script = document.createElement('script');
    query = '%s';
    script.src = 'https://ajax.googleapis.com/ajax/services/search/web?q='+query
	+'&v=1.0&callback=ss_cb';
    document.body.appendChild(script);
})();
