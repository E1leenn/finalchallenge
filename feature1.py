from tkinter import *
from tkinter import messagebox
# import student_pub

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

main = Tk()

frame1 = Frame(main)
frame1.grid(rowspan=2, column=0)

btn = [[i for i in range (32)] for j in range (32)]
for i in range (32):
    for j in range (32):
        btn[i][j] = Button(frame1, font=("Calibri, 5"), width=1, height=1, bg="white")
        btn[i][j].grid(row=i, column=j)

frame2 = Frame(main)
frame2.grid(row=0, column=1, padx=15)

value = [[0 for i in range(32)] for j in range(32)]

gui = [[x for x in range(3)] for y in range(3)]

for x in range (3):
    for y in range (3):
        gui[x][y] = Button(frame2, font=("Calibri, 5"), width=18, height=12, command=lambda r=x, c=y:tictaotoe (r, c))
        gui[x][y].grid(row=x, column=y)

frame3 = Frame(main)
frame3.grid(row=1, column=1)

ximg = PhotoImage(file="x.png")
oimg = PhotoImage(file="o.png")

xoff = 0
yoff = 0
pattern = 0 
p = 0

xbtn = Button(frame3, text="", image=ximg, command=lambda m=0:changeto(m))
xbtn.grid(row=0, column=0)

obtn = Button(frame3, text="", image=oimg, command=lambda m=1:changeto(m))
obtn.grid(row=0, column=1)

clearbtn = Button(frame3, text="Clear", font=("Courier", 15), command=clear)
clearbtn.grid(row=1, columnspan=2)

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