<<<<<<< Updated upstream
from tkinter import *


def whitebtn(i, j):
  global colour, value

  # print("i is {} and j is {}".format(i,j))  
  # print("i is {} and j is {}".format(type(i), type(j))) 
  if colour == 0:
    # print("In white")
    button[i][j].config(bg='grey99')
    value[i][j] = 0
  elif colour == 1: 
    # print("In grey 1")
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
    button[i][j].config(bg='grey11')
    value[i][j] = 70
  else: 
    button[i][j].config(bg='grey1')
    value[i][j] = 90

  # print("value is {}".format(value))
  #print("gridcolour is {}".format(value))

def sendbtn():
  print(value)

def change_colour(m): 
  global colour
  colour=m 

  print("colour is {}".format(colour))

def allwht():
  for j in range (32):
    for i in range (32):
      button[i][j].config(bg='white')
      value[i][j] = 0

def allblk():
  for j in range (32):
    for i in range (32):
      button[i][j].config(bg='black')
      value[i][j] = 90

def pattern():
  for j in range (32):
    for i in range (32):
      if i == j: 
        button[i][j].config(bg='grey')
        value[i][j] = 10
      elif i + j == 31: 
        button[i][j].config(bg='grey')
        value[i][j] = 10
      else:
        button[i][j].config(bg='white')



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
        button[i][j].config(bg='grey55')
        value[i][j] = 50 

       

main = Tk()
main.title("Group C")

#this variable to store the colour choice 
colour = 0

frame1 = Frame(main) #3x3 btn
frame1.grid(row=0, column=0)

frame2 = Frame(main) #shades btn
frame2.grid(row=0, column=1)

frame3 = Frame(main)
frame3.grid(row=1, columnspan=2) #colour btns 

frame4 = Frame(main)
frame4.grid(row=2, columnspan=2) #send btn

# 3x3 grid
button = [[j for j in range(32)] for i in range(32)]

value = [[0 for i in range(32)] for j in range(32)]
print("Value is {}".format(value))


for j in range (32):
  for i in range (32):
    button[i][j] = Button(frame1, font=("Calibri, 5"), width=1, height=1, command=lambda r=i, c=j:whitebtn(r, c))
    button[i][j].grid(row=i, column=j)

    #print(button)

# #shades button
white = Button(frame2, text="White", font=("Calibri, 10"), width=13, height=2, command=lambda m=0:change_colour(m))
white.grid(row=0, column=0)
grey1 = Button(frame2, text="Grey1", font=("Calibri, 10"), bg='#f3f3f3', width=13, height=2, command=lambda m=1:change_colour(m))
grey1.grid(row=1, column=0)
grey2 = Button(frame2, text="Grey2", font=("Calibri, 10"), bg='#dedede', width=13, height=2, command=lambda m=2:change_colour(m))
grey2.grid(row=2, column=0)
grey3 = Button(frame2, text="Grey3", font=("Calibri, 10"), bg='#cccccc', width=13, height=2, command=lambda m=3:change_colour(m))
grey3.grid(row=3, column=0)
grey4 = Button(frame2, text="Grey4", font=("Calibri, 10"), bg='#999999', width=13, height=2, command=lambda m=4:change_colour(m))
grey4.grid(row=4, column=0)
grey5 = Button(frame2, text="Grey5", font=("Calibri, 10"), bg='#666666', fg='white', width=13, height=2, command=lambda m=5:change_colour(m))
grey5.grid(row=5, column=0)
grey6 = Button(frame2, text="Grey6", font=("Calibri, 10"), bg='#222222', fg='white', width=13, height=2, command=lambda m=6:change_colour(m))
grey6.grid(row=6, column=0)
black = Button(frame2, text="Black", font=("Calibri, 10"), bg='black', fg='white', width=13, height=2, command=lambda m=7:change_colour(m))
black.grid(row=7, column=0)

# # #colour button
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

#print("Button is {}".format(button))


=======
from tkinter import *


