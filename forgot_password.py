from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk


class Fpassword:
    def __init__(self,root):
        self.root=root
        self.root.title("Forgot password")
        self.root.geometry("800x600+350+100")
        self.root.resizable(False,False)

        ## Bg image--------

        self.bg=ImageTk.PhotoImage(file="./image_file/background.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        ## Fpassword Frame---------

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=200, y=100, width=400, height=400)

        title = Label(frame1, text="Forgot Password", font=("times new roman", 20, "bold"), bg="white", fg="red").place(x=90,y=30)

        email_address = Label(frame1, text="Email Address", font=("times new roman", 15, "bold"), bg="white",fg="black").place(x=50, y=100)
        self.txt_email_address = Entry(frame1, font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_email_address.place(x=50, y=130, width=290)

        NPassword = Label(frame1, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=170)
        self.txt_npassword = Entry(frame1, font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_npassword.place(x=50, y=200, width=290)

        CPassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=240)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_cpassword.place(x=50, y=270, width=290)

        ## Reset Password button----------

        btn_Reset = Button(frame1, text="Reset Password", font=("times new roman", 15, "bold"), command=self.fpassword_data,bg="lightblue", fg="black", bd=0, cursor="hand2").place(x=120, y=320)

        ## Login button----------

        btn_login = Button(frame1, text="Log in", font=("times new roman", 13), command=self.login_window,bg="white", fg="blue", bd=0, cursor="hand2").place(x=270, y=325)

    def login_window(self):
        self.root.destroy()
        import Login

    def fpassword_data(self):
        if self.txt_email_address.get() == "" or self.txt_npassword.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.txt_npassword.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "New Password and Confirm Password should be same.", parent=self.root)
        else:
            messagebox.showerror("Success", "Reset Successfull", parent=self.root)


root=Tk()
obj=Fpassword(root)
root.mainloop()

