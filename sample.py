from tkinter import *

main = Tk()
main.title("Group C")

frame1 = Frame(main) #3x3 btn
frame1.grid(row=0, column=0)

frame2 = Frame(main) #shades btn
frame2.grid(row=0, column=1)

frame3 = Frame(main)
frame3.grid(row=1, columnspan=2) #colour btns 

frame4 = Frame(main)
frame4.grid(row=2, columnspan=2) #send btn

one = Button(frame1, text="FRAME 1", width=30, height=15, fg='black')
one.grid(row=1, column=1)

two = Button(frame2, text="FRAME 2", width=7, height=15, fg='blue')
two.grid(row=1, column=1)

three = Button(frame3, text="FRAME 3", width=38, height=2, fg='orange')
three.grid(row=1, column=1)

four = Button(frame4, text="FRAME 4", width=8, height=2, fg='red')
four.grid(row=1, column=1)

main.mainloop()