def whitebtn(i, j):
  global colour, value

  # print("i is {} and j is {}".format(i,j))  
  # print("i is {} and j is {}".format(type(i), type(j))) 
  if colour == 0:
    # print("In white")
    button[i][j].config(bg='grey99')
    value[i][j] = 0
  elif colour == 1: 
    # print("In grey 1")
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
    button[i][j].config(bg='grey11')
    value[i][j] = 70
  else: 
    button[i][j].config(bg='grey1')
    value[i][j] = 90

  # print("value is {}".format(value))
  #print("gridcolour is {}".format(value))

def sendbtn():
  print(value)

def change_colour(m): 
  global colour
  colour=m 

  print("colour is {}".format(colour))

def allwht():
  for j in range (32):
    for i in range (32):
      button[i][j].config(bg='white')
      value[i][j] = 0

def allblk():
  for j in range (32):
    for i in range (32):
      button[i][j].config(bg='black')
      value[i][j] = 90

def pattern():
  for j in range (32):
    for i in range (32):
      if i == j: 
        button[i][j].config(bg='grey')
        value[i][j] = 10
      elif i + j == 31: 
        button[i][j].config(bg='grey')
        value[i][j] = 10


def ramseq():
  for j in range (32):
    for i in range (32):
      if i == 0: 
        button[i][j].config(bg='grey99')
        value[i][j] = 0
      elif i == 2:
        button[i][j].config(bg='grey88')
        value[i][j] = 20
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
        button[i][j].config(bg='grey11')
        value[i][j] = 70
      else: 
        button[i][j].config(bg='grey1')
        value[i][j] = 90

main = Tk()
main.title("Group C")

#this variable to store the colour choice 
colour = 0

frame1 = Frame(main) #3x3 btn
frame1.grid(row=0, column=0)

frame2 = Frame(main) #shades btn
frame2.grid(row=0, column=1)

frame3 = Frame(main)
frame3.grid(row=1, columnspan=2) #colour btns 

frame4 = Frame(main)
frame4.grid(row=2, columnspan=2) #send btn

# 3x3 grid
button = [[j for j in range(32)] for i in range(32)]

value = [[0 for i in range(32)] for j in range(32)]
print("Value is {}".format(value))


for j in range (32):
  for i in range (32):
    button[i][j] = Button(frame1, font=("Calibri, 5"), width=1, height=1, command=lambda r=i, c=j:whitebtn(r, c))
    button[i][j].grid(row=i, column=j)

    #print(button)

# #shades button
white = Button(frame2, text="White", font=("Calibri, 10"), width=13, height=2, command=lambda m=0:change_colour(m))
white.grid(row=0, column=0)
grey1 = Button(frame2, text="Grey1", font=("Calibri, 10"), bg='#f3f3f3', width=13, height=2, command=lambda m=1:change_colour(m))
grey1.grid(row=1, column=0)
grey2 = Button(frame2, text="Grey2", font=("Calibri, 10"), bg='#dedede', width=13, height=2, command=lambda m=2:change_colour(m))
grey2.grid(row=2, column=0)
grey3 = Button(frame2, text="Grey3", font=("Calibri, 10"), bg='#cccccc', width=13, height=2, command=lambda m=3:change_colour(m))
grey3.grid(row=3, column=0)
grey4 = Button(frame2, text="Grey4", font=("Calibri, 10"), bg='#999999', width=13, height=2, command=lambda m=4:change_colour(m))
grey4.grid(row=4, column=0)
grey5 = Button(frame2, text="Grey5", font=("Calibri, 10"), bg='#666666', fg='white', width=13, height=2, command=lambda m=5:change_colour(m))
grey5.grid(row=5, column=0)
grey6 = Button(frame2, text="Grey6", font=("Calibri, 10"), bg='#222222', fg='white', width=13, height=2, command=lambda m=6:change_colour(m))
grey6.grid(row=6, column=0)
black = Button(frame2, text="Black", font=("Calibri, 10"), bg='black', fg='white', width=13, height=2, command=lambda m=7:change_colour(m))
black.grid(row=7, column=0)

# # #colour button
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

#print("Button is {}".format(button))


>>>>>>> Stashed changes
main.mainloop()