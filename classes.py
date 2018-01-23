class Testingapp:

    def __init__(self, no1, no2):
        print("this is init method")
        self.no1 = no1
        self.no2 = no2 

    def addition(self):
        return self.no1 + self.no2

    def __eq__(self,obj):

        if self.adding != obj.adding():
            print("objects are not equal")
            return False 
        else:
            print("objects are equal")
            return True
    if __name__ == '__main__':
        t1 = Testingapp(19,309)
        
        t2 = Testingapp(20,498)
        print(t1 ==t2)    
