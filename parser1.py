data = """
COMMAND> du -sh /var/lib/pgsql

635M    /var/lib/pgsql
""".strip()

#for line in data:
#    if line.startswith('COMMAND>'):
#        print line
#    else:
#        print "no output"
#


for line in data:
    if "COMMAND>" in data:
        line_split = line.split()
        print line_split
        print "hellloo"
    else:
        print "no hello"

