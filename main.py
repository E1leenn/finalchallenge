from tkinter import *
from tkinter import messagebox
# from student_pub import *

def gridfunc():
    global var 
    var = "Grid"
    title.config(text=var)

    contenttitle.grid_forget()
    contenttxt.grid_forget()

    tttframe.grid_forget()
    gndframe.grid(row=0, column=0)
    dframe.grid_forget()
    gframe.grid(row=0, column=0)

def drawfunc():
    global var 
    var = "Draw"
    title.config(text=var)

    contenttitle.grid_forget()
    contenttxt.grid_forget()

    tttframe.grid_forget()
    gndframe.grid(row=0, column=0)
    gframe.grid_forget()
    dframe.grid(row=0, column=0)

def tttfunc():
    global var 
    var = "Welcome to Tic-Tac-Toe"
    title.config(text=var)
    
    contenttitle.grid_forget()
    contenttxt.grid_forget()
    
    gndframe.grid_forget()
    tttframe.grid(row=0, column=0)

def whitebtn(i, j):
    global colour

    if colour == 0:
      button[i][j].config(bg='grey99')
      value[i][j] = 0
    elif colour == 1: 
      button[i][j].config(bg='grey88')
      value[i][j] = 20
    elif colour == 2:
      button[i][j].config(bg='grey77')
      value[i][j] = 30
    elif colour == 3: 
      button[i][j].config(bg='grey66')
      value[i][j] = 40
    elif colour == 4:
      button[i][j].config(bg='grey44')  
      value[i][j] = 50
    elif colour == 5: 
      button[i][j].config(bg='grey33')
      value[i][j] = 60
    elif colour == 6:
      button[i][j].config(bg='grey22')
      value[i][j] = 70
    else: 
      button[i][j].config(bg='grey1')
      value[i][j] = 90

def change_colour(m): 
    global colour
    colour=m 

    print("colour is {}".format(colour))

def allwht():
    for j in range (32):
      for i in range (32):
        button[i][j].config(bg='grey99')
        value[i][j] = 0

def allblk():
    for j in range (32):
      for i in range (32):
        button[i][j].config(bg='grey1')
        value[i][j] = 90

def pattern():
    for j in range (32):
      for i in range (32):
        if i == j: 
          button[i][j].config(bg='grey66')
          value[i][j] = 40
        elif i + j == 31: 
          button[i][j].config(bg='grey66')
          value[i][j] = 40
        else:
          button[i][j].config(bg='grey99')
          value[i][j] = 0


def ramseq():
    for j in range (32):
      for i in range (32):
        if j < 6:
          button[i][j].config(bg='grey99')
          value[i][j] = 0
        elif j >= 6 and j <= 12:
          button[i][j].config(bg='grey88')
          value[i][j] = 20
        elif j >= 12 and j <= 18:
          button[i][j].config(bg='grey77')
          value[i][j] = 30
        elif j >= 18 and j <= 24:
          button[i][j].config(bg='grey66')
          value[i][j] = 40
        elif j >= 24 and j <= 32:
          button[i][j].config(bg='grey44')
          value[i][j] = 50 

###########################################################################################
def sendbtn():
    #print(value)
    print(canvasdraw)
    # pubpic(value)

def get_x_and_y(event):
   global lasx, lasy
   lasx, lasy = event.x, event.y

