import random
import time
import datetime
from tkinter import*
from tkinter import ttk
import tkinter.messagebox

def main():
    window = Tk()
    app = windows1(window)
    window.mainloop()

class windows1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry('1250x700')
        self.frame = Frame(self.master)
        self.frame.pack()


        self.Username = StringVar()
        self.Password = StringVar()


        self.LabelTitle = Label(self.frame, text="  Pharmacy Management System  ", font=("arial", 20, "bold"), bd=0,relief= "sunken")
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=0)

        self.Loginframe1 = Frame(self.frame, width=1000, height=300, bd=0, relief="groove")
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(self.frame, width=1000, height=200, bd=0, relief="groove")
        self.Loginframe2.grid(row=2, column=0,pady=0)

        self.Loginframe3 = Frame(self.frame, width=1000, height=180, bd=0, relief="groove")
        self.Loginframe3.grid(row=6, column=0, pady=0)




        self.button_reg = Button(self.Loginframe3, text = "Patient Registration window", font=("arial",12),state=DISABLED, borderwidth= 0, fg = "#6D6968", command=self.Registration_window)
        self.button_reg.grid(row=0, column=0,padx=10, pady=10)

        self.button_Hosp = Button(self.Loginframe3, text = "Hospital management window", font=("arial",12),state=DISABLED,borderwidth= 0, fg = "#6D6968", command=self.Hospital_window)
        self.button_Hosp.grid(row=0, column=1,padx=0, pady=10)

        self.button_Dr_Appt = Button(self.Loginframe3, text = "    Dr. Appoinment window   ", font=("arial",12),state=DISABLED,borderwidth= 0, fg = "#6D6968", command=self.Dr_Apoint_window)
        self.button_Dr_Appt.grid(row=1, column=0,padx=0, pady=10)

        self.button_med_stack = Button(self.Loginframe3, text = "    Medicine Stock Window     ", font=("arial",12),state=DISABLED,borderwidth= 0, fg = "#6D6968", command=self.Medicine_stock)
        self.button_med_stack.grid(row=1, column=1,padx=0, pady=10)


        #  user name and password window
        self.LabelUsername = Label(self.Loginframe1, text = "User Name :", font = ("arial", 10), bd=3)
        self.LabelUsername.grid(row=0, column=0, padx=40, pady=15)

        self.txtUsername = Entry(self.Loginframe1, font = ("arial", 10), bd=0, textvariable= self.Username)
        self.txtUsername.grid(row=0, column=1)


        self.LoginPassword = Label(self.Loginframe1, text = "Password :", font = ("arial", 10), bd=3)
        self.LoginPassword.grid(row=1, column=0)

        self.txtPassword = Entry(self.Loginframe1, show='*',font = ("arial", 10),  bd=0, textvariable= self.Password)
        self.txtPassword.grid(row=1, column=1)


        self.buttonLogin = Button(self.Loginframe2, text = " Login ", width=20, font = ("arial", 10),command=self.login_system)
        self.buttonLogin.grid(row=0, column=0, padx=10,pady=10)

        self.buttonLogin = Button(self.Loginframe2, text = " Reset ", width=20, font = ("arial", 10),)
        self.buttonLogin.grid(row=0, column=1, padx=10,pady=10)

        self.buttonLogin = Button(self.Loginframe2, text = " Exit ", width=20, font = ("arial", 10),)
        self.buttonLogin.grid(row=0, column=2, padx=10,pady=10)

    def login_system(self):
        user = self.Username.get()
        pasw = self.Password.get()

        if (user == str("admin") and (pasw ==str("admin"))):
            self.button_reg.config(state=NORMAL)
            self.button_Hosp.config(state=NORMAL)
            self.button_Dr_Appt.config(state=NORMAL)
            self.button_med_stack.config(state=NORMAL)
        else:
            tkinter.messagebox.askretrycancel("Pharmacy management system","You have entered an invalid username or password ! Try again " )
            self.button_reg.config(state=DISABLED)
            self.button_Hosp.config(state=DISABLED)
            self.button_Dr_Appt.config(state=DISABLED)
            self.button_med_stack.config(state=DISABLED)

            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()




        # define all windows
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows2(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows3(self.newWindow)

    def Dr_Apoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows4(self.newWindow)

    def Medicine_stock(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows5(self.newWindow)



class windows2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Management System")
        self.master
        self.master.geometry('1250x700')
        self.frame = Frame(self.master)
        self.frame.pack()



class windows3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry('1250x700')
        self.frame = Frame(self.master)
        self.frame.pack()


class windows4:
    def __init__(self, master):
        self.master = master
        self.master.title("Doctor Management System")
        self.master.geometry('1250x700')
        self.frame = Frame(self.master)
        self.frame.pack()

class windows5:
    def __init__(self, master):
        self.master = master
        self.master.title("Medicine System")
        self.master.geometry('1250x700')
        self.frame = Frame(self.master)
        self.frame.pack()



if __name__ == "__main__":
    main()