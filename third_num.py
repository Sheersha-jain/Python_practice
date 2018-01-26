sample = [1,2,3,4,5,6,7,8,9]

#for i, num in enumerate(sample):
#    print "i",i
#    print "num",num
#    if num%3==0:
#        


new_list = [num for i,num in enumerate(sample) if num%3 == 0 ]
print new_list
