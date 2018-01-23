"""
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
"""


import re

names = []
def extract_names(filename):
      f = open(filename, 'rU')
      text = f.read()

      year_match = re.match(r'Popularity\sin\s(\d\d\d\d)',text)
      if not year_match:
          print "We did not find year"
      else:
          year = year_match.group(1)
          names.append(year)


