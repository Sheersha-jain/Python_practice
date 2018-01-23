class Copy:
    def copyString(self):
        sample = raw_input("Enter your string here : ")
        while True:
            multiplier = raw_input("Enter number here : ")
            if multiplier.isdigit():
                multiplier = int(multiplier)
                output = sample * multiplier
                print output
                break
            else :
                print "number should be non negetive integer"
                break 
obj = Copy()
obj.copyString()

