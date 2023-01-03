from tkinter import *
# import student_pub

def changeto(m):
    global pattern
    pattern = m 
    print("pattern is", pattern)

def tictaotoe(x,y):
    global pattern, xoff, yoff

    if x == 0 & y == 0:
        xoff = 0
        yoff = 0
    elif x == 0 & y == 1:
        xoff = 0
        yoff = 12
    elif x == 0 & y == 2:
        xoff = 0
        yoff = 24
    elif x == 1 & y == 0:
        xoff = 12
        yoff = 0 
    elif x == 1 & y == 1: 
        xoff = 12
        yoff = 12
    elif x == 1 & y == 2: 
        xoff= 12
        yoff = 24 
    elif x == 2 & y == 0: 
        xoff = 24
        yoff = 0 
    elif x == 2 & y == 1: 
        xoff = 12 
        yoff = 24 
    else: 
        xoff = 24
        yoff = 24

    if pattern == 0: 
        var = "X"
        gui[x][y].config(text=var)

    else:
        var = "O"
        gui[x][y].config(text=var)

        for i in range (32):
            for j in range (32):
                if j == 1 + yoff: 
                    if i == 2 + xoff: 
                        btn[i][j].config(bg="black")
                    elif i == 3 + xoff: 
                        btn[i][j].config(bg="black")
                    elif i == 4 + xoff: 
                        btn[i][j].config(bg="black")
                    elif i == 5 + xoff: 
                        btn[i][j].config(bg="black")
                elif j == 6 + yoff: 
                    if i == 2 + xoff: 
                        btn[i][j].config(bg="black")
                    elif i == 3 + xoff: 
                        btn[i][j].config(bg="black")
                    elif i == 4 + xoff: 
                        btn[i][j].config(bg="black")
                    elif i == 5 + xoff: 
                        btn[i][j].config(bg="black")
                elif i == 1 + xoff: 
                    if j == 2 + yoff: 
                        btn[i][j].config(bg="black")
                    elif j == 3 + yoff: 
                        btn[i][j].config(bg="black")
                    elif j == 4 + yoff: 
                        btn[i][j].config(bg="black")
                    elif j == 5 + yoff: 
                        btn[i][j].config(bg="black")
                elif i == 6 + xoff: 
                    if j == 2 + yoff: 
                        btn[i][j].config(bg="black")
                    elif j == 3 + yoff: 
                        btn[i][j].config(bg="black")
                    elif j == 4 + yoff: 
                        btn[i][j].config(bg="black")
                    elif j == 5 + yoff: 
                        btn[x][y].config(bg="black")


main = Tk()

frame1 = Frame(main)
frame1.grid(rowspan=2, column=0)


btn = [[i for i in range (32)] for j in range (32)]
for i in range (32):
    for j in range (32):
        btn[i][j] = Button(frame1, font=("Calibri, 5"), width=1, height=1)
        btn[i][j].grid(row=i, column=j)

frame2 = Frame(main)
frame2.grid(row=0, column=1, padx=15)

value = [[0 for i in range(32)] for j in range(32)]
gui = [[x for x in range(3)] for y in range(3)]

for x in range (3):
    for y in range (3):
        gui[x][y] = Button(frame2, font=("Calibri, 5"), width=18, height=12, command=lambda r=x, c=y:tictaotoe(r, c))
        gui[x][y].grid(row=x, column=y)

frame3 = Frame(main)
frame3.grid(row=1, column=1)

x = PhotoImage(file="x.png")
o = PhotoImage(file="o.png")

xoff = 0
yoff = 0

pattern = 0 
xbtn = Button(frame3, text="", image=x, command=lambda m=0:changeto(m))
xbtn.grid(row=0, column=0)

obtn = Button(frame3, text="", image=o, command=lambda m=1:changeto(m))
obtn.grid(row=0, column=1)


## black border 
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
        
print(value)
# student_pub.pubpic(value)

main.mainloop()




