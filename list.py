#!/usr/bin/env python 

def main():
 colors()
# cartoon()

def colors():

 color = ['red' , 'yellow' , 'blue' , 'green' ]
 print color[0]
 print color[1]
 print len(color)
 color.append('mango')
 print color
 color.insert(1,'pineapple')
 print color
 color.insert(3,'hello')
 print color

#def public cartoon():
 cartoon = ['pokemon', 'digimon', 'doremon']
 
 color.extend(cartoon)
 print color

 color.index('pineapple')



if __name__ == '__main__':
    main()


