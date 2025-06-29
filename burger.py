class Burger:
    def __init__(self):
        self.patty = None
        self.cheese = None
        self.buns = None
        
    def setBuns(self, bunStyle):
        self.buns = bunStyle

    def setPatty(self, pattyStyle):
        self.patty = pattyStyle
        
    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle
    
    def print(self):
        print(self.patty, self.buns, self.cheese)

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()
    
    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self
    
    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self
    
    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self
    
    def build(self):
        return self.burger
    
    

b = BurgerBuilder()

b.addBuns("sesame buns").addPatty("black angus patty").addCheese("american cheese").build().print()