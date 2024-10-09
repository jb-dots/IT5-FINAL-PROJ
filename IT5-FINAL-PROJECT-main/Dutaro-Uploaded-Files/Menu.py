from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")  # Window size
        self.root.state("zoomed")

        # ===================== 2nd Image (Left Side) ==================
        try:
            img2 = Image.open("logo.jpeg")
            img2 = img2.resize((230, 140), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
            lblimg2.place(x=0, y=0, width=230, height=140)
        except FileNotFoundError:
            print("Image file not found. Please check the path for the second image.")

        # ===================== 1st Image (Next to the 2nd Image) ==================
        try:
            img1 = Image.open("banner2.png")
            img1 = img1.resize((1320, 140), Image.LANCZOS)  # Adjusted width to fit next to the second image
            self.photoimg1 = ImageTk.PhotoImage(img1)

            lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
            lblimg1.place(x=230, y=0, width=1320, height=140)  # Positioned next to the second image

        except FileNotFoundError:
            print("Image file not found. Please check the path for the first image.")

        # ===================== Title (below the images) =====================
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"),
                          bg="#89b0a4", fg="#f7e7ce", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # ===================== Main Frame =====================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ===================== Menu Label =====================
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"),
                        bg="#0F3325", fg="white", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ===================== Button Frame =====================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=240)  # Increased height from 190 to 240

        # ===================== Buttons =====================
        cust_btn = Button(btn_frame, text="CUSTOMER",command=self.cust_details, width=22, font=("times new roman", 14, "bold"),
                          bg="#89b0a4", fg="#f7e7ce", bd=0)
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM",command=self.room_details, width=22, font=("times new roman", 14, "bold"),
                          bg="#89b0a4", fg="#f7e7ce", bd=0)
        room_btn.grid(row=1, column=0, pady=5)

        details_btn = Button(btn_frame, text="DETAILS",command=self.booking_details,width=22, font=("times new roman", 14, "bold"),
                             bg="#89b0a4", fg="#f7e7ce", bd=0)
        details_btn.grid(row=2, column=0, pady=5)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"),
                            bg="#89b0a4", fg="#f7e7ce", bd=0)
        report_btn.grid(row=3, column=0, pady=5)

        logout_btn = Button(btn_frame, text="LOGOUT",command=self.logout_question, width=22, font=("times new roman", 14, "bold"),
                            bg="#89b0a4", fg="#f7e7ce", bd=0)
        logout_btn.grid(row=4, column=0, pady=5)

        # ===================== Right Side Image =====================
        img3 = Image.open("menubg.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS)  # Adjust the size as needed
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)

        # ===================== Down Images =====================
        img4 = Image.open("leftbuttom1.0.jpeg")
        img4 = img4.resize((230, 210), Image.LANCZOS)  # Adjust the size as needed
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=250, width=230, height=200)

        img5 = Image.open("leftbuttom1.2.jpeg")
        img5 = img5.resize((230, 190), Image.LANCZOS)  # Adjust the size as needed
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)
    
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)
    
    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def booking_details(self):
        self.new_window = Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def logout_question(self):
        question = messagebox.askyesno("Hotel Management System", "Are you sure you want to logout?", parent= self.root)
        if question>0:
            self.root.destroy()
        else:
            if not self.question:
                return



if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()