from tkinter import*
from PIL import Image, ImageTk
import tkinter
import qrcode
import image
from tkinter import messagebox



# ---------------- styles for the gui window--------------
window = tkinter.Tk()
window.geometry("600x200")
#window.resizable(0,0) 
window.configure(background="#20B2AA")
window.title("QR code Generator")
window.grid_columnconfigure((0,1),weight = 1)




#--------------- functions ------------------------------
def clicked():
    qr = qrcode.QRCode( version=15, box_size=50, border=5)
    res = url_txt.get()
    qr.add_data(res)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color = "white")
    resizeimage = img.resize((400,400))
    resizeimage.save(r"C:\Users\TJ\Downloads\qr_code.jpg")
    saveplace = Label(window, text="QR code image saved to Downloads forder: ",bg="#20B2AA",fg="#fff")
    saveplace.place(x=150, y=175)


# -------Positioned using place layout manager-----------
### enter URL label--------------
titletxt = Label(window, text="QR Code Generator ",bg="#20B2AA",fg="#fff", font=("Arial, 12"))
titletxt.place(x=240, y=50)

### enter URL label--------------
data = Label(window, text="Enter your URL: ",bg="#20B2AA",fg="#fff")
data.place(x=50, y=100)

### enter URL txt-----------------
url_txt = Entry(window, font=("Arial",10),width=50,bd=0, fg="#808080")
url_txt.place(x=150, y=100)

### create qr btn---------------
enter_btn = tkinter.Button(window, text=" Generate QR Code ", bg="#008080", fg="white", command=clicked) 
enter_btn.place(x=250, y=125)




window.mainloop()

