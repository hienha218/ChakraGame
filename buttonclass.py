# button.py
# for lab 9 on writing classes

from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        ## as you read through this, ask yourself:  what are the instance variables here?
        ## it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        ## you should comment these variables...
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.active = True #this variable keeps track of whether or not the button is currently "active"

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    ##check 3.  complete the deactivate() method
    def deactivate(self):
        "Sets this button to 'inactive'."
        ##color the text "darkgray"
        ##set the outline to look finer/thinner
        ##set the boolean variable that tracks "active"-ness to False
        self.label.setFill("darkgrey")
        self.rect.setWidth(1)
        self.active = False

    ##check 4.  complete the clicked() method
    def clicked(self, p):
        "Returns true if button active and Point p is inside"
        ##your code here
        if p is None:
            return False
        else:
            return (self.active and
                    self.xmin <= p.getX() <= self.xmax and
                    self.ymin <= p.getY() <= self.ymax)

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()

class CircleButton(Button):
    def __init__(self, win, center, radius, label):
        self.cir = Circle(center, radius)
        self.cir.setFill("lightgrey")
        self.cir.draw(win)
        self.label = Text(center,label)
        self.label.draw(win)

        self.centerx = center.getX()
        self.centery = center.getY()
        self.radius = radius
        
        self.active = True   


    def getLabel(self):
        "Returns the label string of this button."
        Button.getLabel(self)

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black') #color the text "black"
        self.cir.setWidth(2)       #set the outline to look bolder
        self.active = True

    
    def deactivate(self):
        "Sets this button to 'inactive'."
        ##color the text "darkgray"
        ##set the outline to look finer/thinner
        ##set the boolean variable that tracks "active"-ness to False
        self.label.setFill("darkgrey")
        self.cir.setWidth(1)
        self.active = False

    ##check 4.  complete the clicked() method
    def clicked(self, p):
        "Returns true if button active and Point p is inside"
        ##your code here
        if self.active and abs(p.getX()-self.centerx)<self.radius and abs(p.getY()-self.centery)<self.radius:
            return True
        else:
            return False

    
        
def main():
    ##check 1. create a graphical window in which to test the Button class
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")
    
    ##check 2. test the Button constructor method...
    ##create two Button objects, one for "Roll Dice" and the other for "Quit"
    ##activate the Roll button
    #rollButton = Button(win, Point(5,4), 6, 1, "Roll Dice")
    #quitButton = Button(win, Point(5,1), 2, 1, "Quit")
    rollButton = CircleButton(win,Point(5,6),2,"Roll Dice")
    quitButton = CircleButton(win,Point(5,2),2,"Quit")

    
    rollButton.activate()
    
    ##check 3. now test the deactivate() method...
    ##deactivate the "Quit" button
    quitButton.deactivate()


    ##check 4. test the .clicked() method with an if statement
    ##(remove this test code before moving onto the next check)

    pt = win.getMouse()
    while not quitButton.clicked(pt):
        #when roll button is clicked
        if rollButton.clicked(pt):
            #activate the quit button
            quitButton.activate()
        pt = win.getMouse()

  
    ##check 5. now test the clicked() boolean method...
    ##keep taking mouse clicks (in a loop) until the "Quit" button is clicked
        ##if the roll button is clicked
            ##activate the quit button
            
        
    #we reach this line of code when quit button is clicked b/c loop condition breaks
    win.close() #so close the window, ending the program
    
if __name__ == "__main__":
    main()
