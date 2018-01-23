sample_list = raw_input("Enter the elements of list : ")

sample_lists = map(int , sample_list.split())

result = ' '
for var in sample_lists:
    result += str(var)
print result