def paint(event):
    global lasx, lasy, value
    if lasx >= 0 and lasx <= 799 and lasy >= 0 and lasy <= 799:
      if colour == 0: 
          c.create_line((lasx,lasy, event.x, event.y),fill='grey99',width=4)
          canvasdraw[lasx][lasy] = 0
      elif colour == 1:
          c.create_line((lasx,lasy, event.x, event.y),fill='grey88',width=4)
          canvasdraw[lasx][lasy] = 1
      elif colour == 2:
          c.create_line((lasx,lasy, event.x, event.y),fill='grey77',width=4)
          canvasdraw[lasx][lasy] = 2
      elif colour == 3: 
          c.create_line((lasx,lasy, event.x, event.y),fill='grey66',width=4)
          canvasdraw[lasx][lasy] = 3
      elif colour == 4:
          c.create_line((lasx,lasy, event.x, event.y),fill='grey44',width=4)
          canvasdraw[lasx][lasy] = 4
      elif colour == 5: 
          c.create_line((lasx,lasy, event.x, event.y),fill='grey33',width=4)
          canvasdraw[lasx][lasy] = 5
      elif colour == 6:
          c.create_line((lasx,lasy, event.x, event.y),fill='grey22',width=4)
          canvasdraw[lasx][lasy] = 6
      else: 
          c.create_line((lasx,lasy, event.x, event.y),fill='grey11',width=4)
          canvasdraw[lasx][lasy] = 7
      get_x_and_y(event)

def scaledown(r, c):
    global lasx, lasy
    list = []
    for x in range(r, c):
      for y in range(r, c):
        list.append(canvasdraw[x][y])
    return list


def save_draw_colour(list):
  for r in range(32):
    for c in range(32):
      if list[r][c] == 0:
        button[r][c].config(bg='grey99')
        value[r][c] = 0
      elif list[r][c] == 1: 
        button[r][c].config(bg='grey88')
        value[r][c] = 20
      elif list[r][c] == 2:
        button[r][c].config(bg='grey77')
        value[r][c] = 30
      elif list[r][c] == 3: 
        button[r][c].config(bg='grey66')
        value[r][c] = 40
      elif list[r][c] == 4:
        button[r][c].config(bg='grey44')
        value[r][c] = 50  
      elif list[r][c] == 5: 
        button[r][c].config(bg='grey33')
        value[r][c] = 60
      elif list[r][c] == 6:
        button[r][c].config(bg='grey22')
        value[r][c] = 70
      else: 
        button[r][c].config(bg='grey1')
        value[r][c] = 90

def save_img():
    global list2, list1, value
    list2 = []
    list1 = []
    list3 = []
    list4 = []
    for i in range(0, 800, 25):
      list3 = []
      for t in range(0 , 800, 25):
        getnumber = f0(t, i) #getting the row downwards then col cause grid is store in the order row-column
        #print(i, t)
        list3.append(getnumber)
      list4.append(list3)
      #list3.append(list1)
    save_draw_colour(list4)
    print(list4)
  
def f0(x, y): #get the starting x, y of a 18x18 and to return 1 value back to rep the 18x18, to scale down a 18x18 to a 1x1
    global list0, list1, list2
    list = []
    #num1 = 18*(x-1)
    #num2 = num1 + 18
    for i in range(x ,25+x):
      for t in range(y ,25+y):
        list.append(canvasdraw[i][t])
    list0 = list
    freq = min(set(list0), key = list0.count) #using min instead cause if max almost everytime will get 0,harder for the draw to show; once the 18x18 grid got 1 value change, then return that value
                                              #Link: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    #list1.append(freq)
    return freq 

def clearbtn():
    c.delete('all')
    allwht()
    for i in range(800):
        for j in range(800):
            canvasdraw[i][j] = 0

#########################################################################################

def changeto(m):
    global pattern
    pattern = m 
    # print("pattern is", pattern)

