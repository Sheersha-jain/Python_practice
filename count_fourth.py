class Input:
    def input_number(self):
        number = raw_input()
        numbers = map(int, number.split())
        print numbers


obj = Input()
obj.input_number()
