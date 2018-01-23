import re

pattern = "Joke: what do you call a pig with three eyes? piiig!"

match = re.search(r'p\w\w\w\g',pattern)
if match:
    print "FOund", match.group()
else:
    print "not found"
