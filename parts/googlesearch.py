import urllib2
import re




def getusername(handle):
    raw_data = urllib2.urlopen("https://twitter.com/search?q=%40" + handle).read()
    scripted_html = re.split(">",re.split('ProfileNameTruncated-link u-textInheritColor js-nav js-action-profile-name',raw_data)[1])
    untrimmed_name = re.split("<",scripted_html[1])
    trimmed_name = re.split("\n",untrimmed_name[0])
    print trimmed_name[1].strip()
    
getusername('RWitherspoon')