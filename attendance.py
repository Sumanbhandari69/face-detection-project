from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Attendance System")


        #Variables

        self.var_student_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()

        # Background image
        img = Image.open("./image_file/background_image.jpeg")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)

        title_lbl = Label(bg_img, text="Attendance Management System", font=("times new roman", 35, "bold"),
                          bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=100, width=1475, height=640)

        #Left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 15, "bold"))
        left_frame.place(x=10, y=10, width=720, height=600)

        #Student_ID
        student_ID_label = Label(left_frame, text="StudentID:", font=("times new roman", 15, "bold"))
        student_ID_label.grid(row=0, column=0, pady=10)

        student_ID_entry = ttk.Entry(left_frame, width=20,textvariable=self.var_student_id,font=("times new roman", 15, "bold"))
        student_ID_entry.grid(row=0, column=1, pady=10)

        # Student Name
        student_name_label = Label(left_frame, text="StudentName:", font=("times new roman", 15, "bold"))
        student_name_label.grid(row=0, column=2, pady=20)

        student_name_entry = ttk.Entry(left_frame, width=20,textvariable=self.var_name,font=("times new roman", 15, "bold"))
        student_name_entry.grid(row=0, column=3, pady=20)

        # Student roll no
        student_roll_label = Label(left_frame, text="Roll no:", font=("times new roman", 15, "bold"))
        student_roll_label.grid(row=1, column=0, pady=20)

        student_roll_entry = ttk.Entry(left_frame, width=20,textvariable=self.var_roll,font=("times new roman", 15, "bold"))
        student_roll_entry.grid(row=1, column=1, pady=20)

        #Department
        department_label = Label(left_frame, text="Department:", font=("times new roman", 15, "bold"))
        department_label.grid(row=1, column=2, pady=20)

        department_entry = ttk.Entry(left_frame, width=20,textvariable=self.var_dep,font=("times new roman", 15, "bold"))
        department_entry.grid(row=1, column=3, pady=20)

        # Time
        time_label = Label(left_frame, text="Time:", font=("times new roman", 15, "bold"))
        time_label.grid(row=2, column=0, pady=20)

        time_entry = ttk.Entry(left_frame, width=20,textvariable=self.var_time, font=("times new roman", 15, "bold"))
        time_entry.grid(row=2, column=1, pady=20)

        # Date
        date_label = Label(left_frame, text="Date:", font=("times new roman", 15, "bold"))
        date_label.grid(row=2, column=2, pady=20)

        date_entry = ttk.Entry(left_frame, width=20,textvariable=self.var_date, font=("times new roman", 15, "bold"))
        date_entry.grid(row=2, column=3, pady=20)

        #Attendance Status
        student_status_label = Label(left_frame, text="Attendance:", font=("times new roman", 15, "bold"))
        student_status_label.grid(row=3, column=0, pady=20)

        status_combo = ttk.Combobox(left_frame,font=("times new roman", 15, "bold"), width=17,textvariable=self.var_attendance, state="readonly")
        status_combo["values"] = ("Status", "Present","Absent")
        status_combo.current(0)
        status_combo.grid(row=3, column=1, padx=10, pady=20)

        # Operation Frame
        operation_frame = LabelFrame(left_frame, bd=3, bg="white", relief=RIDGE, )
        operation_frame.place(x=0, y=350, width=695, height=45 )

        # Import csv button
        save_btn = Button(operation_frame, text="Import csv",command=self.import_csv, width=14,font=("times new roman", 15, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        # Export csv button"
        update_btn = Button(operation_frame, text="Export csv",command=self.export_csv, width=14,font=("times new roman", 15, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        # Delete button
        delete_btn = Button(operation_frame, text="Update", width=14,font=("times new roman", 15, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        # Reset button
        reset_btn = Button(operation_frame, text="Reset",command=self.reset_data, width=14,font=("times new roman", 15, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)



        #Right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance",font=("times new roman", 15, "bold"))
        right_frame.place(x=750, y=10, width=700, height=600)

        # Table Frame
        table_frame = LabelFrame(right_frame, bd=3, bg="white", relief=RIDGE, )
        table_frame.place(x=5, y=5, width=680, height=560)

        #Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,columns=("id", "roll", "name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Student ID")
        self.AttendanceReportTable.heading("name", text="Student Name")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"]= "headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #Fetch Data
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import CSV
    def import_csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    # Export CSV
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open Csv",
                                         filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported"+os.path
                                    .basename(fln)+"Successfully")

        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_student_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance.set(rows[6])

    #Reset data
    def reset_data(self):
        self.var_student_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("Status")














if __name__=="__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()