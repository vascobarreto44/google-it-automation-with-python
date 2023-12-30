class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
        
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < self.top:
            self.current += 1
        else:
            print("floor does not exist")
        
    def down(self):
        """Makes the elevator go down one floor.""" 
        
        if self.current > self.bottom:
            self.current -= 1
        else:
            print("floor does not exist")
        
    def __str__(self):
        return "Current floor: {}".format(self.current)
    
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        
        if floor > self.current and (floor >= self.bottom and floor <= self.top):
            while self.current < floor:
                self.up()
        else:
            while self.current > floor:
                self.down()
