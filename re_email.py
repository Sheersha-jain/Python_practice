import re

string =  "purple alice-b@google.com monkey dishwasher"

match = re.search(r'\w+@\w+',string)
if match:
    print match.group()
else:
    print "Not Found"
