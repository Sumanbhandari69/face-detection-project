from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from cryptography.fernet import Fernet

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration")
        self.root.geometry("1530x790+0+0")

        #variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityqn = StringVar()
        self.var_answer = StringVar()
        self.var_password = StringVar()
        self.var_confirmpw = StringVar()
        self.var_terms = IntVar()

        ## Bg image ##

        self.bg=ImageTk.PhotoImage(file="./image_file/background.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

    
        ## Register Frame

        frame1=Frame(self.root,bg="white")
        frame1.place(x=400,y=120,width=700,height=600)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=230,y=30)



        ## Row 1---------

        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=100)
        self.txt_fname=Entry(frame1,textvariable=self.var_fname,font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=100)
        self.txt_lname=Entry(frame1,textvariable=self.var_lname,font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        ## Row 2---------

        contact=Label(frame1,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=170)
        self.txt_contact=Entry(frame1,textvariable=self.var_contact,font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
        
        
        email=Label(frame1,text="E Mail",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15,"bold"),textvariable=self.var_email,bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

        ## Row 3----------

        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=240)

        self.cmb_question=ttk.Combobox(frame1,font=("times new roman",13,"bold"),textvariable=self.var_securityqn,state='readonly',justify=CENTER)
        self.cmb_question['values']=("Select","Your pet name","Your birth place","Favourite Food")
        self.cmb_question.place(x=50,y=270,width=250)
        self.cmb_question.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15,"bold"),textvariable=self.var_answer,bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        ### Row 4--------

        Password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15,"bold"),textvariable=self.var_password,bg="lightgray")
        self.txt_password.place(x=50,y=345,width=250)

        Confirm_Password=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15,"bold"),textvariable=self.var_confirmpw,bg="lightgray")
        self.txt_cpassword.place(x=370,y=345,width=250)

        ## Check button----
        chk=Checkbutton(frame1,text="I agree the terms and conditions.",variable=self.var_terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)

        # Register button----------

        btn_register=Button(frame1,text="Register now",font=("times new roman",15,"bold"),command=self.register_data,bg="lightblue",fg="black",bd=0,cursor="hand2").place(x=275,y=420)

        ## already have account?? label------

        lbl=Label(frame1,text="Already have an account?",font=("times new roman",15,"bold"),bg="white",fg="blue").place(x=200,y=490)

        ## Sign in button-------

        btn_sign_in=Button(self.root,text="Sign In",font=("times new roman",15,"bold",),command=self.login_window,bg="white",fg="red",bd=0,cursor="hand2").place(x=820,y=608)



    def login_window(self):
        self.root.destroy()
        import Login

    import hashlib

    from cryptography.fernet import Fernet

    def register_data(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" or self.var_securityqn.get() == "Select" or self.var_answer.get() == "" or \
                self.var_password.get() == "" or self.var_confirmpw.get() == "":
            messagebox.showerror("Error", "All Fields Are Required.", parent=self.root)
        elif self.var_password.get() != self.var_confirmpw.get():
            messagebox.showerror("Error", "Password and Confirm Password should be same.", parent=self.root)
        elif self.var_terms.get() == 0:
            messagebox.showerror("Error", "All Fields Are Required.", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="9818913355",
                                           database="face_recognition")
            cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email = %s"
            value = (self.var_email.get(),)
            cursor.execute(query, value)
            row = cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already exists. Please enter another email.")
            else:
                # Generate a new Fernet key
                key = Fernet.generate_key()

                # Create a Fernet cipher using the key
                cipher = Fernet(key)

                # Encrypt the password
                encrypted_password = cipher.encrypt(self.var_password.get().encode())

                # Insert the encrypted password into the database
                query = "INSERT INTO register (fname, lname, contact, email, securityQ, answer, password, encryption_key) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                values = (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityqn.get(),
                    self.var_answer.get(),
                    encrypted_password,
                    key
                )
                cursor.execute(query, values)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Successfully Registered")


root=Tk()
obj=Register(root)
root.mainloop()

