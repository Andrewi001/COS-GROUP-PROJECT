# NEMUEL NUHYEL LAUSHI BHU/23/04/09/0046
# ISHAKU ANDREW  BHU/23/04/09/0050
# NDUKWE EMMANUEL KALU  BHU/23/04/09/0076
# EBENEHI SIMEON  BHU/23/04/09/0025
#

from tkinter import *


def buttonClick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)


def buttonclear():
    global operator
    operator = ""
    input_value.set("")


def buttonEqual():
    global operator
    result = str(eval(operator))
    input_value.set(result)
    operator = ""


window = Tk()
window.title("my_calculator")
operator = ""
input_value = StringVar()
display_text = Entry(window, font=("arial", 20, "bold"), textvariable=input_value, bd=20, insertwidth=4, bg="#F5F5F5",
                     justify=RIGHT)
display_text.grid(columnspan=4)

# calculator row 1

btn1 = Button(window, padx=16, bd=8, fg="white", font=("arial", 20, "bold"), text="1", background="#B2BEB5",
              command=lambda: buttonClick(1))
btn1.grid(row=1, column=0)

btn2 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="2", command=lambda: buttonClick(2))
btn2.grid(row=1, column=1)

btn3 = Button(window, padx=16, bd=8, fg="#F5F5F5", font=("arial", 20, "bold"), text="3", background="#B2BEB5",
              command=lambda: buttonClick(3))
btn3.grid(row=1, column=2)

btn_add = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="+",
                 command=lambda: buttonClick("+"))
btn_add.grid(row=1, column=3)

# calculator row 2

btn4 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="4", command=lambda: buttonClick(4))
btn4.grid(row=2, column=0)

btn5 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="5", command=lambda: buttonClick(5))
btn5.grid(row=2, column=1)

btn6 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="6", command=lambda: buttonClick(6))
btn6.grid(row=2, column=2)

btn_subtract = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="-",
                      command=lambda: buttonClick("-"))
btn_subtract.grid(row=2, column=3)

