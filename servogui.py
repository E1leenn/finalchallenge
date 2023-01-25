# Import required libraries
from gpiozero import AngularServo
from guizero import App, Slider, Text, ButtonGroup
from gpiozero.pins.pigpio import PiGPIOFactory

from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *
import tkinter.messagebox



# Create an instance of tkinter window
win = Tk()
style = Style()


factory = PiGPIOFactory()



win.title("Laser Maze")

# Define the geometry of the window
win.geometry("2000x1100")
# win.state('zoomed')

s = AngularServo(25, initial_angle = 0, min_pulse_width = 1/1000, max_pulse_width =2/1000
                , frame_width = 20/1000, pin_factory = factory, min_angle=-90, max_angle=90)

s1 = AngularServo(12 , initial_angle = 0, min_pulse_width = 1/1000, max_pulse_width =2/1000
                , frame_width = 20/1000, pin_factory = factory, min_angle=-90, max_angle=90)

s2 = AngularServo(24 , initial_angle = 75, min_pulse_width = 1/1000, max_pulse_width =2/1000
                , frame_width = 20/1000, pin_factory = factory, min_angle=-90, max_angle=90)


leftframe = Frame(win, width=200, height=200)
leftframe.grid(row=0, column=0)

rightframe = Frame(win, width=200, height=200)
rightframe.grid(row=0, column=1)

bottomframe = Frame(win, width=200, height=200)
bottomframe.grid(row=2, column=1)



# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("diagram.png"))
# resized_image = img.resize((300,400), Image.ANTIALIAS)
# new_image = ImageTk.PhotoImage(resized_image)
# new_image.show()
# img1 = img.resize(300,400)

# Create a Label Widget to display the text or Image
label = Label(leftframe, image = img)
label.pack()


counter_s = 0
counter_s1 = 0
counter_s2 = 0

def subtract():
    global counter_s 
    counter_s -=15
    s.angle = 0 + counter_s
    s.angle = int(s.angle - 15) 
    print("motor1: ", s.angle)
    
    
    if s.angle == -90:
        counter_s = -90
        
    
#     s1.angle = int(slider1.value)
#     print("motor2: ",s1.angle)
    
def addition():
    
    global counter_s 
    counter_s  +=15
    s.angle = 0 + counter_s 
    print("motor1:", s.angle)
    
    if s.angle == 90.0:
        counter_s  = 90.0
        tkinter.messagebox.showinfo("You have reached the maximum angle")




def subtract2():
    global counter_s1 
    counter_s1 -=15
    s1.angle = 0 + counter_s1 
    #s.angle = int(s.angle - 15) 
    print("motor2: ", s1.angle)
    
    
    if s1.angle == -90.0:
        counter_s1 = -90.0
        print("You have reached the minimum angle")
    
    #s1.angle = int(slider1.value)
    #print("motor2: ",s1.angle)
    
def addition2():
    global counter_s1
    counter_s1 +=15
    s1.angle = 0 + counter_s1
    print("motor2:", s1.angle)
    
    if s1.angle == 90.0:
        counter_s1 = 90.0
        print("You have reached the maximum angle")



def subtract3():
    global counter_s2 
    counter_s2 -=15
    s2.angle = 0 + counter_s2 
    #s.angle = int(s.angle - 15) 
    print("Polariser: ", s2.angle)
    
    
    if s2.angle == -90.0:
        counter_s2 = -90.0
        print("You have reached the minimum angle")
    
    #s1.angle = int(slider1.value)
    #print("motor2: ",s1.angle)
    
def addition3():
    global counter_s2
    counter_s2 +=15
    s2.angle = 0 + counter_s2
    print("Polariser:", s2.angle)
    
    if s2.angle == 90.0:
        counter_s2 = 90.0
        print("You have reached the maximum angle")
        
        
def reset_motor():
    s.angle = 0.0
    s1.angle = 0.0
    s2.angle = 75.0
    print(s.angle,s1.angle,s2.angle)

welcome = Label(bottomframe, text ="Welcome to the laser maze game!", font=("Arial", 25)).grid(row=2, column=1)

instructions = Label(bottomframe, text= "Here are a few instructions: \n 1) Your objective is to navigate the laser and hit the light sensor,\n 2) Play with the left and right buttons to turn the motor,\n 3) Hit the reset button to assign all the motors to its initial angle"
, font= ("Arial", 15)).grid(row=3, column=1)


motor1 = Label(rightframe, text ="Motor1").grid(row=3, column=1, padx=20, pady=20)
btn1 = Button(rightframe, text = '<--', command = subtract)
btn1.grid(row = 4, column = 1, pady = 10, padx = 20)

btn2 = Button(rightframe, text = '-->', command = addition)
btn2.grid(row = 4, column = 2, pady = 10, padx = 20)




motor2 =Label(rightframe, text ="Motor2").grid(row=3,column=4, padx=20, pady=20)
btn3 = Button(rightframe, text = '<--', command = subtract2)
btn3.grid(row = 4, column = 4, pady = 10, padx = 20)

btn4 = Button(rightframe, text = '-->', command = addition2)
btn4.grid(row = 4, column = 5, pady = 10, padx = 20)



motor3 =Label(rightframe, text ="Polariser").grid(row=6,column=3, padx=20, pady=20)
btn5 = Button(rightframe, text = '<--', command = subtract3)
btn5.grid(row = 8, column = 3, pady = 10, padx = 20)

btn6 = Button(rightframe, text = '-->', command = addition3)
btn6.grid(row = 9, column = 3, pady = 10, padx = 20)



btn9 = Button(rightframe, text = 'Reset', command = reset_motor)
btn9.grid(row = 15, column = 3, pady = 70, padx = 20)




win.mainloop()