def tictaotoe(x,y):
    global pattern, xoff, yoff
    if x == 0 and y == 0:
        xoff = 0
        yoff = 0
    elif x == 0 and y == 1:
        xoff = 0
        yoff = 12
    elif x == 0 and y == 2:
        xoff = 0
        yoff = 24
    elif x == 1 and y == 0:
        xoff = 12
        yoff = 0 
    elif x == 1 and y == 1: 
        xoff = 12
        yoff = 12
    elif x == 1 and y == 2: 
        xoff= 12
        yoff = 24 
    elif x == 2 and y == 0: 
        xoff = 24
        yoff = 0 
    elif x == 2 and y == 1: 
        xoff = 24
        yoff = 12 
    else: 
        xoff = 24
        yoff = 24

    if pattern == 0: 
        var = "X"
        gui[x][y].config(text=var)
        condition(logic(var))
        print(logic(var))
        for i in range (32):
            for j in range (32):
                if i == xoff and j == yoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 1 and j == yoff + 1: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 2 and j == yoff + 2: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 3 and j == yoff + 3: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 4 and j == yoff + 4: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 5 and j == yoff + 5: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 6 and j == yoff + 6: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 7 and j == yoff + 7: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff and j == yoff + 7: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 1 and j == yoff + 6: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 2 and j == yoff + 5: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 3 and j == yoff + 4: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 4 and j == yoff + 3: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 5 and j == yoff + 2: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 6 and j == yoff + 1: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == xoff + 7 and j == yoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                

    else:
        var = "O"
        gui[x][y].config(text=var)
        condition(logic(var))
        print(logic(var))
        for i in range (32):
            for j in range (32):
                if j == 1 + yoff: 
                    if i == 2 + xoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                    elif i == 3 + xoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                    elif i == 4 + xoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                    elif i == 5 + xoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif j == 6 + yoff: 
                    if i == 2 + xoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                    elif i == 3 + xoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                    elif i == 4 + xoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                    elif i == 5 + xoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == 1 + xoff: 
                    if j == 2 + yoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                    elif j == 3 + yoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                    elif j == 4 + yoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                    elif j == 5 + yoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                elif i == 6 + xoff: 
                    if j == 2 + yoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                    elif j == 3 + yoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                    elif j == 4 + yoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")
                    elif j == 5 + yoff: 
                        value[i][j] = 7
                        btn[i][j].config(bg="black")

    # student_pub.pubpic(value)
    # logic(x,y)

def check():
    global p
    for x in range (3):
        for y in range (3):
            if (gui[x][y].cget('text') == 'X' or gui[x][y].cget('text') == 'O'):
                p = p+1

def logic(y):
    global p
    p = 0
    check()
    print(p)
    if      ((gui[0][0].cget('text') == y and gui[0][1].cget('text') == y and gui[0][2].cget('text') == y) or
			(gui[1][0].cget('text') == y and gui[1][1].cget('text') == y and gui[1][2].cget('text') == y) or
			(gui[2][0].cget('text') == y and gui[2][1].cget('text') == y and gui[2][2].cget('text') == y) or
			(gui[0][0].cget('text') == y and gui[1][0].cget('text') == y and gui[2][0].cget('text') == y) or
			(gui[0][1].cget('text') == y and gui[1][1].cget('text') == y and gui[2][1].cget('text') == y) or
			(gui[0][2].cget('text') == y and gui[1][2].cget('text') == y and gui[2][2].cget('text') == y) or
			(gui[0][0].cget('text') == y and gui[1][1].cget('text') == y and gui[2][2].cget('text') == y) or
			(gui[0][2].cget('text') == y and gui[1][1].cget('text') == y and gui[2][0].cget('text') == y)):
            return y
    elif (p >= 9):
        c = 'c'
        return c
    else:  
        return N
    

def condition(var):
    if var == "O": 
        messagebox.showinfo("Winner", "Player 1 won the match")
    elif var == "X": 
        messagebox.showinfo("Winner", "Player 2 won the match")
    elif var == 'c': 
        messagebox.showinfo("TIE", "tie game")


def clear():
    for i in range (32):
        for j in range (32):
            btn[i][j].config(bg="white")
            value[i][j] = 0

    for x in range(3):
        for y in range(3):
            gui[x][y].config(text='')

    print("Clear All")
    border()

