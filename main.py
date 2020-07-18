#############################################################################
# Copyright (C) 2020 Olaf Japp
#
# This file is part of 13MoonCalendar.
#
#  13MoonCalendar is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  13MoonCalendar is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with 13MoonCalendar.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

import os
import sys
import datetime  
import ephem
from weasyprint import HTML, CSS


moon_names = ["MAGNETIC", "LUNAR", "ELECTRIC", "SELF-EXISTING", "OVERTONE", "RHYTHMIC", "RESONANT", "GALACTIC", "SOLAR", "PLANETARY", "SPECTRAL", "CRYSTAL", "COSMIC"]

def get_moon_string(d, day, fullmoon):
    if day.year == fullmoon.year and day.month == fullmoon.month and day.day == fullmoon.day:
        return "<td><strong>" + str(d) +"</strong></br><small><strong>" + day.strftime("%d.%m") + "</strong></small></td>\n"
    else:
        return "<td><strong>" + str(d) +"</strong></br><small>" + day.strftime("%d.%m") + "</small></td>\n"

def moon(moon, year):
    startdate = datetime.date(year, 7, 26)
    start = startdate + datetime.timedelta(days= 28 * (moon - 1))
    fullmoon = ephem.next_full_moon(start).datetime()

    html = "<h2>" + str(moon) + ". " + moon_names[moon - 1] + " MOON" + "</h2>"
    html += "<table class=\"moon\">\n"
    html += "<thead>\n"
    html += "<tr>\n"
    html += "<th width=\"70\">Dali</th>\n"
    html += "<th width=\"70\">Seli</th>\n"
    html += "<th width=\"70\">Gamma</th>\n"
    html += "<th width=\"70\">Kali</th>\n"
    html += "<th width=\"70\">Alpha</th>\n"
    html += "<th width=\"70\">Limi</th>\n"
    html += "<th width=\"70\">Silio</th>\n"
    html += "</tr>\n"
    html += "</thead>\n"
    html += "<tbody>\n"
    html += "<tr>\n"
    for d in range(1,8):
        day = start + datetime.timedelta(days=d - 1)
        html += get_moon_string(d, day, fullmoon)
  
    html += "</tr>\n"
    html += "<tr>\n"
    for d in range(8,15):
        day = start + datetime.timedelta(days=d - 1)
        html += get_moon_string(d, day, fullmoon)
    
    html += "</tr>\n"
    html += "<tr>\n"
    for d in range(15,22):
        day = start + datetime.timedelta(days=d - 1)
        html += get_moon_string(d, day, fullmoon)

    html += "</tr>\n"
    html += "<tr>\n"
    for d in range(22,29):
        day = start + datetime.timedelta(days=d - 1)
        html += get_moon_string(d, day, fullmoon)

    html += "</tr>\n"
    html += "</tbody>\n"
    html += "</table>\n"
    return html


if __name__ == "__main__":
    year = 2020
    if len(sys.argv) == 2:
        year = int(sys.argv[1])

    #print(ephem.next_full_moon(datetime.date(year, 1, 1)))

    filename = "moons_" + str(year) + ".pdf"
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
