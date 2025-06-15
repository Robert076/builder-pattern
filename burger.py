class Burger:
    def __init__(self):
        self.patty = None
        self.cheese = None
        self.buns = None
        
    def setBuns(self, bunStyle):
        self.buns = bunStyle
        return self

    def setPatty(self, pattyStyle):
        self.patty = pattyStyle
        return self
        
    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle
        return self
    
    def print(self):
        print(self.patty, self.buns, self.cheese)

b = Burger()

b.setBuns("sesame buns").setPatty("black angus patty").setCheese("american cheese").print()