def border(): 
    print("Borders")
    for j in range (32):
        for i in range (32):
            if i == 8: 
                value[i][j] = 7
            elif i == 9: 
                value[i][j] = 7
            elif i == 10: 
                value[i][j] = 7
            elif i == 11: 
                value[i][j] = 7
            elif i == 20: 
                value[i][j] = 7
            elif i ==  21: 
                value[i][j] = 7
            elif i == 22: 
                value[i][j] = 7
            elif i == 23: 
                value[i][j] = 7
            elif j == 8: 
                value[i][j] = 7
            elif j == 9: 
                value[i][j] = 7
            elif j == 10: 
                value[i][j] = 7
            elif j == 11: 
                value[i][j] = 7
            elif j == 20: 
                value[i][j] = 7
            elif j ==  21: 
                value[i][j] = 7
            elif j == 22: 
                value[i][j] = 7
            elif j == 23: 
                value[i][j] = 7
            else:
                value[i][j] = 0

#################################################################################################
main = Tk()
# main.state('zoom')

titleframe = Frame(main)
titleframe.grid(row=0, columnspan=2)
contentframe = Frame(main)
contentframe.grid(row=1, column=0)
modeframe = Frame(main)
modeframe.grid(row=1, column=1, padx=15, pady=15)


#title for different mode
var = "Welcome!!!"
titlefont = ("Fixedsys", 25)
title = Label(titleframe, text=var, font=titlefont)
title.grid(row=0, column=0)

# content 
explaination = Frame(contentframe)
explaination.grid(row=0, column=0)
contenttitle = Label(explaination, text="Theme: Wonders of Our Childhood", font=("Fixedsys", 15))
contenttitle.grid(row=0, column=0)
contenttxt = Label(explaination, text="""Our features consists of games that remind us of our childhood.
 We created these features as we wanted to bring some form of nostalgia
 to our target audience and teach them the physics of polarisation 
 through our interactive games while using our games as a form of relatability.""", font=("Courier", 15))

contenttxt.grid(row=1, column=0)

#mode 
modefont = ("Courier", 15)

default = Button(modeframe, text="Grid", font=modefont, command=gridfunc)
default.grid(row=0, column=0, padx=5, pady=5)
draw = Button(modeframe, text="Draw", font=modefont, command=drawfunc)
draw.grid(row=1, column=0, padx=5, pady=5)
ttt = Button(modeframe, text="Tic-Tac-Toe", font=modefont, command=tttfunc)
ttt.grid(row=2, column=0)

############################################ GRID 
gndframe = Frame(contentframe)

gframe = Frame(gndframe)
gframe.grid(row=0, column=0)

gndframe2 = Frame(gndframe) #shades btn
gndframe2.grid(row=0, column=1)
gndframe3 = Frame(gndframe)
gndframe3.grid(row=1, columnspan=2) #colour btns 
gndframe4 = Frame(gndframe)
gndframe4.grid(row=2, columnspan=2) #send btn

# 32x32 grid
button = [[j for j in range(32)] for i in range(32)]
value = [[0 for i in range(32)] for j in range(32)]

for j in range (32):
  for i in range (32):
    button[i][j] = Button(gframe, font=("Calibri, 5"), width=1, height=1, bg='white', command=lambda r=i, c=j:whitebtn(r, c))
    button[i][j].grid(row=i, column=j)

#shades button
white = Button(gndframe2, text="White", font=("Calibri, 10"), bg='grey99', width=13, height=2, command=lambda m=0:change_colour(m))
white.grid(row=1, column=0)
grey1 = Button(gndframe2, text="Grey1", font=("Calibri, 10"), bg='grey88', width=13, height=2, command=lambda m=1:change_colour(m))
grey1.grid(row=2, column=0)
grey2 = Button(gndframe2, text="Grey2", font=("Calibri, 10"), bg='grey77', width=13, height=2, command=lambda m=2:change_colour(m))
grey2.grid(row=3, column=0)
grey3 = Button(gndframe2, text="Grey3", font=("Calibri, 10"), bg='grey66', width=13, height=2, command=lambda m=3:change_colour(m))
grey3.grid(row=4, column=0)
grey4 = Button(gndframe2, text="Grey4", font=("Calibri, 10"), bg='grey44', width=13, height=2, command=lambda m=4:change_colour(m))
grey4.grid(row=5, column=0)
grey5 = Button(gndframe2, text="Grey5", font=("Calibri, 10"), bg='grey33', fg='white', width=13, height=2, command=lambda m=5:change_colour(m))
grey5.grid(row=6, column=0)
grey6 = Button(gndframe2, text="Grey6", font=("Calibri, 10"), bg='grey11', fg='white', width=13, height=2, command=lambda m=6:change_colour(m))
grey6.grid(row=7, column=0)
black = Button(gndframe2, text="Black", font=("Calibri, 10"), bg='grey1', fg='white', width=13, height=2, command=lambda m=7:change_colour(m))
black.grid(row=8, column=0)

