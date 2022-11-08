# 32 x 32 GUI Documentation 
This documentation is an introduction about the 32 x 32 GUI and its features. 

# Setting Up The GUI
To create a tkinter GUI, we need to import the tkinter library. 
```
from tkinter import *
```

To create a window with our group title. 
```
main = Tk()
main.title("Group C")
```

For the window to stay on the screen, we need to loop it. 
```
main.mainloop()
```

Output <br>
![](images/window.png)

# Frame Function
We are using the frame function to group and organize the widget to make it neater so that it is user friendly.

Frame1 is to indicate the first frame for the 32x32 grid.
```
frame1 = Frame(main)
frame1.grid(row=0, column=0)
```
Frame2 is to indicate the second frame for the shades buttons. 
```
frame2 = Frame(main) 
frame2.grid(row=0, column=1)
```
Frame 3 is to indicate the third frame for the features buttons. 
```
frame3 = Frame(main)
frame3.grid(row=1, columnspan=2)
```
Frame4 is to indicate the fourth frame for the send button. 
```
frame4 = Frame(main)
frame4.grid(row=2, columnspan=2)
```
Output <br>
![](images/frameEXAMPLE.png)

# Create 32 x 32 Buttons
We are using a list of list to create a 32 x 32 buttons. 
```
button = [[j for j in range(32)] for i in range(32)]

for j in range (32):
  for i in range (32):
    button[i][j] = Button(frame1, font=("Calibri, 5"), width=1, height=1)
    button[i][j].grid(row=i, column=j)
```
Output <br>
![](images/whitebtns.png)

# Create Shades Buttons
Below is the codes to create shades buttons. Change the text and background colour accordingly to get different shades buttons. 
```
white = Button(frame2, text="White", font=("Calibri, 10"), width=13, height=2)
white.grid(row=0, column=0)

grey1 = Button(frame2, text="Grey1", font=("Calibri, 10"), bg='#f3f3f3', width=13, height=2)
grey1.grid(row=1, column=0)

grey2 = Button(frame2, text="Grey2", font=("Calibri, 10"), bg='#dedede', width=13, height=2)
grey2.grid(row=2, column=0)

grey3 = Button(frame2, text="Grey3", font=("Calibri, 10"), bg='#cccccc', width=13, height=2)
grey3.grid(row=3, column=0)

grey4 = Button(frame2, text="Grey4", font=("Calibri, 10"), bg='#999999', width=13, height=2)
grey4.grid(row=4, column=0)

grey5 = Button(frame2, text="Grey5", font=("Calibri, 10"), bg='#666666', fg='white', width=13, height=2)
grey5.grid(row=5, column=0)

grey6 = Button(frame2, text="Grey6", font=("Calibri, 10"), bg='#222222', fg='white', width=13, height=2)
grey6.grid(row=6, column=0)

black = Button(frame2, text="Black", font=("Calibri, 10"), bg='black', fg='white', width=13, height=2)
black.grid(row=7, column=0)
```
Output <br>
![](images/colour%20btns.png)

## Assign function to the 32x32 buttons and shades Buttons
Create a variable to store colour value. 
```
colour = 0
```
Use Lambda Function to ...?
```
def change_colour(m): 
  global colour
  colour=m 
```
Add the command to the shades buttons. 
```
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
```
Use if else statement to create fucntion for the white buttons. 
```
def whitebtn(i, j):
  global colour

  if colour == 0:
    button[i][j].config(bg='grey99')
  elif colour == 1: 
    button[i][j].config(bg='grey88')
  elif colour == 2:
    button[i][j].config(bg='grey77')
  elif colour == 3: 
    button[i][j].config(bg='grey66')
  elif colour == 4:
    button[i][j].config(bg='grey44')  
  elif colour == 5: 
    button[i][j].config(bg='grey33')
  elif colour == 6:
    button[i][j].config(bg='grey11')
  else: 
    button[i][j].config(bg='grey1')
```
Add command to the button codes. 
```
button = [[j for j in range(32)] for i in range(32)]

for j in range (32):
  for i in range (32):
    button[i][j] = Button(frame1, font=("Calibri, 5"), width=1, height=1, command=lambda r=i, c=j:whitebtn(r, c))
    button[i][j].grid(row=i, column=j)
```

# Features Buttons 
To create the features buttons, the code is similar to the shades button. Change the text and background colour accordingly. 
```
allwhite = Button(frame3, text="All White",font=("Calibri, 12"), bg='white', width=13, height=2)
allwhite.grid(row=0, column=0)

allblack = Button(frame3, text="All Black",font=("Calibri, 12"), bg='black', fg='white', width=13, height=2)
allblack.grid(row=0, column=1)

xpattern = Button(frame3, text="X Pattern",font=("Calibri, 12"), bg='gold', width=13, height=2)
xpattern.grid(row=0, column=2)

seq = Button(frame3, text="Sequence",font=("Calibri, 12"), bg='#ff007f', width=13, height=2)
seq.grid(row=0, column=3)
```
Add commands to each of the features function. <br>
Below are the function codes for All White and All Black. 
```
def allwht():
  for j in range (32):
    for i in range (32):
      button[i][j].config(bg='white')

def allblk():
  for j in range (32):
    for i in range (32):
      button[i][j].config(bg='black')
```
Below are the function codes for X Pattern. 
```
def pattern():
  for j in range (32):
    for i in range (32):
      if i == j: 
        button[i][j].config(bg='grey')
      elif i + j == 31: 
        button[i][j].config(bg='grey')
```
Below are the function codes for Sequence. 
```
def ramseq():
  for j in range (32):
    for i in range (32):
      if i == 0: 
        button[i][j].config(bg='grey99')
      elif i == 2:
        button[i][j].config(bg='grey88')
      elif colour == 3: 
        button[i][j].config(bg='grey66')
      elif colour == 4:
        button[i][j].config(bg='grey44')  
      elif colour == 5: 
        button[i][j].config(bg='grey33')
      elif colour == 6:
        button[i][j].config(bg='grey11')
      else: 
        button[i][j].config(bg='grey1')
```
Output <br>
![](images/features%20btn.png)

# Send Button 
When the send button is pressed, it will output the value of the different shades. 
Below is the codes to create send button. 
```
send = Button(frame4, text="Send Image!", font=("Calibri, 12"), width=13, height=2)
send.grid(row=0, column=0)
```
## Assign function to the send button. 
First, create a variable to store the value. 
```
value = [[0 for i in range(32)] for j in range(32)]
```
Next, add value to the 32 x 32 button's function, shades button's function and features button's function. 
Below are the code for 32x32 buttons after adding the value. 
```
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
    button[i][j].config(bg='grey11')
    value[i][j] = 70
  else: 
    button[i][j].config(bg='grey1')
    value[i][j] = 90
```
Below are the code for All White and All Black button after adding the value. 
```
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
```
Below are the code for X Pattern button after adding the value. 
```
def pattern():
  for j in range (32):
    for i in range (32):
      if i == j: 
        button[i][j].config(bg='grey')
        value[i][j] = 10
      elif i + j == 31: 
        button[i][j].config(bg='grey')
        value[i][j] = 10
```
Below are the code for sequence after adding the value. 
```
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
```
Function code for send button. 
```
def sendbtn():
  print(value)
```
Output <br>
![](images/send%20btn.png)

# The Final Output of GUI 
![](images/32gui.png)