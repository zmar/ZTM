# http://www.dabeaz.com/pydata/
# https://api.um.warszawa.pl/index.php#

# Dave's office

daves_latitude = 41.98062
daves_longitude = 87.668452

import urllib
u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data=u.read()
f=open('rt22.xml', 'wb')
f.write(data)
f.close()
from xml.etree.ElementTree import parse
doc=parse('rt22.xml')
for bus in doc.findall('bus'):
    id_bus = bus.findtext("pid")
    d=bus.findtext('d')
    lat=float(bus.findtext('lat'))
    if  d == 'North Bound':
        print id_bus , d, lat
import webbrowser
# webbrowser.open('https://developers.google.com/maps/documentation/static-maps/')
# http://www.dabeaz.com/pydata
