import tkinter
import tkinter.messagebox
import tkinter.font as font
window=tkinter.Tk()


def nextr():
    window.destroy()
    import Game1

def nextg():
    window.destroy()
    import Game2

#main screen
window.configure(bg='black')
#Setting font size
myFont = font.Font(family = "Comic Sans MS",size=20,weight='bold')

#headings
var=tkinter.Label(window,text="Mind Twister",bg='black',fg='yellow')
var2=tkinter.Label(window,text="To Workout Your Mind !!",bg='black',fg='yellow')

#buttons
Btn=tkinter.Button(window,text='Colour Game',command=nextg)
Btn2=tkinter.Button(window,text='Number guessing',command=nextr)
Btn3=tkinter.Button(window,text='Quit',command=window.destroy)

var['font'] = myFont
var2['font']= myFont

Btn['font'] = myFont
Btn2['font']= myFont
Btn3['font']= myFont

#Setting Positions of buttons and heading
Btn.place(x=150,y=180)
Btn2.place(x=120,y=270)
Btn3.place(x=200,y=360)
var.place(x=150,y=20)
var2.place(x=80,y=80)


#setting Window's geometry
window.geometry("500x500")
window.mainloop()

