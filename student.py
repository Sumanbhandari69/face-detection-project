from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Attendance System")

        #variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()


        # Background image
        img = Image.open("./image_file/background_image.jpeg")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)

        title_lbl = Label(bg_img, text="Student Management System", font=("times new roman", 35, "bold"),
                          bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        #main frame
        main_frame = Frame(bg_img,bd=2,bg= "white")
        main_frame.place(x=20,y=100,width=1475,height=640)

        #Left Label Frame

        left_frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE,text="Student Details",font=("times new roman",15, "bold"))
        left_frame.place(x=10,y=10,width=720, height=600)

        img_left= Image.open("./image_file/Student_image2.jpeg")
        img_left = img_left.resize((720, 125), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=720, height=125)

        #Current Courses

        course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Courses",
                                font=("times new roman", 15, "bold"))
        course_frame.place(x=10, y=125, width=700, height=140)


        #Department Label

        department_label = Label(course_frame,text="Department:",font=("times new roman",15, "bold"))
        department_label.grid(row=0,column=0, padx=15,pady= 12)

        department_combo = ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman",15, "bold"),width=17,state="readonly")
        department_combo["values"] = ("Select Department", "Engineering", "IT")
        department_combo.current(0)
        department_combo.grid(row=0, column=1, padx=10,pady=12)

        # Course Label

        course_label = Label(course_frame, text="Course:", font=("times new roman", 15, "bold"))
        course_label.grid(row=0, column=2,padx=15,pady=12)

        course_combo = ttk.Combobox(course_frame,textvariable=self.var_course, font=("times new roman", 15, "bold"), width=17, state="readonly")
        course_combo["values"] = ("Select course", "Civil", "CSIT", "BCA", "Mechanical")
        course_combo.current(0)
        course_combo.grid(row=0, column=3,padx=10,pady=12)

        # Year Label

        year_label = Label(course_frame, text="Year:", font=("times new roman", 15, "bold"))
        year_label.grid(row=1, column=0,padx=15,pady=15)

        year_combo = ttk.Combobox(course_frame,textvariable=self.var_year, font=("times new roman", 15, "bold"), width=17, state="readonly")
        year_combo["values"] = ("Select Year", "2018", "2019", "2020", "2021","2022","2023")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10,pady=15)

        # Semester Label

        semester_label = Label(course_frame, text="Semester:", font=("times new roman", 15, "bold"))
        semester_label.grid(row=1, column=2,padx=15,pady=15)

        semester_combo = ttk.Combobox(course_frame,textvariable=self.var_semester, font=("times new roman", 15, "bold"), width=17, state="readonly")
        semester_combo["values"] = ("Select Semester", "First", "Second", "Third", "Fourth","Fifth","Sixth","Seventh","Eighth")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3,padx=10,pady=15)


        #Class Student Information
        student_info_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("times new roman", 15, "bold"))
        student_info_frame.place(x=10, y=265, width=700, height=305)

        #Student_ID
        student_ID_label = Label(student_info_frame, text="StudentID:", font=("times new roman", 15, "bold"))
        student_ID_label.grid(row=0, column=0,pady=10)

        student_ID_entry = ttk.Entry(student_info_frame,textvariable=self.var_std_id, width=20,font=("times new roman", 15, "bold"))
        student_ID_entry.grid(row=0, column=1,pady=10)

        # Student Name
        student_name_label = Label(student_info_frame, text="StudentName:", font=("times new roman", 15, "bold"))
        student_name_label.grid(row=0, column=2, pady=10)

        student_name_entry = ttk.Entry(student_info_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 15, "bold"))
        student_name_entry.grid(row=0, column=3, pady=10)

        # Student roll no
        student_roll_label = Label(student_info_frame, text="Roll no:", font=("times new roman", 15, "bold"))
        student_roll_label.grid(row=1, column=0, pady=10)

        student_roll_entry = ttk.Entry(student_info_frame,textvariable=self.var_roll, width=20, font=("times new roman", 15, "bold"))
        student_roll_entry.grid(row=1, column=1, pady=10)

        # Student gender
        student_gender_label = Label(student_info_frame, text="Gender:", font=("times new roman", 15, "bold"))
        student_gender_label.grid(row=1, column=2, pady=10)

        gender_combo = ttk.Combobox(student_info_frame, textvariable=self.var_gender,
                                      font=("times new roman", 15, "bold"), width=17, state="readonly")
        gender_combo["values"] = ("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=10, pady=15)


        # Student Email
        student_Email_label = Label(student_info_frame, text="Email:", font=("times new roman", 15, "bold"))
        student_Email_label.grid(row=2, column=2, pady=10)

        student_Email_entry = ttk.Entry(student_info_frame,textvariable=self.var_email, width=20, font=("times new roman", 15, "bold"))
        student_Email_entry.grid(row=2, column=3, pady=10)

        # Student Phone
        student_phone_label = Label(student_info_frame, text="Phone:", font=("times new roman", 15, "bold"))
        student_phone_label.grid(row=2, column=0, pady=10)

        student_phone_entry = ttk.Entry(student_info_frame,textvariable=self.var_phone, width=20, font=("times new roman", 15, "bold"))
        student_phone_entry.grid(row=2, column=1, pady=10)


        #Radio Buttons
        self.var_radio1 = StringVar()
        radiobutton1 = ttk.Radiobutton(student_info_frame,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobutton1.grid(row=5,column=0,padx=10)


        radiobutton2 = ttk.Radiobutton(student_info_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobutton2.grid(row=5, column=1,padx=10)

        #Operation Frame
        operation_frame = LabelFrame(student_info_frame, bd=3, bg="white", relief=RIDGE,)
        operation_frame.place(x=0, y=180, width=695, height=100)

        #Save button
        save_btn = Button(operation_frame,text="Save",command=self.add_data,width=18, font=("times new roman", 15, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0, column=0)

        # Update button"
        update_btn = Button(operation_frame,command=self.update_data, text="Update", width=18, font=("times new roman", 15, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0, column=1)

        # Delete button
        delete_btn = Button(operation_frame,command=self.delete_data, text="Delete", width=18, font=("times new roman", 15, "bold"), bg="blue",fg="white")
        delete_btn.grid(row=0, column=2)

        # Reset button
        reset_btn = Button(operation_frame,command=self.reset_data, text="Reset", width=18, font=("times new roman", 15, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=1, column=0)

        # Take photo sample button
        take_photo_btn = Button(operation_frame,command=self.generate_dataset, text="Take Photo", width=18, font=("times new roman", 15, "bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1, column=1)

        # Update Photo button
        update_photo_btn = Button(operation_frame, text="Update Photo", width=18, font=("times new roman", 15, "bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1, column=2)





        # Right Label Frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 15, "bold"))
        right_frame.place(x=750, y=10, width=700, height=600)

        # search system
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search system",
                                 font=("times new roman", 15, "bold"))
        search_frame.place(x=10, y=5, width=680, height=80)

        #Search label
        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"))
        search_label.grid(row=0, column=0,padx=10)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 15, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "StudentID", "Phone")
        search_combo.current(0)
        search_combo.grid(row=0, column=1)

        #Search Entry
        student_address_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 15, "bold"))
        student_address_entry.grid(row=0, column=2 )

        #Search Button
        search_btn = Button(search_frame, text="Search", width=7, font=("times new roman", 15, "bold"),bg="blue",fg="white")
        search_btn.grid(row=0, column=3)

        # ShowAll Button
        showall_btn = Button(search_frame, text="Show all", width=8, font=("times new roman", 15, "bold"),bg="blue",fg="white")
        showall_btn.grid(row=0, column=4)

        #Table frame
        table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=90, width=680, height=480)

        #Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("Dep","Course","Year","Semester","ID","Name","Roll no"
                                                              ,"Gender","Email","Phone","Photo"),
                                          xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("ID", text="ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Roll no", text="Roll no")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Photo", text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Roll no", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Photo", width=100)



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #Function Declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_phone.get()=="" or self.var_course.get()=="Select course" or self.var_email.get()=="" or self.var_gender.get()=="Select Gender" or self.var_roll.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_semester.get()=="Select Semester" or self.var_year.get()=="Select Year":
            messagebox.showerror("Error","All fields are mandatory!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="9818913355",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),
                                                                                                  self.var_course.get(),
                                                                                                  self.var_year.get(),
                                                                                                  self.var_semester.get(),
                                                                                                  self.var_std_id.get(),
                                                                                                  self.var_std_name.get(),
                                                                                                  self.var_roll.get(),
                                                                                                  self.var_gender.get(),
                                                                                                  self.var_email.get(),
                                                                                                  self.var_phone.get(),
                                                                                                  self.var_radio1.get()

                                                                                                  ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data stored successfully!",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #------fetch data------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="9818913355",
                                       database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)

            conn.commit()
        conn.close()

    #Get Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_radio1.set(data[10])


    #Update
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_phone.get() == "" or self.var_course.get() == "Select course" or self.var_email.get() == "" or self.var_gender.get() == "Select Gender" or self.var_roll.get() == "" or self.var_std_name.get() == "" or self.var_std_id.get() == "" or self.var_semester.get() == "Select Semester" or self.var_year.get() == "Select Year":
            messagebox.showerror("Error", "All fields are mandatory!", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this data",parent = self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="9818913355",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep = %s, Course = %s,Year = %s,Semester = %s,Name= %s,Roll = %s,Gender = %s,Email = %s,Phone = %s,PhotoSample = %s where Student_ID = %s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

    #Delete Button
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must required",parent= self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete page","Do you want to delete this Student details",parent= self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="9818913355",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_ID =%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


    #Reset function
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_radio1.set("")


    #Generate Dataset/Photo Sample
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_phone.get() == "" or self.var_course.get() == "Select course" or self.var_email.get() == "" or self.var_gender.get() == "Select Gender" or self.var_roll.get() == "" or self.var_std_name.get() == "" or self.var_std_id.get() == "" or self.var_semester.get() == "Select Semester" or self.var_year.get() == "Select Year":
            messagebox.showerror("Error", "All fields are mandatory!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="9818913355",
                                                   database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id+=1

                my_cursor.execute(
                    "update student set Dep = %s, Course = %s,Year = %s,Semester = %s,Name= %s,Roll = %s,Gender = %s,Email = %s,Phone = %s,PhotoSample = %s where Student_ID = %s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1
                    ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #Load predefined data on face frontals from open cv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.1,5)
                    #scaling factor = 1.3
                    #minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face =cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croppped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==200:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating datasets completed!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)



















if __name__=="__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()