divisor_list = []

def divByfifteen():
    number_list = raw_input("Enter the list of number you want to enter : ")
    number_lists = map(int, number_list.split())
    for num in number_lists:
        if num%15 == 0:
            divisor_list.append(num)
    print "List of numbers divisible by 15 is : ", divisor_list

divByfifteen()
