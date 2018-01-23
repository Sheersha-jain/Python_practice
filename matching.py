#!usr/bin/python

import re
match = re.search(r'iii','piiiiiig') => found, match.group() == "iii"
match = re.search(r'iii' , 'piiiiig') => not found, match == None  



