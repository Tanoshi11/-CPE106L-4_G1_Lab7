from urllib.request import urlopen

html = urlopen("http://pythonscraping.com/pages/page1.html")
# html = urlopen('https://www.mapua.edu.ph/')
print(html.read())