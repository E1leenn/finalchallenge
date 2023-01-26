from tkinter import * 

main = Tk()

titleframe = Frame(main)
titleframe.grid(row=0, columnspan=2, padx=2, pady=2)
contentframe = Frame(main)
contentframe.grid(row=1, column=0, padx=2, pady=2)
modeframe = Frame(main)
modeframe.grid(row=1, column=1, padx=2, pady=2)

titlefont = ("Fixedsys", 25)
title = Label(titleframe, text="Frame 1", font=titlefont, highlightbackground="#9b9655", highlightthickness=2, width=36)
title.grid(row=0, column=0)

content = Label(contentframe, text="Frame 2", font=titlefont, highlightbackground="#9b9655", highlightthickness=2, width=25, height=12)
content.grid(row=0, column=0)

mode = Label(modeframe, text="Frame 3", font=titlefont, highlightbackground="#9b9655", highlightthickness=2, width=10, height=5)
mode.grid(row=0, column=0)

main.mainloop()