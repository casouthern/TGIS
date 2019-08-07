import turtle

# access to tkinter - tk & root
# instead of standard
# import tkinter as tk
# root = tk.Tk()
tk = turtle.TK
screen = turtle.getscreen()

root = screen._root
canvas = screen._canvas
root.title('TGIS')
# pack the canvas right
canvas.pack(side='right')

MOVING, DRAGGING = range(2)  # states
#root.set_geometry(900, 500, 0, 0)
#root.geometry('500x500')
#turtle.setup(180, -90)

# call setup() before setworldcoordinates()
# So if you make the screen size larger the coordinates will adjust to the new screensize
screen.setup(900, 500)
screen.setworldcoordinates(-180,-90,180,90)

#screen.bgpic('/Users/primaryuser/Desktop/world-map-with-continents.gif')
# create a toplevel menu
menubar = tk.Menu(root)
root.config(menu=menubar)

# create submenu
# submenus arent showing on Mac OSX
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Close", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

viewmenu = tk.Menu(menubar, tearoff=0)
viewmenu.add_command(label="956x502", command = 'ViewSetup1')
viewmenu.add_command(label="1200x800", command = 'ViewSetup2')
menubar.add_cascade(label="View", menu=viewmenu)

frame = tk.Frame(root)
footer = tk.Frame(root)
footer.pack(before=canvas, side='bottom', anchor= 'e')
#frame.pack(side='right')
footer.pack()
frame.pack()#fill='y', expand=True)
#Create a turtle and set its shape, color,  and lift up the pen:

turtle.shape('circle')
# we can hide the turtle and it will still dot() its shape when drawing
turtle.hideturtle()
turtle.color('red')
turtle.penup()

NAME = 0
POINTS = 1
POP = 2

text = ['World map draw colorado and plot NYC']
state = ["COLORADO", [[-109, 37],[-109, 41],[-102, 41],[-102, 37]], 5187582]
Andorra = ["Andorra", [[1.44583614083,42.6019451433],[1.73860914641,42.6163911858],[1.72360906008,42.5094360893],[1.45152728546,42.4462450888],[1.44583614083,42.6019451433]], 1]
cities = []
cities.append(["DENVER",[-104.98, 39.74], 634265])
cities.append(["BOULDER",[-105.27, 40.02], 98889])
cities.append(["DURANGO",[-107.88,37.28], 17069])
cities.append(["Hong Kong",[114.15769, 22.28552], 99999])
turtle.speed(0)
turtle.tracer(0)


def state_shapes():
    turtle.up()
    first_pixel = None
    for point in state[POINTS]:
      pixel = point
      if not first_pixel:
        first_pixel = pixel
      turtle.goto(pixel)
      turtle.down()
    turtle.goto(first_pixel)
    turtle.up()
    turtle.write(state[NAME], align="center", font=("Arial",16,"bold"))
state_shapes()


turtle.up()
first_pixel = None
for point in Andorra[POINTS]:
  pixel = point
  if not first_pixel:
    first_pixel = pixel
  turtle.goto(pixel)
  turtle.down()
turtle.goto(first_pixel)
turtle.up()
turtle.write(Andorra[NAME], align="center", font=("Arial",16,"bold"))

def state_cities():
    turtle.up()

    for city in cities:
      pixel = city[POINTS]
      turtle.up()
      turtle.goto(pixel)
      # Place a point for the city
      turtle.dot(10)
      # Label the city
      turtle.write(city[NAME] + ", Pop.: " + str(city[POP]), align="left")
      turtle.up()

state_cities()
# turn tracer off so it doesnt crash appending lat longs from mouse motion
turtle.tracer(1)

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    # to return the value in meters
    m = km * 1000
    return m

# get the sum total of floats in D

def TotalLength():
    print(sum(D))


