from tkinter import * 


def changetoX(m):
    global pattern 

    if pattern == 0: 
        for x in range (8):
            for y in range (8):
                if x == y:
                    btn[x][y].config(bg="black")
                elif x + y == 7:
                    btn[x][y].config(bg="black")
                else: 
                    btn[x][y].config(bg="white")
                

def changetoO(m):
    global pattern 
    for x in range(8):
        for y in range (8):
            btn[x][y].config(bg="white")

    if pattern == 0: 
        for x in range (8):
            for y in range (8):
                if y == 1: 
                    if x == 2: 
                        btn[x][y].config(bg="black")
                    elif x == 3: 
                        btn[x][y].config(bg="black")
                    elif x == 4: 
                        btn[x][y].config(bg="black")
                    elif x == 5: 
                        btn[x][y].config(bg="black")
                elif y == 6: 
                    if x == 2: 
                        btn[x][y].config(bg="black")
                    elif x == 3: 
                        btn[x][y].config(bg="black")
                    elif x == 4: 
                        btn[x][y].config(bg="black")
                    elif x == 5: 
                        btn[x][y].config(bg="black")
                elif x == 1: 
                    if y == 2: 
                        btn[x][y].config(bg="black")
                    elif y == 3: 
                        btn[x][y].config(bg="black")
                    elif y == 4: 
                        btn[x][y].config(bg="black")
                    elif y == 5: 
                        btn[x][y].config(bg="black")
                elif x == 6: 
                    if y == 2: 
                        btn[x][y].config(bg="black")
                    elif y == 3: 
                        btn[x][y].config(bg="black")
                    elif y == 4: 
                        btn[x][y].config(bg="black")
                    elif y == 5: 
                        btn[x][y].config(bg="black")

main = Tk()

btn = [[x for x in range (8)] for y in range (8)]
for x in range (8):
    for y in range (8):
        btn[x][y] = Button(main, font=("Calibri, 5"), width=5, height=3)
        btn[x][y].grid(row=x, column=y)

pattern = 0

x = Button(main, font=("Calivri, 15"), text="X", command=lambda m=0:changetoX(m))
x.grid(row=10, columnspan=10, padx=5, pady=5)

o = Button(main, font=("Calivri, 15"), text="O", command=lambda m=0:changetoO(m))
o.grid(row=11, columnspan=10, padx=5, pady=5)

main.mainloop()