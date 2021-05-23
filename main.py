import math
from tkinter import *
import datetime

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
# myWindow = Tk()
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
reps = 0


def raise_window(window):
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


def resetTimer():
    myWindow.after_cancel(timer)
    global reps
    button1['state'] = 'active'
    reps = 0
    myCanvas.itemconfig(textCanvas, text='00:00:00')
    mainLabel.config(text='TIMER')
    tickLabel.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #

def timeStart():
    global reps
    reps += 1
    # raise_window(myWindow)
    button1['state'] = 'disabled'
    if reps % 8 == 0:
        countDown(LONG_BREAK_MIN * 60)
        mainLabel.config(text='LONG BREAK')
    elif reps % 2 == 0:
        countDown(SHORT_BREAK_MIN * 60)
        mainLabel.config(text='SHORT BREAK')
    else:
        countDown(WORK_MIN * 60)
        mainLabel.config(text='W$RK')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countDown(time):
    # time=25*60*60
    pr = str(datetime.timedelta(seconds=time))

    if time > 0:
        global timer
        timer = myWindow.after(1000, countDown, time - 1)
        myCanvas.itemconfig(textCanvas, text=pr)
    else:
        timeStart()
        marks = ''
        for i in range(math.floor(reps / 2)):
            marks += '✔'
        mainLabel.config(text='W$RK')
        tickLabel.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
myWindow = Tk()
myWindow.title("Pomodoro")
myWindow.config(width='400', height=400, bg=YELLOW, padx=50, pady=50)
# Label 1
mainLabel = Label(text='TIMER', pady=20, fg=GREEN)
mainLabel.config(font=(FONT_NAME, 35, 'bold'), bg="#f7f5dd")
mainLabel.grid(column=1, row=0)

# Label 2
tickLabel = Label(text='', pady=20, fg=GREEN)
tickLabel.config(font=(FONT_NAME, 15, 'bold'), bg=YELLOW)
tickLabel.grid(column=1, row=2)
myCanvas = Canvas(width=200, height=224)

# Image
myCanvas.config(bg="#f7f5dd")
img = PhotoImage(file='tomato.png')
myCanvas.create_image(100, 112, image=img)
textCanvas = myCanvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 10, 'bold'), fill='white')
myCanvas.grid(column=1, row=1)

# Button1
button1 = Button(text='Start', padx=0, pady=0, bg='white', font=(FONT_NAME, 9), command=timeStart)
button1.grid(column=0, row=2)
# Button2
button2 = Button(text='Reset', padx=0, pady=0, bg='white', font=(FONT_NAME, 9), command=resetTimer)
button2.grid(column=2, row=2)
# countDown(5)
myWindow.mainloop()
