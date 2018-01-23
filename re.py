import re
string = "an example word:cat!!"

match = re.search(r'word:\w\w\w', string)
if match:
    print "found", match.group()
else :
    print "did not found"

