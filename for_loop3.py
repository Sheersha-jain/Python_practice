#!/usr/bin/python

fruits = ['a', 'b', 'c']

for index in range(len(fruits)):
    print fruits[index]


for num in range(10,20):
    if num == 3:
        print num 

else:
    print "there is no number"


def new_function(str):
    "function doc string"
    print str
    return;

new_function("helloo all my first function")


def number(x,y):

    if x > y:
        return x
        print x
    else:
        return y
        print y

number(5,6)


def changename(mylist):
    "this changes apply"
    mylist.append([1234]);
    print mylist
    return 

mylist = [56,78]
changename( mylist )

def foo (x,y):
    def bar(z):
        return z*2
    return bar(x) + y 


def found (x=3) :
    print x
found()

def name1(a,b,c):
    print a,b,c
name1(c=399,b=98,a=45)
