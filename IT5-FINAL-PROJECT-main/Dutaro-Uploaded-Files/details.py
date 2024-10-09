
import random
from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

#--------------logo - --------------------
        try:
            img2 = Image.open("logo.jpeg")
            img2 = img2.resize((100, 40), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
            lblimg2.place(x=5, y=5, width=100, height=40)

        except FileNotFoundError:
            print("Image file not found. Please check the path for the first image.")

        #-------------title--------------------
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="#89b0a4", fg="#f7e7ce", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

# -------------labelframe----------------------
        lblframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add",font=("times new roman", 12, "bold"),bg="#89b0a4", fg="#f7e7ce")
        lblframeleft.place(x=5, y=50, width=1500, height=500)
#Floor
        lblfloor=Label(lblframeleft,text="Floor",font=("times new roman",12,"bold"),padx=2,pady=6,bg="#89b0a4", fg="#f7e7ce")
        lblfloor.grid(row=0,column=0,sticky=W,padx=20)

        self.varfloor=StringVar()
        entryfloor=ttk.Entry(lblframeleft,textvariable=self.varfloor,font=("times new roman",13,"bold"),width=20)
        entryfloor.grid(row=0,column=1,sticky=W)

#room number
        lblroom=Label(lblframeleft,text="Room No",font=("times new roman",12,"bold"),padx=2,pady=6,bg="#89b0a4", fg="#f7e7ce")
        lblroom.grid(row=1,column=0,sticky=W,padx=20)

        self.varroom=StringVar()
        entryroom=ttk.Entry(lblframeleft,textvariable=self.varroom,font=("times new roman",13,"bold"),width=20)
        entryroom.grid(row=1,column=1,sticky=W)

#room type
        lblroomtype=Label(lblframeleft,text="Room Type",font=("times new roman",12,"bold"),padx=2,pady=6,bg="#89b0a4", fg="#f7e7ce")
        lblroomtype.grid(row=2,column=0,sticky=W,padx=20)

        self.vartype=StringVar()
        entryroomtype=ttk.Entry(lblframeleft,textvariable=self.vartype,font=("times new roman",13,"bold"),width=20)
        entryroomtype.grid(row=2,column=1,sticky=W)

#-------------------btns------------------
        buttonframe=Frame(lblframeleft,bd=2,relief=RIDGE)
        buttonframe.place(x=0,y=200,width=412,height=40)

        buttonadd=Button(buttonframe, text="Add", command=self.add_data, font=("times new roman", 12, "bold"), bg="#0F3325", fg="white", width=10)
        buttonadd.grid(row=0,column=0,padx=1)

        buttonupdate = Button(buttonframe, text="Update",command=self.update, font=("times new roman", 12, "bold"), bg="#0F3325", fg="white",width=10)
        buttonupdate.grid(row=0, column=1, padx=1)

        buttondelete = Button(buttonframe, text="Delete",command=self.mDelete, font=("times new roman", 12, "bold"), bg="#0F3325", fg="white",width=10)
        buttondelete.grid(row=0, column=2, padx=1)

        buttonreset = Button(buttonframe, text="Reset",command=self.reset_data, font=("times new roman", 12, "bold"), bg="#0F3325", fg="white",width=10)
        buttonreset.grid(row=0, column=3, padx=1)

#----------------table frame search system-------------
        Tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2,bg="#89b0a4", fg="#f7e7ce")
        Tableframe.place(x=600,y=50,width=600,height=400)

        scrollx=ttk.Scrollbar(Tableframe,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(Tableframe,orient=VERTICAL)
        self.roomtable=ttk.Treeview(Tableframe,column=("floor","roomno","roomtype",),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.roomtable.xview)
        scrolly.config(command=self.roomtable.yview)

        self.roomtable.heading("floor",text="Floor")
        self.roomtable.heading("roomno", text="Room No")
        self.roomtable.heading("roomtype", text="Room Type")

        self.roomtable["show"]="headings"

        self.roomtable.column("floor", width=100)
        self.roomtable.column("roomno", width=100)
        self.roomtable.column("roomtype", width=100)

        self.roomtable.pack(fill=BOTH,expand=1)
        self.roomtable.bind("<ButtonRelease-1>", self.get_cursor)
        self.roomtable.bind()
        self.fetch_data()

    def add_data(self):
        if self.varfloor.get()=="" or self.vartype.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", user="root", password="", database="hotel_management_system")
                mycursor=conn.cursor()
                mycursor.execute("INSERT INTO details (floor, roomno, roomtype) VALUES (%s,%s,%s)",(

                    self.varfloor.get(),
                    self.varroom.get(),
                    self.vartype.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showerror("Database Error",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="", database="hotel_management_system")
        mycursor=conn.cursor()
        mycursor.execute("SELECT * FROM details")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.roomtable.delete(*self.roomtable.get_children())
            for i in rows:
                self.roomtable.insert("",END,values=i)
                conn.commit()
            conn.close()

    def get_cursor(self,event=""):
        cursorrow=self.roomtable.focus()
        content=self.roomtable.item(cursorrow)
        row=content["values"]

        self.varfloor.set(row[0])
        self.varroom.set(row[1])
        self.vartype.set(row[2])

    def update(self):
        if self.varfloor.get()=="":
            messagebox.showerror("Error", "Please enter floor number", parent=self.root)
        else:
            conn=mysql.connector.connect(host ="localhost", username="root", password="", database="hotel_management_system")
            mycursor=conn.cursor()
            mycursor.execute("UPDATE details SET floor=%s,roomtype=%s WHERE roomno=%s",(

                self.varfloor.get(),
                self.vartype.get(),
                self.varroom.get(),
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New room details has been updated successfully", parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost", username="root", password="", database="hotel_management_system")
            mycursor=conn.cursor()
            query="DELETE FROM details WHERE roomno=%s"
            value=(self.varroom.get(),)
            mycursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        self.varfloor.set(""),
        self.varroom.set(""),
        self.vartype.set("")







if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()

