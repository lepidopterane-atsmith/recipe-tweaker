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
        self.deactivate( )

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
        self.active = False
#=======================================================================

def title():
    win = GraphWin("Literary (Lepidopterane mod)",600,600)
    win.setCoords(-100,-100,100,100)

    title = Text(Point(0,70),"Literary")
    title.setSize(24)
    title.setStyle("bold italic")
    title.draw(win)

    captione = Text(Point(0,40),"Type the name of the .txt file you want to analyze")
    captione.draw(win)
    
    captitwo = Text(Point(0,30),"[extension included]")
    captitwo.draw(win)

    captithree = Text(Point(0,0), "Then click to continue.")
    captitwo.setStyle("bold")
    captithree.draw(win)
    

    fileblank = Entry(Point(0,-50),20)
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