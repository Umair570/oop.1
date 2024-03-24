class Cars:
    def __init__(self,colour,model):   #init is the method or function which is automatically called in a class
        self.col=colour   #self. means that self is the object and the thing which comes after
                             #. means that it is the attribute of that object(specific object) for that instance
        self.mod=model
    def car(self):
        return f"{self.col} is driving and its model is {self.mod}"

car1=Cars("Red",2021)    
print(car1.car())    
car2=Cars("Black",2024)        
print(car2.car())