# Sarah Abowitz and Stefany Alicea
# Recipe Tweaker

from graphics import *

class Button:
    '''Zelle Chap.10, p.324, also modded by my awesome prof Joseph O'Rourke '''

    def __init__( self, win, pcent, width, height, strlabel ):

        w,h = width/2, height/2
        x,y = pcent.getX( ), pcent.getY( )
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point( self.xmin, self.ymin )
        p2 = Point( self.xmax, self.ymax )
        self.rect = Rectangle( p1, p2 )
        self.rect.setFill( 'lightgray' )
        self.rect.draw( win )
        self.textlabel = Text( pcent, strlabel )
        self.textlabel.setSize( 18 )
        self.strlabel = strlabel
        self.textlabel.draw( win )
        #self.deactivate( )

    def clicked( self, p ):
        # JOR addition: Allow for p==None (no click)
        if p == None:
            return False
        x,y = p.getX( ), p.getY( )
        bool_clicked = (self.active
                and
                self.xmin <= x <= self.xmax
                and
                self.ymin <= y <= self.ymax
                )
        return bool_clicked
        # JOR added a button test here but I don't really need it
    
    def getLabel( self ):
        return self.strlabel

    def activate( self ):
        self.textlabel.setFill( 'Black' )
        self.rect.setWidth( 3 )
        self.rect.setOutline( 'Red' )
        self.active = True

    def deactivate( self ):
        self.textlabel.setFill( 'darkgray' )
        self.rect.setWidth( 1 )
        self.rect.setOutline( 'Black' )
        self.rect.undraw()
        self.textlabel.undraw()
        self.active = False
#=======================================================================

win = GraphWin("Recipe Tweaker",600,600)
win.setCoords(-100,-100,100,100)

def start():

    title = Text(Point(0,70),"Recipe Tweaker")
    title.setSize(24)
    title.setStyle("bold italic")
    title.draw(win)

    captione = Text(Point(0,40),"Type the name of the .txt recipe file you want to tweak")
    captione.draw(win)
    
    captitwo = Text(Point(0,30),"[extension included]")
    captitwo.draw(win)

    # would be awesome if I could have a next button

    captithree = Text(Point(0,-25), "Then click to continue.")
    captitwo.setStyle("bold")
    captithree.draw(win)

    fileblank = Entry(Point(0,0),20)
    fileblank.draw(win)
    filename = ''
    while(filename==''):
        y = win.getMouse()
        filename = fileblank.getText()
    fileblank.undraw()
    title.undraw()
    captione.undraw()
    captitwo.undraw()
    captithree.undraw()
    choices(filename)
    
def choices(filename):
	title = Text(Point(0,70),"Make Your Tweaks")
	title.setSize(18)
	title.setStyle("bold italic")
	title.draw(win)	
	
	dir = Text(Point(0,25), "Type one or more of the following tweaks, separate each with commas.")
	dir.draw(win)
	
	opt1 = Text(Point(0,15), "Gluten-Free")
	opt2 = Text(Point(0,10), "Sugar-Free")
	opt3 = Text(Point(0,5), "Vegan")
	opt4 = Text(Point(0,0), "Low-Sodium")
	
	options = [opt1, opt2, opt3, opt4]
	
	for i in options:
	    i.draw(win)
	
	ctcontinue = Text(Point(0,-75), "Then click to continue.")
	ctcontinue.setStyle("bold")
	ctcontinue.draw(win)
	
	but_ctnu = Button(win, Point(0,-60), 40, 10, 'Continue' )
	but_ctnu.activate()
	
	prefblank = Entry(Point(0,50),60)
	prefblank.draw(win)
	prefs = ''
	
	while(prefs==''):
		y = win.getMouse()
		print("We're here!")
		prefs = prefblank.getText()+" \n"
        
	print("now we're here!")
	title.undraw()
	prefblank.undraw()
	
	for i in options:
	    i.undraw()
	
	but_ctnu.deactivate()
	ctcontinue.undraw()
	dir.undraw()
	pages(filename, prefs)
    
def pages(filename, prefs):
    title = Text(Point(0,85),"Recipe Tweaked!")
    title.setSize(18)
    title.setStyle("bold italic")
    title.draw(win)
    
    str = "text "*25
    textline = Text(Point(0,0),str)
    textline.draw(win)
    
    but_prev = Button(win, Point(-80,80), 20,20,'Previous')
    but_prev.deactivate()
    
    but_next = Button(win, Point(80,80),20,20,'Next')
    but_quit = Button(win, Point(-80,-80),20,20,'Quit')
    but_again = Button(win, Point(80,-80),20,20,'Again!')
    # ask Stef about this one
    
    but_arr = [but_next,but_quit,but_again]
    for i in but_arr:
        i.activate()
    
    # load the first "page" of stuff
    # if the \n count is less than 33ish, deactivate next
    
    y = win.getMouse()
    
    while ( not but_quit.clicked(y)):
        if (but_again.clicked(y)):
        	but_arr = [but_next,but_quit,but_again,but_prev]
        	for i in but_arr:
        	    i.deactivate()
        	title.undraw()
        	textline.undraw()
        	start()
        y = win.getMouse()
             

    win.close()
    title.undraw()
    
start()