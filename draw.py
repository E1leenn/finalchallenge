from tkinter import *
from tkinter import ttk
# from student_pub import *

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
  #print(value)
  print(canvasdraw)
  # pubpic(value)
  
def change_colour(m): 
  global colour
  colour=m 

  print("colour is {}".format(colour))

def allwht():
  for j in range (32):
    for i in range (32):
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
    #print(value)
    print(canvasdraw)

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
    if lasx >= 0 and lasx <= 575 and lasy >= 0 and lasy <= 575:
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
    #f0(18)
    for i in range(0, 576, 18):
      list3 = []
      for t in range(0 , 576, 18):
        #list3 = []
        #f0(t, i)
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
    for i in range(x ,18+x):
      for t in range(y ,18+y):
        list.append(canvasdraw[i][t])
    list0 = list
    freq = min(set(list0), key = list0.count) #using min instead cause if max almost everytime will get 0,harder for the draw to show; once the 18x18 grid got 1 value change, then return that value
                                              #Link: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    #list1.append(freq)
    return freq 

def clearbtn():
    c.delete('all')

def tictactoe():
    frame2.destroy()
    frame3.destroy()
    frame4.destroy()

main = Tk()
main.title("Group C")

notebook = ttk.Notebook(main) #widget that manages a collection of windows/displays

tab1 = Frame(notebook) #new frame for tab 1
tab2 = Frame(notebook) #new frame for tab 2
tab3 = Frame(notebook) #new frame for tab 3

notebook.add(tab1,text="Grid")
notebook.add(tab2,text="Draw")
# notebook.add(tab3, text="tictactoe")
notebook.grid(row=0, column = 0)

frame1 = Frame(tab1, width=800, height=800) 
frame1.grid(row=0, column=0)

frame2 = Frame(main) #shades btn
frame2.grid(row=0, column=1)

frame3 = Frame(main)
frame3.grid(row=1, columnspan=2) #colour btns 

frame4 = Frame(main)
frame4.grid(row=2, columnspan=2) #send btn

frame5 = Frame(tab2) # draw canvas 
frame5.grid(row=0, column=0) 

# frame6 = Frame(tab3) # tictactoe
# frame6.grid(row=0, column=0)

c = Canvas(tab2, width=576, height=576, bg='white')  
c.grid(row=0, column=0)

c.bind('<Button-1>', get_x_and_y)
c.bind('<B1-Motion>',paint)
c.bind('<Enter>', get_x_and_y)

#this variable to store the colour choice 
colour = 0
canvasdraw = [[0 for i in range(576)] for j in range(576)]  # save eventxy into an array 

# 32x32 grid
button = [[j for j in range(32)] for i in range(32)]

value = [[0 for i in range(32)] for j in range(32)]
# print("Value is {}".format(value))

for j in range (32):
  for i in range (32):
    button[i][j] = Button(frame1, font=("Calibri, 5"), width=1, height=1, bg='white', command=lambda r=i, c=j:whitebtn(r, c))
    button[i][j].grid(row=i, column=j)


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

#save button
savebtn = Button(frame2, text="Save", font=("Calibri, 10"), bg='light blue', fg='black', width=13, height=2, command=save_img)
savebtn.grid(row=9, column=0)

#colour button
allwhite = Button(frame3, text="All White",font=("Calibri, 12"), bg='white', width=13, height=2, command=allwht)
allwhite.grid(row=0, column=0)

allblack = Button(frame3, text="All Black",font=("Calibri, 12"), bg='black', fg='white', width=13, height=2, command=allblk)
allblack.grid(row=0, column=1)

clear = Button(frame3, text="Clear",font=("Calibri, 12"), bg='gold', width=13, height=2, command=clearbtn)
clear.grid(row=0, column=2)

# 


#send btn
send = Button(frame4, text="Send Image!", font=("Calibri, 12"), width=13, height=2, command=lambda :sendbtn())
send.grid(row=0, column=0)

main.mainloop()