def Infile():
    # create a data frame and use the get() function to retrieve user input as the pathname
    df = pd.read_csv(e6.get(), usecols = ["Id", "Resolution", "lat1", "lon1", "lat2", "lon2"], index_col = "Id")
    # if the lat longs are missing decimals you can perform division on whole number values to convert them to floats
    # convert lat longs missing decimal point divide by 10000000
    # make the column equal itself divided by 10000000
    df['lat1'] = df["lat1"]/10000000
    df['lon1'] = df["lon1"]/10000000
    df['lat2'] = df["lat2"]/10000000
    df['lon2'] = df["lon2"]/10000000
    for index,row in df.iterrows():
        lat1 = row['lat1'] #first row of location.lat column here
        lon1 = row['lon1'] #first row of location.long column here
        lat2 = row['lat2'] #second row of location.lat column here
        lon2 = row['lon2'] #second row of location.long column here
        value = haversine(lon1, lat1, lon2, lat2)  # calculate the distance
        new_column.append(value)   #append the empty list with distance values
    df.insert(5,'Distance',new_column)
    with open(e7.get(),'ab') as f:
        df.to_csv(f,index = False)



# export items in D to a CSV
def ExportCSV():
    with open('/Users/primaryuser/Desktop/area_gui.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        for n in D:
            writer.writerow([n])


def CircleArea():
    # assign diameter to functions to get what the functions return
    diameter = LengthDist()
    # calculate the radius of a circle
    radius = diameter/2
    # area of a circle
    area = 3.14 * radius**2
    # use insert() to place the str value of the area into the entry box
    e3.insert(END, str(area))
    

def GetArea():
    # assign length and width to functions to get what the functions return
    length = LengthDist()
    width = WidthDist()
    # calulate the area of a square/rect
    area = length * width / 2
    # use insert() to place the str value of the area into the entry box
    e3.insert(END, str(area))

def LengthDist():
    # .get() to retrieve input from Entry(root)  
    coord = e1.get()
    coord2 = e2.get()
    # split the lat long string at ',' to get lat1 lon1 and lat2 lon2 values
    lat1_str, lon1_str = coord.split(',')
    lat2_str, lon2_str = coord2.split(',')
    # convert the individual str to floats
    lat1_f = float(lat1_str)
    lon1_f = float(lon1_str)
    lat2_f = float(lat2_str)
    lon2_f = float(lon2_str)
    # convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(radians, [lat1_f, lon1_f, lat2_f, lon2_f])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    # to return the value in meters
    m = km * 1000
    # append distance m to global var D empty list
    D.append(m)
    print(D)
    # return distance in m
    return m

    

def WidthDist():
    coord = e4.get()
    coord2 = e5.get()
    lat1_str, lon1_str = coord.split(',')
    lat2_str, lon2_str = coord2.split(',')
    lat1_f = float(lat1_str)
    lon1_f = float(lon1_str)
    lat2_f = float(lat2_str)
    lon2_f = float(lon2_str)
    # convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(radians, [lat1_f, lon1_f, lat2_f, lon2_f])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    # to return the value in meters
    m = km * 1000
    return m

  
def move_handler(x, y):
    if state != MOVING:  # ignore stray events
        return

    onmove(screen, None)  # avoid overlapping events
    turtle.penup()
    turtle.setheading(turtle.towards(x, y))
    turtle.goto(x, y)
    onmove(screen, move_handler)

def click_handler(x, y):
    global state

    turtle.onclick(None)  # disable until release
    onmove(screen, None)  # disable competing handler

    turtle.onrelease(release_handler)  # watch for release event
    turtle.ondrag(drag_handler)  # motion is now dragging until release

    state = DRAGGING

def release_handler(x, y):
    global state

    turtle.onrelease(None)  # disable until click
    turtle.ondrag(None)  # disable competing handler

    turtle.onclick(click_handler)  # watch for click event
    onmove(screen, move_handler)  # dragging is now motion until click

    state = MOVING

def drag_handler(x, y):
    if state != DRAGGING:  # ignore stray events
        return

    turtle.ondrag(None)  # disable event inside event handler
    turtle.pendown()
    turtle.setheading(turtle.towards(x, y))
    turtle.goto(x, y)
    turtle.ondrag(drag_handler)  # reenable event on event handler exit

def onmove(self, fun, add=None):
    """
    Bind fun to mouse-motion event on screen.

    Arguments:
    self -- the singular screen instance
    fun  -- a function with two arguments, the coordinates
        of the mouse cursor on the canvas.

    Example:

    >>> onmove(turtle.Screen(), lambda x, y: print(x, y))
    >>> # Subsequently moving the cursor on the screen will
    >>> # print the cursor position to the console
    >>> screen.onmove(None)
    """

    if fun is None:
        self.cv.unbind('<Motion>')
    else:
        def eventfun(event):
            fun(self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale)
        self.cv.bind('<Motion>', eventfun, add)
        getloc()

# the below function constantly prints the mouse location
# but returns the canvas coordinates in pixels not the screen lat lon
def motion(event):
    e8.delete(0, 'end')
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

# this made the turtle go off screen but did update entry with latlong 
def motion2(event):
    x, y = (event.x), (event.y)
    turtle.goto(x-900/2, (y*-1)+500/2)
    pos = turtle.position()
    e8.delete(0, 'end')
    e8.insert('end', str(pos))
    #print('{}, {}'.format(x, y))

def movearound(event):
    turtle.goto(event.x-900/2, (event.y*-1)+500/2)

def getloc():
    #move_handler()
    e8.delete(0, 'end')
    pos = turtle.position()
    #x, y = pos
    e8.insert('end', str(pos))
    #e8.insert('end', str(pos))

# zoom function order of placement is important
# zoom_out has to stated before zoom_in
# if zoom_in is placed first setworldcooordinates will not be overwritten
# instead the screen canvas will look really small when using zoom_out
# essentially when we call zoom_out after zoom_in screen will pack everything into
# the screensize in zoom_out screen.setworldcoordinates(llx, lly,urx, ury) and maintain that relative size
# setworldcoordiantes is dependent on order placement in the code

# zoom is close to finished something else is causing polygons to look squished after zoom in and out
# after zooming out the scroll bars disappear from the canvas
# could be that setworldcoords changes canvas extent every time its called 

def zoom_out():
     tk = turtle.TK
     screen = turtle.getscreen()
     root = screen._root
     canvas = screen._canvas
     screen.setup(900, 500)
     screen.setworldcoordinates(-180,-90,180,90)
     turtle.speed(0)
     turtle.tracer(0)
##     turtle.goto(-180,-90)
##     L = turtle.position()
##     turtle.goto(180,90)
##     R = turtle.position()
##     urx, ury = R
##     llx, lly = L
##     screen.setworldcoordinates(llx, lly,urx, ury)
     #screen.update()

# this may be distorting shapes on the screen
def zoom_in():
    #turtle.clear()
    """ draw square for turtles """
    turtle.pen(shown=False)
    # to draw a square you want to : move forward, turn right,
    #  move forward, turn right,move forward turn right
    turtle.forward(15)  # forward takes a number which is the distance to move
    R = turtle.position()
    turtle.right(90)  # turn right
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    L = turtle.position()
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    urx, ury = R
    llx, lly = L
    screen.setworldcoordinates(llx, lly,urx, ury)
    
    turtle.pen(shown=True)

# this works and zooms in and out!! just need to implement some sort of panning function
# https://stackoverflow.com/questions/51050754/implement-python-tkinter-zoom-with-turtle-and-single-double-click
def zoom(event):
    amount = 0.9 if event.delta < 0 else 1.1

    canvas.scale(tk.ALL, 0, 0, amount, amount)
    

def up():
    turtle.setheading(90)
    turtle.forward(25)

def down():
    turtle.setheading(270)
    turtle.forward(25)

def left():
    turtle.setheading(180)
    turtle.forward(25)

def right():
    turtle.setheading(0)
    turtle.forward(25)
   
turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
turtle.onkey(getloc, 'x')
screen.onkey(zoom, 'z')
screen.onkey(zoom_out, 'o')
canvas.bind('<MouseWheel>', zoom)
#screen.onclick(turtle.goto)
#c.bind("<Motion>", movearound)

#turtle.onrelease(getloc)
# figure out how to bind mouse motion and call get loc
#canvas.bind('<Motion>', move_handler)
# create button
button = tk.Button(frame, text='Calculate', command=LengthDist)
button.grid(row=3, column=1, sticky='we')
e8 = tk.Entry(footer)
e8.grid(row=0, column=4, sticky='we')
'''
label = tk.Label(frame, background='grey', text='paste vertices of polygon length')
label.grid(row=0, sticky='we')
label = tk.Label(frame, text='Coordinate 1')
label.grid(row=1, sticky='we')
label = tk.Label(frame, text='Coordinate 2')
label.grid(row=2, sticky='we')
label = tk.Label(frame, text='Area in meters sqr')
label.grid(row=4, sticky='we')

label = tk.Label(frame, text='paste vertices of polygon width')
label.grid(row=0, column=2, sticky='we')
label = tk.Label(frame, text='Coordinate 1')
label.grid(row=1, column=2, sticky='we')
label = tk.Label(frame, text='Coordinate 2')
label.grid(row=2, column=2, sticky='we')
label = tk.Label(frame, text='Paste CSV pathname')
label.grid(row=3, column=2, sticky='we')
label = tk.Label(frame, text='Paste Destination pathname')
label.grid(row=4, column=2, sticky='we')
label = tk.Label(frame, text='position')
label.grid(row=8, column=0, sticky='we')

e1 = tk.Entry(frame)
e2 = tk.Entry(frame)
e3 = tk.Entry(frame)
e4 = tk.Entry(frame)
e5 = tk.Entry(frame)
e6 = tk.Entry(frame)
e7 = tk.Entry(frame)
e8 = tk.Entry(footer)

e1.grid(row=1, column=1, sticky='we')
e2.grid(row=2, column=1, sticky='we')
e3.grid(row=4, column=1, sticky='we')
e4.grid(row=1, column=3, sticky='we')
e5.grid(row=2, column=3, sticky='we')
e6.grid(row=3, column=3, sticky='we')
e7.grid(row=4, column=3, sticky='we')
e8.grid(row=0, column=4, sticky='we')

button = tk.Button(frame, text='Calculate', command=LengthDist)
button.grid(row=3, column=1, sticky='we')
button = tk.Button(frame, text='Export', command=Infile)
button.grid(row=5, column=3, sticky='we')
button = tk.Button(frame, text='Route Length', command=TotalLength)
button.grid(row=5, column=2, sticky='we')


coord1 = e1.get()
coord2 = e2.get()

button = tk.Button(frame, text="forward 50", command=lambda:turtle.forward(50))
button.grid(row=0, column=0, sticky='we')

button = tk.Button(frame, text="forward 10", command=lambda:turtle.forward(10))
button.grid(row=0, column=1, sticky='we')

button = tk.Button(frame, text="backward 10", command=lambda:turtle.backward(10))
button.grid(row=0, column=2, sticky='we')

button = tk.Button(frame, text="backward 50", command=lambda:turtle.backward(50))
button.grid(row=0, column=3, sticky='we')


button = tk.Button(frame, text="left 90", command=lambda:turtle.left(90))
button.grid(row=1, column=0, sticky='we')

button = tk.Button(frame, text="left 30", command=lambda:turtle.left(30))
button.grid(row=1, column=1, sticky='we')

button = tk.Button(frame, text="right 30", command=lambda:turtle.right(30))
button.grid(row=1, column=2, sticky='we')

button = tk.Button(frame, text="right 90", command=lambda:turtle.right(90))
button.grid(row=1, column=3, sticky='we')
'''
state = MOVING

# Initially we track the turtle's motion and left button clicks
onmove(screen, move_handler)  # a la screen.onmove(move_handler)
turtle.onclick(click_handler)  # a click will turn motion into drag
#turtle.done()
#turtle.mainloop()
root.mainloop()
