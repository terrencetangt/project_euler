#read text from a url
def read_url_txt(url):
    import urllib.request
    file = urllib.request.urlopen(url)
    s = ""
    for line in file:
    	s = s + line.decode()
    return s
