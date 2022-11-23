from tkinter import *
from tkinter import ttk

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

def sendbtn():
  print(value)

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

def get_x_and_y(event):
   global lasx, lasy
   lasx, lasy = event.x, event.y

def paint(event):
    global lasx, lasy, value
    
    if colour == 0: 
        c.create_line((lasx,lasy, event.x, event.y),fill='grey99',width=4)  
    elif colour == 1:
        c.create_line((lasx,lasy, event.x, event.y),fill='grey88',width=4)
    elif colour == 2:
        c.create_line((lasx,lasy, event.x, event.y),fill='grey77',width=4)
    elif colour == 3: 
        c.create_line((lasx,lasy, event.x, event.y),fill='grey66',width=4)
    elif colour == 4:
        c.create_line((lasx,lasy, event.x, event.y),fill='grey44',width=4)
    elif colour == 5: 
        c.create_line((lasx,lasy, event.x, event.y),fill='grey33',width=4)
    elif colour == 6:
        c.create_line((lasx,lasy, event.x, event.y),fill='grey22',width=4)
    else: 
        c.create_line((lasx,lasy, event.x, event.y),fill='grey11',width=4)

    lasx, lasy = event.x, event.y

def clearbtn():
    c.delete('all')

main = Tk()
main.title("Group C")

#this variable to store the colour choice 
colour = 0

notebook = ttk.Notebook(main) #widget that manages a collection of windows/displays

tab1 = Frame(notebook) #new frame for tab 1
tab2 = Frame(notebook) #new frame for tab 2

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.grid(row=0, column = 0)

frame1 = Frame(tab1) #3x3 btn
frame1.grid(row=0, column=0)

frame2 = Frame(main) #shades btn
frame2.grid(row=0, column=1)

frame3 = Frame(main)
frame3.grid(row=1, columnspan=2) #colour btns 

frame4 = Frame(main)
frame4.grid(row=2, columnspan=2) #send btn

frame5 = Frame(tab2)
frame5.grid(row=0, column=0)

c = Canvas(tab2, width=443, height=380, bg='white')
c.grid(row=0, column=0)
# c.pack(anchor='nw', fill='both', expand=1)

c.bind('<Button-1>', get_x_and_y)
c.bind('<B1-Motion>',paint)

# 3x3 grid
button = [[j for j in range(32)] for i in range(32)]

value = [[0 for i in range(32)] for j in range(32)]
print("Value is {}".format(value))

for j in range (32):
  for i in range (32):
    button[i][j] = Button(frame1, font=("Calibri, 5"), width=1, height=1, bg='white', command=lambda r=i, c=j:whitebtn(r, c))
    button[i][j].grid(row=i, column=j)

#clear button
clear = Button(frame2, text="Clear", font=("Calibri, 10"), bg='grey99', width=13, height=2, command=clearbtn)
clear.grid(row=0, column=0)

#shades button
white = Button(frame2, text="White", font=("Calibri, 10"), bg='grey99', width=13, height=2, command=lambda m=0:change_colour(m))
white.grid(row=1, column=0)
grey1 = Button(frame2, text="Grey1", font=("Calibri, 10"), bg='grey88', width=13, height=2, command=lambda m=1:change_colour(m))
grey1.grid(row=2, column=0)
grey2 = Button(frame2, text="Grey2", font=("Calibri, 10"), bg='grey77', width=13, height=2, command=lambda m=2:change_colour(m))
grey2.grid(row=3, column=0)
grey3 = Button(frame2, text="Grey3", font=("Calibri, 10"), bg='grey66', width=13, height=2, command=lambda m=3:change_colour(m))
grey3.grid(row=4, column=0)
grey4 = Button(frame2, text="Grey4", font=("Calibri, 10"), bg='grey44', width=13, height=2, command=lambda m=4:change_colour(m))
grey4.grid(row=5, column=0)
grey5 = Button(frame2, text="Grey5", font=("Calibri, 10"), bg='grey33', fg='white', width=13, height=2, command=lambda m=5:change_colour(m))
grey5.grid(row=6, column=0)
grey6 = Button(frame2, text="Grey6", font=("Calibri, 10"), bg='grey11', fg='white', width=13, height=2, command=lambda m=6:change_colour(m))
grey6.grid(row=7, column=0)
black = Button(frame2, text="Black", font=("Calibri, 10"), bg='grey1', fg='white', width=13, height=2, command=lambda m=7:change_colour(m))
black.grid(row=8, column=0)

#colour button
allwhite = Button(frame3, text="All White",font=("Calibri, 12"), bg='white', width=13, height=2, command=allwht)
allwhite.grid(row=0, column=0)

allblack = Button(frame3, text="All Black",font=("Calibri, 12"), bg='black', fg='white', width=13, height=2, command=allblk)
allblack.grid(row=0, column=1)

xpattern = Button(frame3, text="X Pattern",font=("Calibri, 12"), bg='gold', width=13, height=2, command=pattern)
xpattern.grid(row=0, column=2)

seq = Button(frame3, text="Sequence",font=("Calibri, 12"), bg='#ff007f', width=13, height=2, command=ramseq)
seq.grid(row=0, column=3)

#send btn
send = Button(frame4, text="Send Image!", font=("Calibri, 12"), width=13, height=2, command=lambda :sendbtn())
send.grid(row=0, column=0)

main.mainloop()