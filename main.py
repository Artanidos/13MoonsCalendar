import os
import datetime  
from weasyprint import HTML, CSS


moon_names = ["MAGNETIC", "LUNAR", "ELECTRIC", "SELF-EXISTING", "OVERTONE", "RHYTHMIC", "RESONANT", "GALACTIC", "SOLAR", "PLANETARY", "SPECTRAL", "CRYSTAL", "COSMIC"]

def moon(moon, year):
    startdate = datetime.date(year, 7, 26)
    start = startdate + datetime.timedelta(days= 28 * (moon - 1))
    html = "<h2>" + str(moon) + ". " + moon_names[moon - 1] + " MOON" + "</h2>"
    html += "<table class=\"moon\">\n"
    html += "<thead>\n"
    html += "<tr>\n"
    html += "<th width=\"70\">Dali (Fr)</th>\n"
    html += "<th width=\"70\">Seli (Sa)</th>\n"
    html += "<th width=\"70\">Gamma (So)</th>\n"
    html += "<th width=\"70\">Kali (Mo)</th>\n"
    html += "<th width=\"70\">Alpha (Di)</th>\n"
    html += "<th width=\"70\">Limi (Mi)</th>\n"
    html += "<th width=\"70\">Silio (Do)</th>\n"
    html += "</tr>\n"
    html += "</thead>\n"
    html += "<tbody>\n"
    html += "<tr>\n"
    for d in range(1,8):
        day = start + datetime.timedelta(days=d - 1)
        html += "<td><strong>" + str(d) +"</strong></br><small>" + day.strftime("%d.%m") + "</small></td>\n"
    
    html += "</tr>\n"
    html += "<tr>\n"
    for d in range(8,15):
        day = start + datetime.timedelta(days=d - 1)
        html += "<td><strong>" + str(d) +"</strong></br><small>" + day.strftime("%d.%m") + "</small></td>\n"
    
    html += "</tr>\n"
    html += "<tr>\n"
    for d in range(15,22):
        day = start + datetime.timedelta(days=d - 1)
        html += "<td><strong>" + str(d) +"</strong></br><small>" + day.strftime("%d.%m") + "</small></td>\n"

    html += "</tr>\n"
    html += "<tr>\n"
    for d in range(22,29):
        day = start + datetime.timedelta(days=d - 1)
        html += "<td><strong>" + str(d) +"</strong></br><small>" + day.strftime("%d.%m") + "</small></td>\n"

    html += "</tr>\n"
    html += "</tbody>\n"
    html += "</table>\n"
    return html

year = 2020
filename = "/media/art/data/SourceCode/13Moons/moons.pdf"
html = "<html>\n<head>\n"
html += "<link href=\"file:///media/art/data/SourceCode/13Moons/Creator/style.css\" rel=\"stylesheet\" type=\"text/css\"/>\n"
html += "</head>\n<body>\n"
html += "<p style=\"page-break-before: always\">"
html += "<h1>13 Moon Calendar of the year " + str(year - 2019) + "</br>(" + str(year)+ ")</h1>"
    
for m in range(1,14):
    html += moon(m, year)
html += "\n</body>\n</html>"
h = HTML(string=html)
css = CSS(string='@page { size: A5; margin: 0cm }')
h.write_pdf(filename, stylesheets=[css])


