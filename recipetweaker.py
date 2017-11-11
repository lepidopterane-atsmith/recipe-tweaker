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
		self.rect.setFill( 'Yellow' )
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

	def activate( self, isDrawn ):
		self.textlabel.setFill( 'Red' )
		self.rect.setWidth( 3 )
		self.rect.setOutline( 'Yellow' )
		if (not isDrawn):
			self.rect.draw( win )
			self.textlabel.draw(win)
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
	win.setBackground(color_rgb(255,235,225))
	title = Text(Point(0,70),"Recipe Tweaker")
	title.setSize(24)
	title.setStyle("bold italic")
	title.draw(win)

	captione = Text(Point(0,40),"Type the name of the .txt recipe file you want to tweak.")
	captione.draw(win)

	captitwo = Text(Point(0,30),"[extension included]")
	captitwo.draw(win)

	# would be awesome if I could have a next button

	but_cntu = Button(win, Point(0,-60),40,10,'Continue')
	but_cntu.activate(True)

	fileblank = Entry(Point(0,0),20)
	fileblank.draw(win)
	filename = ''
	
	y = win.getMouse()
	
	while(filename=='' or (not but_cntu.clicked(y))):
		y = win.getMouse()
		filename = fileblank.getText()
	fileblank.undraw()
	title.undraw()
	captione.undraw()
	captitwo.undraw()
	but_cntu.deactivate()
	choices(filename)

