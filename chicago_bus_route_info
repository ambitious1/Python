import urllib.request

u=urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data=u.read()
f=open('rt22.xml','wb')
f.write(data)
f.close()
input("Press <ENTER> to continue...")
