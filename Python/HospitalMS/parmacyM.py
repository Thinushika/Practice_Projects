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

        self.button_reset = Button(self.Loginframe2, text = " Reset ", width=20,command=self.reset_btn, font = ("arial", 10),)
        self.button_reset.grid(row=0, column=1, padx=10,pady=10)

        self.button_Exit = Button(self.Loginframe2, text = " Exit ", width=20,command=self.Exit_btn, font = ("arial", 10),)
        self.button_Exit.grid(row=0, column=2, padx=10,pady=10)

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

    def reset_btn(self):
        self.button_reg.config(state=DISABLED)
        self.button_Hosp.config(state=DISABLED)
        self.button_Dr_Appt.config(state=DISABLED)
        self.button_med_stack.config(state=DISABLED)

        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def Exit_btn(self):
        self.Exit_btn = tkinter.messagebox.askyesno("Pharmacy Management System","Do you want to exit")
        if self.Exit_btn >0:
            self.master.destroy()
            return


        # define all windows
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows3(self.newWindow)

    def Dr_Apoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows4(self.newWindow)

    def Medicine_stock(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows5(self.newWindow)



class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry('1250x700')
        self.root.configure(background = "black")

        # take live time
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        Mobile_num = StringVar()
        Pincode = StringVar()
        Address = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Gender = StringVar()

        # for combo box
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = StringVar()

        Membership = StringVar()
        Membership.set("0")


        #----------- functions --------------
        def exitBtnnn():
            exitBtnnn = tkinter.messagebox.askyesno("Member registrain form", "Do you want to exit?")
            if exitBtnnn>0:
                root.destroy()
            else:
                self.newWindow = Toplevel(self.master)
                self.app = Registration(self.newWindow)
                return

        def resetbtnnn():
            Ref .set("")
            Mobile_num .set("")
            Pincode .set("")
            Address .set("")
            Firstname.set("")
            Lastname .set("")
            Gender .set("")
            var1.set("")
            var2 .set("")
            var3 .set("")
            var4 .set("")
            var5 .set("")
            Membership .set("")
            Membership.set("0")
            Member_gendercmb.current(0)
            Member_id_proofcmb.current(0)
            Member_typecmb.current(0)
            Member_payment_withcmb.current(0)
            member_membershiptxt(state = DISABLED)


        def reesetbtn():
            resetbutt = tkinter.messagebox.askokcancel("Member registrain form", "Do you want to add as new record?")
            if reesetbtn>0:
                resetbtnnn()
            elif reesetbtn<=0:
                resetbtnnn()
                detail_labeltxt.delete("1.0",END)
                return

        def Reference_number():
            randnum = random.randint(10000,9999999)
            randnumber = str(randnum)
            Ref.set(randnumber)

        def membership_fee():
            if(var5.get()==1):
                member_membershiptxt.configure(state=NORMAL)
                item = float(15000)
                Membership.set(str(item)+"Rs")
            elif(var5.get()==0):
                member_membershiptxt.configure(state=DISABLED)
                Membership.set("0")


        def Receipt():
            Reference_number()
            detail_labeltxt.insert(END, "\t" + Date_of_Registration.get()+"         \t"+Ref.get()+"\t\t"+Firstname.get()+'      \t'+Lastname.get()+"\t\t" + Mobile_num.get()+"      \t\t" + Address.get()+ "\t" + Pincode.get()+"       \t"+Member_gendercmb.get()+"\t\t" + Membership.get()+"\n")



        title = Label(self.root, text="  Member Registration System  ", font=("monotype corsiva", 20, "bold"), bd=0,relief= GROOVE,bg = "#E6005C", fg="#000000")
        title.pack(side=TOP, fill= X )


        Manage_form = Frame(self.root,bd = 4, relief=RIDGE, bg="#001a66")
        Manage_form.place(x=20, y=100, width=450, height=550)

        


        # --------- label, test, combo box ----------------
        cusTitle = Label(Manage_form, text = "Customer Details ", font = ("arial", 12), bg="#001a66", fg="#fff")
        cusTitle.grid(row=0, columnspan=2, pady=5)

        Member_detail = Label(Manage_form, text = "Date ", font = ("arial", 12), bg="#001a66", fg="#fff")
        Member_detail.grid(row=1, column=0, pady=5,padx=10, sticky="w")

        membe_datetxt = Entry(Manage_form, font= ("arial",12), textvariable=Date_of_Registration)
        membe_datetxt.grid(row=1,column=1, pady=5,padx=10, sticky="w")


        member_reflbl = Label(Manage_form,text="Reference ID", font=("arial",12),bg="#001a66",fg="#fff")
        member_reflbl.grid(row=2, column=0, pady=5, padx=10,sticky="w")

        membe_reftxt = Entry(Manage_form, font= ("arial",12), state=DISABLED, text=Ref)
        membe_reftxt.grid(row=2,column=1, pady=5,padx=10, sticky="w")

        #fname
        Member_fnamelbl = Label(Manage_form, text = "First name : ", font = ("arial", 12), bg="#001a66", fg="#fff")
        Member_fnamelbl.grid(row=3, column=0, pady=5,padx=10, sticky="w")

        membe_fnametxt = Entry(Manage_form, font= ("arial",12), textvariable=Firstname)
        membe_fnametxt.grid(row=3,column=1, pady=5,padx=10, sticky="w")

        #lname
        Member_lnamelbl = Label(Manage_form, text = "Last name : ", font = ("arial", 12), bg="#001a66", fg="#fff")
        Member_lnamelbl.grid(row=4, column=0, pady=5,padx=10, sticky="w")

        membe_lnametxt = Entry(Manage_form, font= ("arial",12), textvariable=Lastname)
        membe_lnametxt.grid(row=4,column=1, pady=5,padx=10, sticky="w")

        #mobilenum
        Member_mobilenolbl = Label(Manage_form, text = "Mobile Number : ", font = ("arial", 12), bg="#001a66", fg="#fff")
        Member_mobilenolbl.grid(row=5, column=0, pady=5,padx=10, sticky="w")

        Member_mobilenotxt = Entry(Manage_form, font= ("arial",12), textvariable=Mobile_num)
        Member_mobilenotxt.grid(row=5,column=1, pady=5,padx=10, sticky="w")

        #Address
        Member_Addresslbl = Label(Manage_form, text = "Address : ", font = ("arial", 12), bg="#001a66", fg="#fff")
        Member_Addresslbl.grid(row=6, column=0, pady=5,padx=10, sticky="w")

        Member_Addresstxt = Entry(Manage_form, font= ("arial",12), textvariable=Address)
        Member_Addresstxt.grid(row=6,column=1, pady=5,padx=10, sticky="w")

        #pincode
        Member_pincodelbl = Label(Manage_form, text = "Pin code : ", font = ("arial", 12), bg="#001a66", fg="#fff")
        Member_pincodelbl.grid(row=7, column=0, pady=5,padx=10, sticky="w")

        Member_pincodetxt = Entry(Manage_form, font= ("arial",12), textvariable=Pincode)
        Member_pincodetxt.grid(row=7,column=1, pady=5,padx=10, sticky="w")

        #gender
        Member_genderlbl = Label(Manage_form, text = "Gender : ", font = ("arial", 12), bg="#001a66", fg="#fff")
        Member_genderlbl.grid(row=8, column=0, pady=5,padx=10, sticky="w")

        Member_gendercmb = ttk.Combobox(Manage_form, text = var4,state= "readonly", font =("arial", 12), width=18)
        Member_gendercmb["values"] = (" ","Male","Female","Other")
        Member_gendercmb.current(0)
        Member_gendercmb.grid(row=8, column=1, pady=5,padx=10, sticky="w")

        # member id proof label
        Member_id_prooflbl = Label(Manage_form, text = "ID proof : ", font = ("arial", 12), bg="#001a66", fg="#fff")
        Member_id_prooflbl.grid(row=9, column=0, pady=5,padx=10, sticky="w")

        Member_id_proofcmb = ttk.Combobox(Manage_form, text = var3,state= "ID Proof", font =("arial", 12), width=18)
        Member_id_proofcmb["values"] = (" ","NIC","Passport","Driving License", "University ID", "Student ID")
        Member_id_proofcmb.current(0)
        Member_id_proofcmb.grid(row=9, column=1, pady=5,padx=10, sticky="w")

        # member type label
        Member_typelbl = Label(Manage_form, text = "Member Type : ", font = ("arial", 12), bg="#001a66", fg="#fff")
        Member_typelbl.grid(row=10, column=0, pady=5,padx=10, sticky="w")

        Member_typecmb = ttk.Combobox(Manage_form, text = var2,state= "Member type", font =("arial", 12), width=18)
        Member_typecmb["values"] = (" ","Green Card","Pay Imidiatly","Pay when leaving")
        Member_typecmb.current(0)
        Member_typecmb.grid(row=10, column=1, pady=5,padx=10, sticky="w")

        # member payment with label
        Member_payment_withlbl = Label(Manage_form, text = "Payment method : ", font = ("arial", 12), bg="#001a66", fg="#fff")
        Member_payment_withlbl.grid(row=11, column=0, pady=5,padx=10, sticky="w")

        Member_payment_withcmb = ttk.Combobox(Manage_form, text = var1,state= "Member type", font =("arial", 12), width=18)
        Member_payment_withcmb["values"] = (" ","Debit card - Visa", "Credit card - Master", "Cash","cheque", "PayPal", "Google Pay")
        Member_payment_withcmb.current(0)
        Member_payment_withcmb.grid(row=11, column=1, pady=5,padx=10, sticky="w")

        member_membership = Checkbutton(Manage_form, text="Membership Fees",variable=var5,onvalue=1, offvalue=0,font = ("arial", 12), bg="#001a66", fg="#fff",command=membership_fee)
        member_membership.grid(row=12, column=0, sticky="w")

        member_membershiptxt = Entry(Manage_form, font =("arial", 12), state=DISABLED, justify="right", textvariable=Membership)
        member_membershiptxt.grid(row=12, column=1, sticky="w",pady=5,padx=10)


#------------- Detail frame ----------
        Detail_frame = Frame(self.root,bd = 4, relief=RIDGE, bg="#001a66")
        Detail_frame.place(x=500, y=100, width=720, height=550)

        detail_label =Label(Detail_frame,font=("arial", 10, "bold") , pady=10, padx=2,width=90, text = "Date\t Ref Id\t Firstname   Lastname    Mobile NO   Address     Pincode     Gender      Membership")
        detail_label.grid(row=0,column=0, columnspan=4, sticky="w")

        detail_labeltxt = Text(Detail_frame,width=123, height=29,font= ("arial",10))
        detail_labeltxt.grid(row=1,column=0, columnspan=4)

        ### ----------- recipt / reset / exit btn ----------------------- 

        receiptbtn = Button(Detail_frame, padx=10, bd=1, font=("arial",10), bg="#ff9966", width=15, text="Recepit", command=Receipt)
        receiptbtn.grid(row=2,column=0)

        resetbtn = Button(Detail_frame, padx=10, bd=1, font=("arial",10), bg="#ff9966", width=15, text="Reset", command=reesetbtn)
        resetbtn.grid(row=2,column=1)

        exitbtn = Button(Detail_frame, padx=10, bd=1, font=("arial",10), bg="#ff9966", width=15, text="Exit",command=exitBtnnn)
        exitbtn.grid(row=2,column=2)



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