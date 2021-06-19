from tkinter import*
import tkinter

# styles for the gui window
window = tkinter.Tk()
window.geometry("312x324")
window.resizable(0,0) # prevent from resizing the window
window.title("Cool Calulator")

def btn_click(item):
    global expression 
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression 
    expression = ""
    input_text.set("")

def btn_equal():
    try:
        global expression 
        total = str(eval(expression))
        input_text.set(total)
        expression = ""
    except:
        input_text.set("error")
        expression=""

expression = ""
input_text = StringVar()

input_Frame = Frame(window,width=312,height=50,bd=0, highlightbackground="black", highlightcolor="black",highlightthickness=1)
input_Frame.pack(side=TOP)

input_field = Entry(input_Frame, font=('arial', 18, 'bold'),textvariable= input_text , width=50, bg="#fff", bd =0,justify= CENTER)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) # internal padding

btns_frame = Frame(window,width=312, height=272.5, bg = "#73467e")
btns_frame.pack()

###   zero row
clear = Button(btns_frame, text="C", fg="black",width=32,height=3,bd=0,bg="#b676c7",cursor="hand2",command=btn_clear).grid(row=1,columnspan=3)
devide = Button(btns_frame, text="/", fg="black",width=10,height=3,bd=0,bg="#413569",cursor="hand2",command=lambda: btn_click("/")).grid(row=1,column=3)


###   first row
seven = Button(btns_frame, text="7", fg="black",width=10,height=3,bd=0,bg="#73467e",cursor="hand2",command=lambda: btn_click(7)).grid(row=2,column=0)
eight = Button(btns_frame, text="8", fg="black",width=10,height=3,bd=0,bg="#73467e",cursor="hand2",command=lambda: btn_click(8)).grid(row=2,column=1)
nine = Button(btns_frame, text="9", fg="black",width=10,height=3,bd=0,bg="#73467e",cursor="hand2",command=lambda: btn_click(9)).grid(row=2,column=2)
multiply = Button(btns_frame, text="*", fg="black",width=10,height=3,bd=0,bg="#413569",cursor="hand2",command=lambda: btn_click("*")).grid(row=2,column=3)

###   2nd row
four = Button(btns_frame, text="4", fg="black",width=10,height=3,bd=0,bg="#73467e",cursor="hand2",command=lambda: btn_click(4)).grid(row=3,column=0)
five = Button(btns_frame, text="5", fg="black",width=10,height=3,bd=0,bg="#73467e",cursor="hand2",command=lambda: btn_click(5)).grid(row=3,column=1)
six = Button(btns_frame, text="6", fg="black",width=10,height=3,bd=0,bg="#73467e",cursor="hand2",command=lambda: btn_click(6)).grid(row=3,column=2)
minus = Button(btns_frame, text="-", fg="black",width=10,height=3,bd=0,bg="#413569",cursor="hand2",command=lambda: btn_click("-")).grid(row=3,column=3)

###   3rd row
one = Button(btns_frame, text="1", fg="black",width=10,height=3,bd=0,bg="#73467e",cursor="hand2",command=lambda: btn_click(1)).grid(row=4,column=0)
two = Button(btns_frame, text="2", fg="black",width=10,height=3,bd=0,bg="#73467e",cursor="hand2",command=lambda: btn_click(2)).grid(row=4,column=1)
three = Button(btns_frame, text="3", fg="black",width=10,height=3,bd=0,bg="#73467e",cursor="hand2",command=lambda: btn_click(3)).grid(row=4,column=2)
plus = Button(btns_frame, text="+", fg="black",width=10,height=3,bd=0,bg="#413569",cursor="hand2",command=lambda: btn_click("+")).grid(row=4,column=3)

###   4th row
zero = Button(btns_frame, text="0", fg="black",width=21,height=3,bd=0,bg="#73467e",cursor="hand2",command=lambda: btn_click(0)).grid(row=5,column=0,columnspan=2)
point = Button(btns_frame, text=".", fg="black",width=10,height=3,bd=0,bg="#413569",cursor="hand2",command=lambda: btn_click(".")).grid(row=5,column=2)
equal = Button(btns_frame, text="=", fg="black",width=10,height=3,bd=0,bg="#413569",cursor="hand2",command=btn_equal).grid(row=5,column=3)

window.mainloop()