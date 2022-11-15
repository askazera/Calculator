'''

Python Calculator using GUI (Graphical User Interface)
'''

from tkinter import *


# creating a blank screen
win = Tk()
win.geometry('312x324')
win.resizable(height=None, width=None)
win.title('Calculator')

expression = '' # a calculator starts with no value, blank space waiting to receive a value

#declaring all inputs as a string
input_text = StringVar()


def btn_click(value):  # function to insert the values (ex: numbers, operations)
    global expression
    expression += str(value)
    input_text.set(expression)


def btn_clear():
    global expression
    expression = ''
    input_text.set(expression)


def btn_equal(): # when we press the equal button, the eval calculates de operation for us
    global expression
    result = str(eval(expression)) # it must be a string since we have special caracteres to do the operations
    input_text.set(result)


# creating a first frame on the top, to input field
# first you have to create a frame, after you create the field to receive the values


input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)

input_frame.pack(side=TOP)

# creating the input field to receive all the values bellow


input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)

# a new frame, to insert all the bottons below
btns_frame = Frame(win, width=312, height=272.5, bg="grey")

btns_frame.pack()

# first row, one for clear botton and another one for a divide botton operation

Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

# second row

Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
       cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# third row

Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: btn_click('-')).grid(row=2, column=3, padx=1, pady=1)

# fourth row

Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: btn_click('+')).grid(row=3, column=3, padx=1, pady=1)

# fourth row

Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
# use columspan to get 2 spaces, colum 0 and 1, so the button get larger

Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: btn_click('.')).grid(row=4, column=2, padx=1, pady=1)

Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: btn_equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop() #call the screen