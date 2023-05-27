import csv
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
import cv2
import numpy as np
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
from attendance import Attendance
from developers import Developer
#import cv2.face

class Face_Recognition_System:
    def __init__(self,root): 
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Attendance System")

        #Background image
        img = Image.open("./image_file/background_image.jpeg")
        img = img.resize((1530,790),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)

        title_lbl =Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",35, "bold"),bg= "blue"
                         ,fg="white")
        title_lbl.place(x=0,y=0,width=1530,height= 50)

        #Student Button
        img1 = Image.open("./image_file/button_image.jpeg")
        img1 = img1.resize((250, 250), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(bg_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x= 200,y=100,width= 250,height=250)

        b1_1 = Button(bg_img, text="Students Details",command=self.student_details, cursor="hand2",font=("times new roman",20, "bold"),bg="blue",fg="white")
        b1_1.place(x=200, y=350, width=250, height=40)

        # Detect face Button
        img2 = Image.open("./image_file/face_detector_image.jpeg")
        img2 = img2.resize((250, 250), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2 = Button(bg_img,command=self.face_recog, image=self.photoimg2, cursor="hand2")
        b2.place(x=600, y=100, width=250, height=250)

        b2_1 = Button(bg_img,command=self.face_recog, text="Face Detector", cursor="hand2", font=("times new roman", 20, "bold"),bg="blue",fg="white")
        b2_1.place(x=600, y=350, width=250, height=40)

        # Attendance Button
        img3 = Image.open("./image_file/Attendance_image.jpeg")
        img3 = img3.resize((250, 250), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3 = Button(bg_img, image=self.photoimg3,command=self.attendance_data, cursor="hand2")
        b3.place(x=1000, y=100, width=250, height=250)

        b3_1 = Button(bg_img, text="Attendance",command=self.attendance_data, cursor="hand2", font=("times new roman", 20, "bold"),bg="blue",fg="white")
        b3_1.place(x=1000, y=350, width=250, height=40)

        # Train dataset Button
        img4 = Image.open("./image_file/train_dataset_image.jpeg")
        img4 = img4.resize((250, 250), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4 = Button(bg_img,command=self.train_classifier, image=self.photoimg4, cursor="hand2")
        b4.place(x=200, y=450, width=250, height=250)

        b4_1 = Button(bg_img,command=self.train_classifier, text="Train Data", cursor="hand2", font=("times new roman", 20, "bold"),bg="blue",fg="white")
        b4_1.place(x=200, y=700, width=250, height=40)

        # Developers Button
        img5 = Image.open("./image_file/Developers_image.jpeg")
        img5 = img5.resize((250, 250), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b5 = Button(bg_img, image=self.photoimg5,command=self.developer_data, cursor="hand2")
        b5.place(x=600, y=450, width=250, height=250)

        b5_1 = Button(bg_img, text="Developers", cursor="hand2",command=self.developer_data, font=("times new roman", 20, "bold"),bg="blue",fg="white")
        b5_1.place(x=600, y=700, width=250, height=40)

        # Exit Button
        img6 = Image.open("./image_file/Exit_image.jpeg")
        img6 = img6.resize((250, 250), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.iExit)
        b6.place(x=1000, y=450, width=250, height=250)

        b6_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 20, "bold"),bg="blue",fg="white",command=self.iExit)
        b6_1.place(x=1000, y=700, width=250, height=40)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman", 15, "bold"),bg="blue",fg="white")
        lbl.place(x=10,y=0, width=110, height=50)
        time()


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit? ",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


    #=========Functions button==========
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces =[]
        ids =[]

        for image in path:
            img = Image.open(image).convert('L') #Gray scale
            imagenp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13


        ids = np.array(ids)

        #Train classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
    #Attendance
    def mark_attendance(self,i,r,n,d):

        with open("Attendance.csv", "r+", newline="\n") as f:
            reader = csv.reader(f)
            attendance_records = list(reader)
            name_list = set(row[0] for row in attendance_records)
            today = datetime.now().strftime("%d/%m/%Y")
            today_marked = any(row[-2] == today and row[0] == i for row in attendance_records)

            if not today_marked:
                now = datetime.now()
                dt_string = now.strftime("%H:%M:%S")
                d1 = now.strftime("%d/%m/%Y")
                with open("Attendance.csv", "a", newline="\n") as f:
                    writer = csv.writer(f)
                    writer.writerow([i, r, n, d, dt_string, d1, "Present"])




    #face recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scalefactor,minneighbour,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scalefactor,minneighbour)

            coord = []
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence =int((100*(1-predict/300)))
                # print(predict)
                # print(confidence)

                conn = mysql.connector.connect(host="localhost", username="root", password="9818913355",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select Name from student where Student_ID="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_ID=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_ID=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Student_ID from student where Student_ID=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)



                if confidence>80:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord =[x,y,w,h]
            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,face_cascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)













if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
