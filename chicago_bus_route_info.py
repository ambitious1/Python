import urllib.request

u=urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data=u.read()
f=open('rt22.xml','wb')
f.write(data)
f.close()
input("Press <ENTER> to continue...")



'''
This uses Chicago public transportation website, and gives a live representation of when a specific bus on a specified route, arrives at each stop. The web page is analyzed as an XML document in which I extract the information I need, and write the data to an XML document. 
Utilizing urllib.request module and file handling.
'''
