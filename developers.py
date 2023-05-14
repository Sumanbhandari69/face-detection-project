from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Attendance System")

        # Background image
        img = Image.open("./image_file/background_image.jpeg")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)

        title_lbl = Label(bg_img, text="Developers Information", font=("times new roman", 35, "bold"),
                          bg="blue"
                          , fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=450, y=200, width=600, height=400)
        # Developer info
        dev_label = Label(main_frame, text="Pravin Ale ", font=("times new roman", 20, "bold"),fg="blue",bg="white")
        dev_label.grid(row=0,column=3,padx=90,pady=10)

        dev_label = Label(main_frame, text="pravinale80@gamil.com", font=("times new roman", 20, "bold"), fg="blue", bg="white")
        dev_label.grid(row=1, column=3, padx=90, pady=10)

        dev_label = Label(main_frame, text="Suchit Baniya", font=("times new roman", 20, "bold"), fg="blue", bg="white")
        dev_label.grid(row=2,column=3,padx=90,pady=10)

        dev_label = Label(main_frame, text="suchitbaniya57@gmail.com", font=("times new roman", 20, "bold"), fg="blue", bg="white")
        dev_label.grid(row=3, column=3, padx=90, pady=10)

        dev_label = Label(main_frame, text="Suman Bhandari", font=("times new roman", 20, "bold"), fg="blue", bg="white")
        dev_label.grid(row=4, column=3,padx=90, pady=10)

        dev_label = Label(main_frame, text="sumanbhandari6969@gamil.com", font=("times new roman", 20, "bold"), fg="blue", bg="white")
        dev_label.grid(row=5, column=3, padx=90, pady=10)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()