#save button
savebtn = Button(gndframe2, text="Save", font=("Calibri, 10"), bg='light blue', fg='black', width=13, height=2, command=save_img)
savebtn.grid(row=9, column=0)

#colour button
allwhite = Button(gndframe3, text="All White",font=("Calibri, 12"), bg='white', width=13, height=2, command=allwht)
allwhite.grid(row=0, column=0)

allblack = Button(gndframe3, text="All Black",font=("Calibri, 12"), bg='black', fg='white', width=13, height=2, command=allblk)
allblack.grid(row=0, column=1)

clear = Button(gndframe3, text="Clear",font=("Calibri, 12"), bg='gold', width=13, height=2, command=clearbtn)
clear.grid(row=0, column=2)

#send btn
send = Button(gndframe4, text="Send Image!", font=("Calibri, 12"), width=13, height=2, command=lambda :sendbtn())
send.grid(row=0, column=0)

############################################### DRAW
dframe = Frame(gndframe)
dframe.grid(row=0, column=0)

c = Canvas(dframe, width=800, height=800, bg='white')  
c.grid(row=0, column=0)

c.bind('<Button-1>', get_x_and_y)
c.bind('<B1-Motion>',paint)
c.bind('<Enter>', get_x_and_y)

#this variable to store the colour choice 
colour = 0
canvasdraw = [[0 for i in range(800)] for j in range(800)]  # save eventxy into an array 


###################################### TIC-TAC-TOE
tttframe = Frame(contentframe)

tttframe1 = Frame(tttframe)
tttframe1.grid(rowspan=2, column=0)

btn = [[i for i in range (32)] for j in range (32)]
for i in range (32):
    for j in range (32):
        btn[i][j] = Button(tttframe1, font=("Calibri, 5"), width=1, height=1, bg="white")
        btn[i][j].grid(row=i, column=j)

tttframe2 = Frame(tttframe)
tttframe2.grid(row=0, column=1, padx=15)

value = [[0 for i in range(32)] for j in range(32)]

gui = [[x for x in range(3)] for y in range(3)]

for x in range (3):
    for y in range (3):
        gui[x][y] = Button(tttframe2, font=("Calibri, 5"), width=18, height=12, command=lambda r=x, c=y:tictaotoe (r, c))
        gui[x][y].grid(row=x, column=y)

tttframe3 = Frame(tttframe)
tttframe3.grid(row=1, column=1)

ximg = PhotoImage(file="x.png")
oimg = PhotoImage(file="o.png")

xoff = 0
yoff = 0
pattern = 0 
p = 0

obtn = Button(tttframe3, text="", image=oimg, command=lambda m=1:changeto(m))
obtn.grid(row=0, column=0)
xbtn = Button(tttframe3, text="", image=ximg, command=lambda m=0:changeto(m))
xbtn.grid(row=0, column=1)

p1 = Label(tttframe3, text="Player 1 is O", font=("Courier", 10))
p1.grid(row=2, columnspan=2)
p2 = Label(tttframe3, text="Player 2 is X", font=("Courier", 10))
p2.grid(row=3, columnspan=2)

clearbtn = Button(tttframe3, text="Clear", font=("Courier", 15), command=clear)
clearbtn.grid(row=1, columnspan=2)


main.mainloop()