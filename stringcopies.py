def nCopies():
    sample = raw_input("Enter the string you want to replicate : ")
    number = input("Enter the number of times you want to print first two characters : ")
    if sample > 2:
        print number * sample[0] 
        print number * sample[1]
    if sample == 2:
        print sample * number

nCopies()

