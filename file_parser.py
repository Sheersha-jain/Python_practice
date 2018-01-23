"""
Parser to parse content written in file. 
"""

import re
content = """ COMMAND> du -sh /var/lib/pgsql

635M    /var/lib/pgsql

 """.strip()

s= re.findall(r'(\d+\w)(\s....+)',content)
print s

