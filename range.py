import sys
"""
def main():
    list_of_squares = []  
    input_range_number = input('enter the range you want to calculate:')
    for number in range(int (input_range_number)):
        square = number*number
        list_of_squares.append(square)
    print list_of_squares

if __name__ == '__main__':
    main()
"""
class Range:

    def range_function(n):
        for i in range(n):
            yield i*i
    for item in range_function(int(sys.argv[1])):
        print(item)