def choices(filename):
	title = Text(Point(0,70),"Make Your Tweaks")
	title.setSize(18)
	title.setStyle("bold italic")
	title.draw(win)	

	win.setBackground(color_rgb(225,235,255))

	dir = Text(Point(0,25), "Type one or more of the following tweaks, separate each with commas.")
	dir.draw(win)

	opt1 = Text(Point(0,15), "Gluten-Free")
	opt1.draw(win)
	opt2 = Text(Point(0,10),"Sugar-Free")
	opt2.draw(win)
	opt3 = Text(Point(0,5),"Vegan")
	opt3.draw(win)
	opt4 = Text(Point(0,0),"Low-Sodium")
	opt4.draw(win)

	but_ctnu = Button(win, Point(0,-60),40,10,'Continue')
	but_ctnu.activate(True)

	prefblank = Entry(Point(0,50),60)
	prefblank.draw(win)
	prefs = ''
	
	y = win.getMouse()

	while(prefs=='' or (not but_ctnu.clicked(y))):
		y = win.getMouse()
		print("boop")
		prefs = prefblank.getText()+" \n"
		
	but_ctnu.deactivate()

	raw = ["-","1","3/4","cups","confectioners\'","sugar","-","1","cup","almond","flour","-","3","large","egg","whites,","at","room","temperature","-","1/4","teaspoon","cream","of","tartar","-","Pinch","of","salt","-","1/4","cup","superfine","sugar","-","2","to","3","drops","gel","food","coloring","(see","below)","-","1/2","teaspoon","vanilla,","almond","or","mint","extract","-","Oven","with","convection","setting","-","4","baking","sheets","-","3","silicone","baking","mats","-","Fine-mesh","sieve","-","Pastry","bag","with","1/4-inch","round","tip","1.","Preheat","the","oven","to","300","degrees","F","using","the","convection","setting.","Line","3","baking","sheets","with","silicone","mats.","Measure","the","confectioners'","sugar","and","almond","flour","by","spooning","them","into","measuring","cups","and","leveling","with","a","knife.","Transfer","to","a","bowl;","whisk","to","combine.","2.","Sift","the","sugar-almond","flour","mixture,","a","little","at","a","time,","through","a","fine-mesh","sieve","into","a","large","bowl,","pressing","with","a","rubber","spatula","to","pass","through","as","much","as","possible.","It","will","take","a","while,","and","up","to","2","tablespoons","of","coarse","almond","flour","may","be","left;","just","toss","it.","3.","Beat","the","egg","whites,","cream","of","tartar","and","salt","with","a","mixer","on","medium","speed","until","frothy.","Increase","the","speed","to","medium","high;","gradually","add","the","superfine","sugar","and","beat","until","stiff","and","shiny,","about","5","more","minutes.","4.","Transfer","the","beaten","egg","whites","to","the","bowl","with","the","almond","flour","mixture.","Draw","a","rubber","spatula","halfway","through","the","mixture","and","fold","until","incorporated,","giving","the","bowl","a","quarter","turn","with","each","fold.","5.","Add","the","food","coloring","and","extract","(see","below).","Continue","folding","and","turning,","scraping","down","the","bowl,","until","the","batter","is","smooth","and","falls","off","the","spatula","in","a","thin","flat","ribbon,","2","to","3","minutes.","6.","Transfer","the","batter","to","a","pastry","bag","fitted","with","a","1/4-inch","round","tip.","Holding","the","bag","vertically","and","close","to","the","baking","sheet,","pipe","1","1/4-inch","circles","(24","per","sheet).","Firmly","tap","the","baking","sheets","twice","against","the","counter","to","release","any","air","bubbles.","7.","Let","the","cookies","sit","at","room","temperature","until","the","tops","are","no","longer","sticky","to","the","touch,","15","minutes","to","1","hour,","depending","on","the","humidity.","Slip","another","baking","sheet","under","the","first","batch","(a","double","baking","sheet","protects","the","cookies","from","the","heat).","8.","Bake","the","first","batch","until","the","cookies","are","shiny","and","rise","1/8","inch","to","form","a","foot","about","20","minutes.","Transfer","to","a","rack","to","cool","completely.","Repeat,","using","a","double","sheet","for","each","batch.","Peel","the","cookies","off","the","mats","and","sandwich","with","a","thin","layer","of","filling","(see","below).","9.","Tint","the","batter","with","2","drops","neon","pink","gel","food","coloring;","flavor","with","almond","extract.","Fill","with","seedless","raspberry","jam","(you'll","need","about","3/4","cup).","10.","Tint","the","batter","with","2","drops","mint","green","gel","food","coloring;","flavor","with","mint","extract.","For","the","filling,","microwave","3","ounces","chopped","white","chocolate,","2","tablespoons","heavy","cream","and","1","tablespoon","butter","in","30-second","intervals,","stirring,","until","smooth.","Stir","in","1/4","teaspoon","mint","extract","and","1","drop","mint","green","gel","food","coloring.","11.","Tint","the","batter","with","3","drops","royal","blue","gel","food","coloring;","flavor","with","vanilla","extract.","For","the","filling,","mix","4","ounces","softened","cream","cheese","and","3","tablespoons","blueberry","jam.","12.","Tint","the","batter","with","2","drops","violet","gel","food","coloring;","flavor","with","almond","or","vanilla","extract.","For","the","filling,","mix","3/4","cup","mascarpone","cheese,","2","tablespoons","Transfer","to","a","rack","to","cool","completely.","Repeat,","using","a","double","sheet","for","each","batch.","Peel","the","cookies","off","the","mats","and","sandwich","with","a","thin","layer","of","filling","(see","below).","9.","Tint","the","batter","with","2","drops","neon","pink","gel","food","coloring;","flavor","with","almond","extract.","Fill","with","seedless","raspberry","jam","(you'll","need","about","3/4","cup).","10.","Tint","the","batter","with","2","drops","mint","green","gel","food","coloring;","flavor","with","mint","extract.","For","the","filling,","microwave","3","ounces","chopped","white","chocolate,","2","tablespoons","heavy","cream","and","1","tablespoon","butter","in","30-second","intervals,","stirring,","until","smooth.","Stir","in","1/4","teaspoon","mint","extract","and","1","drop","mint","green","gel","food","coloring.","11.","Tint","the","batter","with","3","drops","royal","blue","gel","food","coloring;","flavor","with","vanilla","extract.","For","the","filling,","mix","4","ounces","softened","cream","cheese","and","3","tablespoons","blueberry","jam.","12.","Tint","the","batter","with","2","drops","violet","gel","food","coloring;","flavor","with","almond","or","vanilla","extract.","For","the","filling,","mix","3/4","cup","mascarpone","cheese,","2","tablespoons","Transfer","to","a","rack","to","cool","completely.","Repeat,","using","a","double","sheet","for","each","batch.","Peel","the","cookies","off","the","mats","and","sandwich","with","a","thin","layer","of","filling","(see","below).","9.","Tint","the","batter","with","2","drops","neon","pink","gel","food","coloring;","flavor","with","almond","extract.","Fill","with","seedless","raspberry","jam","(you'll","need","about","3/4","cup).","10.","Tint","the","batter","with","2","drops","mint","green","gel","food","coloring;","flavor","with","mint","extract.","For","the","filling,","microwave","3","ounces","chopped","white","chocolate,","2","tablespoons","heavy","cream","and","1","tablespoon","butter","in","30-second","intervals,","stirring,","until","smooth.","Stir","in","1/4","teaspoon","mint","extract","and","1","drop","mint","green","gel","food","coloring.","11.","Tint","the","batter","with","3","drops","royal","blue","gel","food","coloring;","flavor","with","vanilla","extract.","For","the","filling,","mix","4","ounces","softened","cream","cheese","and","3","tablespoons","blueberry","jam.","12.","Tint","the","batter","with","2","drops","violet","gel","food","coloring;","flavor","with","almond","or","vanilla","extract.","For","the","filling,","mix","3/4","cup","mascarpone","cheese,","2","tablespoons","honey","and","1","teaspoon","ground","dried","lavender."]
	# I know this is long but also screw it I'm not gonna make this take up 25 lines of code    
	
	title.undraw()
	prefblank.undraw()
	
	options = [opt1, opt2, opt3, opt4]

	for i in options:
		i.undraw()

	dir.undraw()
	pages(filename, prefs, raw)

