from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from main import Face_Recognition_System
# from Register import Register

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        self.var_Email = StringVar()
        self.var_Password = StringVar()

        ## Bg image--------

        self.bg=ImageTk.PhotoImage(file="./image_file/background.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        ## Login Frame---------

        frame1=Frame(self.root,bg="white")
        frame1.place(x=550,y=150,width=400,height=500)

        title=Label(frame1,text="LOGIN HERE",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=110,y=30)

        ## Row 1---------

        email_address=Label(frame1,text="Email Address",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=100)
        self.txt_email_address=Entry(frame1,textvariable=self.var_Email,font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_email_address.place(x=50,y=130,width=290)

        Password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=170)
        self.txt_password=Entry(frame1,textvariable=self.var_Password,show="*",font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_password.place(x=50,y=200,width=290)

        ## forget password------

        forget_password=Button(self.root,text="Forget password?",font=("times new roman",14),command=self.fpassword_window,bg="white",fg="black",bd=0,cursor="hand2").place(x=750,y=390)

        ## Login button----------

        btn_login=Button(frame1,text="Log in",font=("times new roman",15,"bold"),command=self.login_data,bg="lightblue",fg="black",bd=0,cursor="hand2").place(x=50,y=240)

        ## Dont have an account label--------

        acnt=Label(text="Don't have an account?",font=("times new roman",15),bg="white",fg="blue").place(x=650,y=540)

        ## Register button----------

        btn_register=Button(self.root,text="Register",font=("times new roman",15,"bold"),command=self.register_window,bg="white",fg="red",bd=0,cursor="hand2").place(x=670,y=570,width=150)


    def register_window(self):
        # self.new_window = Toplevel(self.root)
        # self.app = Register(self.new_window)
        self.root.destroy()
        import Register

    def fpassword_window(self):
        self.root.destroy()
        import forgot_password

    def login_data(self):
        if self.var_Email.get()=="" or self.var_Password.get()=="":
             messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="9818913355",
                                           database="face_recognition")
            cursor = conn.cursor()
            cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.var_Email.get(),
                                                                                    self.var_Password.get()
                                                                                     ))
            row = cursor.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error","Invalid Email and Password")
            else:
                self.new_window = Toplevel(self.root)
                self.app = Face_Recognition_System(self.new_window)

        conn.commit()
        conn.close()



 











root=Tk()
obj=Login(root)
root.mainloop()

