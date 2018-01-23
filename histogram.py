input_list = raw_input("Enter the values of list : ")

numbers = map(int, input_list.split())

for var in numbers:
    output = ' '
    times = var
    while (times > 0):
        output += "*"
        times = times-1
    print output
    
print numbers
