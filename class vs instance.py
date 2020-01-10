class Person:
    def __init__(self,initialAge):
        self.age=initialAge
    def amIOld(self): 
        if self.age<13:
            if self.age<0:
                self.age=0
                print('Age is not valid, setting age to 0.')
            print('You are young.')
        elif 13<=self.age<18:
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self): 
        self.age+=1
