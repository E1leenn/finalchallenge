from cgi import print_arguments
from tkinter import *

def whitebtn(i, j):
  global colour   
  if colour == 0:
    button[i][j].config(bg='white')
  elif colour == 1: 
    button[i][j].config(bg='#f3f3f3')
  elif colour == 2:
    button[i][j].config(bg='#dedede')
  elif colour == 3: 
    button[i][j].config(bg='#cccccc')
  elif colour == 4:
    button[i][j].config(bg='#999999')  
  elif colour == 5: 
    button[i][j].config(bg='#666666')
  elif colour == 6:
    button[i][j].config(bg='#222222')
  else: 
    button[i][j].config(bg='black')

def change_colour(m): 
  global colour
  colour=m 

  print("colour is {}".format(colour))

def allwht():
  for j in range (32):
    for i in range (32):
      button[i][j].config(bg='white')

def allblk():
  for j in range (32):
    for i in range (32):
      button[i][j].config(bg='black')

def pattern():
  for j in range (32):
    for i in range (32):
      if i == j: 
        button[i][j].config(bg='grey')
      elif i + j == 2: 
        button[i][j].config(bg='grey')


main = Tk()

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

for j in range (32):
  for i in range (32):
    button[i][j] = Button(frame1, width=1,height=1, command=lambda r=i, c=j:whitebtn(r, c))
    button[i][j].grid(row=i, column=j)

    print(button)

# #shades button
white = Button(frame2, text="White", font=("Calibri, 5"), command=lambda m=0:change_colour(m))
white.grid(row=0, column=0)
grey1 = Button(frame2, text="Grey1", font=("Calibri, 5"), bg='#f3f3f3', command=lambda m=1:change_colour(m))
grey1.grid(row=1, column=0)
grey2 = Button(frame2, text="Grey2", font=("Calibri, 5"), bg='#dedede', command=lambda m=2:change_colour(m))
grey2.grid(row=2, column=0)
grey3 = Button(frame2, text="Grey3", font=("Calibri, 5"), bg='#cccccc', command=lambda m=3:change_colour(m))
grey3.grid(row=3, column=0)
grey4 = Button(frame2, text="Grey4", font=("Calibri, 5"), bg='#999999', command=lambda m=4:change_colour(m))
grey4.grid(row=4, column=0)
grey5 = Button(frame2, text="Grey5", font=("Calibri, 5"), bg='#666666', fg='white', command=lambda m=5:change_colour(m))
grey5.grid(row=5, column=0)
grey6 = Button(frame2, text="Grey6", font=("Calibri, 5"), bg='#222222', fg='white', command=lambda m=6:change_colour(m))
grey6.grid(row=6, column=0)
black = Button(frame2, text="Black", font=("Calibri, 5"), bg='black', fg='white', command=lambda m=7:change_colour(m))
black.grid(row=7, column=0)

# # #colour button
allwhite = Button(frame3, text="All White",font=("Calibri, 5"), bg='white', command=allwht)
allwhite.grid(row=0, column=0)

allblack = Button(frame3, text="All Black",font=("Calibri, 5"), bg='black', fg='white', command=allblk)
allblack.grid(row=0, column=1)

xpattern = Button(frame3, text="X Pattern",font=("Calibri, 5"), bg='gold', command=pattern)
xpattern.grid(row=0, column=2)

seq = Button(frame3, text="Sequence",font=("Calibri, 5"), bg='#ff007f')
seq.grid(row=0, column=3)

#send btn
send = Button(frame4, text="Send Imaged!", font=("Calibri, 5"))
send.grid(row=0, column=0)

print("Button is {}".format(button))

main.mainloop()