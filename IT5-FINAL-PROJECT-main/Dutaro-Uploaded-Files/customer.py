from importlib.resources import contents
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer")
        self.root.geometry("1135x550+220+220")

        # ================== Title (below the images) =====================
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"),
                          bg="#89b0a4", fg="#f7e7ce", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1290, height=50)

        # ================== Logo Image =====================
        try:
            img2 = Image.open("logo.jpeg")
            img2 = img2.resize((100, 40), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
            lblimg2.place(x=5, y=2, width=105, height=50)
        except FileNotFoundError:
            print("Image file not found. Please check the path for the logo image.")
            lblimg2 = Label(self.root, text="Logo", font=("times new roman", 18, "bold"), bg="#89b0a4", fg="#f7e7ce")
            lblimg2.place(x=5, y=2, width=105, height=50)

        # ================== Label Frame for Customer Details =====================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",
                                    font=("times new roman", 18, "bold"),
                                    bg="#89b0a4", fg="#f7e7ce")
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ================== Customer Ref =====================
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=("times new roman", 12, "bold"),
                             padx=2, pady=6, bg="#89b0a4", fg="white")
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        self.entry_ref = ttk.Entry(labelframeleft, width=29, font=("times new roman", 13, "bold"))
        self.entry_ref.grid(row=0, column=1)

        # ================== Customer Name =====================
        cname = Label(labelframeleft, text="Customer Name:", font=("times new roman", 12, "bold"),
                      padx=2, pady=6, bg="#89b0a4", fg="white")
        cname.grid(row=1, column=0, sticky=W)
        self.txtcname = ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=29)
        self.txtcname.grid(row=1, column=1)

        # ================== Gender Combobox =====================
        lbl_gender = Label(labelframeleft, text="Gender:", font=("times new roman", 12, "bold"),
                           padx=2, pady=6, bg="#89b0a4", fg="white")
        lbl_gender.grid(row=2, column=0, sticky=W)
        self.combo_gender = ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=27, state="readonly")
        self.combo_gender["values"] = ("Male", "Female", "Other")
        self.combo_gender.grid(row=2, column=1)

        # ================== Postcode =====================
        lbl_postcode = Label(labelframeleft, text="Postcode:", font=("times new roman", 12, "bold"),
                             padx=2, pady=6, bg="#89b0a4", fg="white")
        lbl_postcode.grid(row=3, column=0, sticky=W)
        self.txt_postcode = ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=29)
        self.txt_postcode.grid(row=3, column=1)

        # ================== Mobile Number =====================
        lbl_mobile = Label(labelframeleft, text="Mobile Number:", font=("times new roman", 12, "bold"),
                           padx=2, pady=6, bg="#89b0a4", fg="white")
        lbl_mobile.grid(row=4, column=0, sticky=W)
        self.txt_mobile = ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=29)
        self.txt_mobile.grid(row=4, column=1)

        # ================== Email =====================
        lbl_email = Label(labelframeleft, text="Email:", font=("times new roman", 12, "bold"),
                          padx=2, pady=6, bg="#89b0a4", fg="white")
        lbl_email.grid(row=5, column=0, sticky=W)
        self.txt_email = ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=29)
        self.txt_email.grid(row=5, column=1)

        # ================== Nationality =====================
        lbl_nationality = Label(labelframeleft, text="Nationality:", font=("times new roman", 12, "bold"),
                                padx=2, pady=6, bg="#89b0a4", fg="white")
        lbl_nationality.grid(row=6, column=0, sticky=W)
        self.txt_nationality = ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=29)
        self.txt_nationality.grid(row=6, column=1)

        # ================== ID Proof Type Combobox =====================
        lbl_idproof = Label(labelframeleft, text="ID Proof Type:", font=("times new roman", 12, "bold"),
                            padx=2, pady=6, bg="#89b0a4", fg="white")
        lbl_idproof.grid(row=7, column=0, sticky=W)
        self.combo_idproof = ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=27, state="readonly")
        self.combo_idproof["values"] = ("Passport", "Driving License", "National ID", "Voter ID")
        self.combo_idproof.grid(row=7, column=1)

        # ================== ID Number =====================
        lbl_idnumber = Label(labelframeleft, text="ID Number:", font=("times new roman", 12, "bold"),
                             padx=2, pady=6, bg="#89b0a4", fg="white")
        lbl_idnumber.grid(row=8, column=0, sticky=W)
        self.txt_idnumber = ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=29)
        self.txt_idnumber.grid(row=8, column=1)

        # ================== Address =====================
        lbl_address = Label(labelframeleft, text="Address:", font=("times new roman", 12, "bold"),
                            padx=2, pady=6, bg="#89b0a4", fg="white")
        lbl_address.grid(row=9, column=0, sticky=W)
        self.txt_address = ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=29)
        self.txt_address.grid(row=9, column=1)

        # ================== Buttons =====================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="ADD", command=self.add_data, font=("times new roman", 12, "bold"), bg="#0F3325", fg="white", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="UPDATE", command=self.update_data , font=("times new roman", 12, "bold"), bg="#0F3325", fg="white", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="DELETE",command=self.delete_data, font=("times new roman", 12, "bold"), bg="#0F3325", fg="white", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="RESET",command=self.reset, font=("times new roman", 12, "bold"), bg="#0F3325", fg="white", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # ================== Table Frame =====================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",
                                 font=("times new roman", 12, "bold"),
                                 bg="#89b0a4", fg="#f7e7ce")
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchby = Label(Table_Frame, text="Search By:", font=("times new roman", 12, "bold"),
                            bg="#89b0a4", fg="white")
        lblSearchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=24,
                                    state="readonly")
        combo_search["value"] = ("Mobile", "Ref")
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="SEARCH", font=("times new roman", 12, "bold"), bg="#0F3325", fg="white", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="SHOW ALL", font=("times new roman", 12, "bold"), bg="#0F3325", fg="white", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # ================== Show Data Table =====================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=850, height=300)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column=("ref", "name", "gender", "postcode", "mobile", "email", "nationality", "idproof", "idnumber", "address"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("postcode", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="Id Proof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("postcode", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.Cust_Details_Table.bind()
        self.fetch_data()

    # Function to add data into the database
    def add_data(self):
        if self.entry_ref.get() == "" or self.txtcname.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel_management_system")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO customer (ref, name, gender, postcode, mobile, email, nationality, idproof, idnumber, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.entry_ref.get(),
                    self.txtcname.get(),
                    self.combo_gender.get(),
                    self.txt_postcode.get(),
                    self.txt_mobile.get(),
                    self.txt_email.get(),
                    self.txt_nationality.get(),
                    self.combo_idproof.get(),
                    self.txt_idnumber.get(),
                    self.txt_address.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Customer details have been added.")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Database Error: {e}")

    def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel_management_system")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM customer")
            rows = cursor.fetchall()
            if len(rows) !=0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for row in rows:
                    self.Cust_Details_Table.insert("", END, values=row)
                    conn.commit()
                conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.entry_ref.delete(0, END)
        self.entry_ref.insert(END, row[0])

        self.txtcname.delete(0, END)
        self.txtcname.insert(END, row[1])

        self.combo_gender.set(row[2])

        self.txt_postcode.delete(0, END)
        self.txt_postcode.insert(END, row[3])

        self.txt_mobile.delete(0, END)
        self.txt_mobile.insert(END, row[4])

        self.txt_email.delete(0, END)
        self.txt_email.insert(END, row[5])

        self.txt_nationality.delete(0, END)
        self.txt_nationality.insert(END, row[6])

        self.combo_idproof.set(row[7])

        self.txt_idnumber.delete(0, END)
        self.txt_idnumber.insert(END, row[8])

        self.txt_address.delete(0, END)
        self.txt_address.insert(END, row[9])

    def update_data(self):
        if self.txtcname.get() == "" or self.txt_mobile.get() == "":
            messagebox.showerror("Error","Please select a record to update")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel_management_system")
            mycursor = conn.cursor()
            mycursor.execute("UPDATE customer SET name=%s, gender=%s, postcode=%s, mobile=%s, email=%s, nationality=%s, idproof=%s, idnumber=%s, address=%s WHERE ref=%s", (

                self.entry_ref.get(),
                self.txtcname.get(),
                self.combo_gender.get(),
                self.txt_postcode.get(),
                self.txt_mobile.get(),
                self.txt_email.get(),
                self.txt_nationality.get(),
                self.combo_idproof.get(),
                self.txt_idnumber.get(),
                self.txt_address.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details has been updated successfully", parent=self.root)


    def delete_data(self):
        Delete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?",
                                      parent=self.root)
        if Delete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel_management_system")
            mycursor = conn.cursor()
            query = "DELETE FROM customer WHERE ref=%s"
            value = (self.entry_ref.get(),)
            mycursor.execute(query, value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        self.entry_ref.delete(0, END)
        self.txtcname.delete(0, END)
        self.combo_gender.set("")
        self.txt_postcode.delete(0, END)
        self.txt_mobile.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_nationality.delete(0, END)
        self.combo_idproof.set("")
        self.txt_idnumber.delete(0, END)
        self.txt_address.delete(0, END)


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