def pages(filename, prefs, raw):
	title = Text(Point(0,85),"Recipe Tweaked!")
	title.setSize(18)
	title.setStyle("bold italic")
	title.draw(win)

	str = "text "*25
	textline = Text(Point(0,0),str)
	#textline.draw(win)

	but_prev = Button(win, Point(-75,90), 30,18,'Previous')
	but_prev.deactivate()

	but_next = Button(win, Point(80,90),20,18,'Next')
	but_quit = Button(win, Point(-80,-80),20,20,'Quit')
	but_again = Button(win, Point(80,-80),20,20,'Again!')
	# ask Stef about this one

	but_arr = [but_next,but_quit,but_again]
	for i in but_arr:
		i.activate(True)

	# load the first "page" of stuff
	# if the \n count is less than 33ish, deactivate next

	processed = render(raw)
	x = len(processed)

	win.setBackground(color_rgb(235,255,225))

	print(x)

	if (x < 29):
		but_next.deactivate();
	
	# next step: group processed into arrs of 33 lns each. it's gonna be a 2D list deal
	folio = []
	current = []

	for i in processed:
		if (len(current) == 29):
			folio.append(current)
			current = []
		current.append(i)

	while (len(current)<29):
		current.append("")

	folio.append(current)

	for i in folio:
		print(len (i))

	lines = []
	lcounter = 0
	whichfolio = 0
	thisfolio = folio[whichfolio]
	for i in range(70,-70,-5):
		text = Text(Point(0,i),thisfolio[lcounter])
		lines.append(text)
		text.draw(win)
		lcounter += 1

	y = win.getMouse()

	while ( not but_quit.clicked(y)):
		if (but_again.clicked(y)):
	
			but_arr = [but_next,but_quit,but_again,but_prev]
			for i in but_arr:
				i.deactivate()
			
			for i in lines:
				i.undraw()
			
			title.undraw()
			textline.undraw()
			start()
		
		if (but_next.clicked(y)):
			but_prev.deactivate()
			but_prev.activate(False)
			whichfolio += 1
			thisfolio = folio[whichfolio]
			lcounter = 0
			if (whichfolio == len(folio)-1):
				but_next.deactivate()
		
			for i in lines:
				i.setText(thisfolio[lcounter])   
				lcounter += 1 
		
		if (but_prev.clicked(y)):
			but_next.deactivate()
			but_next.activate(False)
			whichfolio -= 1
			thisfolio = folio[whichfolio]
			lcounter = 0
			if (whichfolio == 0):
				but_prev.deactivate()
			
			for i in lines:
				i.setText(thisfolio[lcounter])
				lcounter += 1
			
		y = win.getMouse()
		 

	win.close()
	title.undraw()

def render(raw):
	processed = []

	#Find indexOf -, organize into lines
	stepStartInd = raw.index("1.")
	stub = ""

	for i in range(0,stepStartInd):
		if (raw[i]=="-"):
			if (not stub==""):
				while (len(stub) < 124):
					stub += " "
				processed.append(stub);
			stub = "-"
		else:
			stub += " "+raw[i]

	# The hardest part: identifying steps.
	stepset = []
	end = len(raw)
	stub = ""

	for i in range(stepStartInd,end):
		if (len(raw[i]) <4 and raw[i].endswith(".") and raw[i].replace(".","").isdigit()):
			if (not stub==""):
				while (len(stub) < 100):
					stub += " "
				stepset.append(stub);
			stub = raw[i]
		else:
			stub += " "+raw[i]

	for i in stepset:
		if (len(i) < 101):
			processed.append(i);
		else:
			while (len(i)>100):
				div = 100
				while (not i[div].isspace()):
					div -= 1
				stub = i[:div]
				processed.append(stub)
				i = i[div:]
			if (len(i)>0):
				processed.append(i)    
	'''
	for i in processed:
		print(i+"\n");
	'''
	return processed

start()
