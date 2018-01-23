a = 5
def f(a, l=None):
    if l is None:
        l=[]
    l.append(a)
    print l

f(1)
