while True:
    N = raw_input("Please enter an non-negative even integer: ") #request user to input
    if N.isdigit(): # accepts a string of positive integer, filter out floats, negative ints
        N = int(N)
        if N % 2 == 0: #no need to test N>=0 here
            break
print 'Your input is: ', N
