def enumerate(sequence, start=0):
    n= start
    for element in sequence:
        yield n, element
        n += 1
a = ['hello','heii','hii','ping','yello']
enumerate(a, start=0)
