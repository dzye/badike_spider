
#encoding:utf-8
#---------------------
import urllib2


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        try:    
        	response = urllib2.urlopen(url ,timeout=10)
	        if response.getcode() != 200:
	            return None
        	return  response.read()
    	except:
    		return None

