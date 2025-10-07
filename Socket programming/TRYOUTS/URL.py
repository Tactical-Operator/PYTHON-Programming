import urllib.parse
url=input("URL\n")
tpl=urllib.parse.urlparse(url)
print(tpl)
input("")