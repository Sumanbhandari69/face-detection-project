from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from main import Face_Recognition_System
from cryptography.fernet import Fernet
# from Register import Register

class Login:
    def __init__(self,root1):
        self.root1=root1
        self.root1.title("Login")
        self.root1.geometry("1530x790+0+0")

        self.var_Email = StringVar()
        self.var_Password = StringVar()

        ## Bg image--------

        self.bg=ImageTk.PhotoImage(file="./image_file/background.jpg")
        bg=Label(self.root1,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        ## Login Frame---------

        frame1=Frame(self.root1,bg="white")
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

        forget_password=Button(self.root1,text="Forget password?",font=("times new roman",14),command=self.fpassword_window,bg="white",fg="black",bd=0,cursor="hand2").place(x=750,y=390)

        ## Login button----------

        btn_login=Button(frame1,text="Log in",font=("times new roman",15,"bold"),command=self.login_data,bg="lightblue",fg="black",bd=0,cursor="hand2").place(x=50,y=240)

        ## Dont have an account label--------

        acnt=Label(text="Don't have an account?",font=("times new roman",15),bg="white",fg="blue").place(x=650,y=540)

        ## Register button----------

        btn_register=Button(self.root1,text="Register",font=("times new roman",15,"bold"),command=self.register_window,bg="white",fg="red",bd=0,cursor="hand2").place(x=670,y=570,width=150)


    def register_window(self):
        # self.new_window = Toplevel(self.root)
        # self.app = Register(self.new_window)
        self.root1.destroy()
        import Register

    def reset_password(self):
        if self.cmb_question.get() == "Select":
            messagebox.showerror("Error", "Select the security question", parent=self.root2)
        elif self.txt_answer.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
        elif self.txt_new_pass.get() == "":
            messagebox.showerror("Error", "Please enter new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="9818913355",
                                           database="face_recognition")
            cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email = %s AND securityQ = %s AND answer = %s"
            value = (self.var_Email.get(), self.cmb_question.get(), self.txt_answer.get())
            cursor.execute(query, value)
            row = cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid input", parent=self.root2)
            else:
                # Generate a new Fernet key
                key = Fernet.generate_key()

                # Create a Fernet cipher using the key
                cipher = Fernet(key)

                # Encrypt the new password
                encrypted_password = cipher.encrypt(self.txt_new_pass.get().encode())

                query = "UPDATE register SET password = %s, encryption_key = %s WHERE email = %s"
                value = (encrypted_password, key, self.var_Email.get())
                cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset. Please login with the new password")
                self.root2.destroy()

    def fpassword_window(self):
        if self.var_Email.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="9818913355",
                                           database="face_recognition")
            cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_Email.get(),)
            cursor.execute(query, value)
            row=cursor.fetchone()
           # print(row)
            if row==None:
                messagebox.showerror("My Error","Please enter valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("forget password")
                self.root2.geometry("400x500+550+150")
              #  x = 550, y = 150, width = 400, height = 500

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="white",
                                 fg="black").place(x=80, y=80)

                self.cmb_question = ttk.Combobox(self.root2, font=("times new roman", 13, "bold"),
                                                  state='readonly', justify=CENTER)
                self.cmb_question['values'] = ("Select", "Your pet name", "Your birth place", "Favourite Food")
                self.cmb_question.place(x=80, y=110, width=250)
                self.cmb_question.current(0)

                answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white",
                               fg="black").place(x=80, y=150)

                self.txt_answer = Entry(self.root2, font=("times new roman", 15, "bold"),
                                        bg="lightgray")
                self.txt_answer.place(x=80, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",
                               fg="black").place(x=80, y=220)

                self.txt_new_pass = Entry(self.root2, font=("times new roman", 15, "bold"),
                                        bg="lightgray")
                self.txt_new_pass.place(x=80, y=250, width=250)

                btn=Button(self.root2,text="Reset",font=("times new roman", 15, "bold"),command=self.reset_password,fg="white",bg="green")
                btn.place(x=160,y=310)

    def login_data(self):
        if self.var_Email.get() == "" or self.var_Password.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="9818913355",
                                               database="face_recognition")
            cursor = conn.cursor()
            cursor.execute("SELECT password, encryption_key FROM register WHERE email = %s",
                               (self.var_Email.get(),))
            row = cursor.fetchone()
            # conn.close()

            if row is None:
                messagebox.showerror("Error", "Invalid Email and Password")
            else:
                masked_password = row[0]
                encryption_key = row[1]

                    # Decrypt the masked password using the encryption key
                cipher = Fernet(encryption_key)
                decrypted_password = cipher.decrypt(masked_password).decode()

                if decrypted_password == self.var_Password.get():
                    self.root1.destroy()
                    self.new_window = Tk()
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    messagebox.showerror("Error", "Invalid Email and Password")

        conn.commit()
        conn.close()



 











root1=Tk()
obj=Login(root1)
root1.mainloop()

