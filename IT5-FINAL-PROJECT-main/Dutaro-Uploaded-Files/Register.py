from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register():
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.resizable(0,0)
        
        window_width = 960
        window_height = 640
        self.center_window(self.root, window_width, window_height)

        #============ variables ==========
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()


        #==========Bg Image ===========
        self.bg = ImageTk.PhotoImage(file = "register.png")
        bg_lbl = Label(self.root, image = self.bg)
        bg_lbl.place(x = 0, y = 0, relwidth=1, relheight= 1)
    
        self.bg1 = ImageTk.PhotoImage(file = "leftbg.png")
        left_lbl = Label(self.root, image = self.bg1)
        left_lbl.place(x = 20, y = 80, width=400, height = 500)
    

        frame = Frame(self.root, bg = "white")
        frame.place(x = 350, y = 80, width = 580, height =500)

        register_lbl = Label(frame, text= "REGISTER HERE", font=("times new roman", 20, "bold"), fg = "darkgreen", bg = "white")
        register_lbl.place(x = 180, y = 20)


        #==============Label and Entry==================

        fname = Label(frame, text = "First Name", font=("times new roman", 15, "bold"), bg="white", fg= "black")
        fname.place(x = 20, y = 100)

        self.fname_entry = Entry(frame, textvariable=self.var_fname,font=("times new roman", 15))
        self.fname_entry.place(x =20, y=130,width=250)

        lname = Label(frame, text = "Last Name", font=("times new roman", 15, "bold"), bg="white", fg = "black")
        lname.place(x = 320, y = 100)

        self.lname_entry = Entry(frame,textvariable=self.var_lname, font=("times new roman", 15))
        self.lname_entry.place(x =320, y=130,width=250)

        contact = Label(frame, text = "Contact Number", font=("times new roman", 15, "bold"), bg="white", fg= "black")
        contact.place(x = 20, y = 170)

        self.contact_entry = Entry(frame,textvariable=self.var_contact, font=("times new roman", 15))
        self.contact_entry.place(x =20, y=200,width=250)

        email = Label(frame, text = "Email", font=("times new roman", 15, "bold"), bg="white", fg= "black")
        email.place(x = 320, y = 170)

        self.email_entry = Entry(frame,textvariable=self.var_email, font=("times new roman", 15))
        self.email_entry.place(x =320, y=200,width=250)
        
        #---------row 3

        security_Q = Label(frame, text="Select Security Questions", font= ("times new roman", 15, "bold"), bg = "white", fg = "black")
        security_Q.place(x=20, y=240)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ, font = ("times new roman", 15, "bold"))
        self.combo_security_Q['values'] = ('Select', 'Your Pet Name', 'Your Birth Place', 'Your Favorite Color', 'Your Best Friend Name')
        self.combo_security_Q.place(x =20, y = 270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Select Answer", font= ("times new roman", 15, "bold"), bg = "white", fg = "black")
        security_A.place(x=320, y=240)

        self.security_entry = Entry(frame,textvariable=self.var_securityA,font =("times new roman", 15))
        self.security_entry.place(x=320, y=270, width=250)

        password  = Label(frame, text = "Password ", font=("times new roman", 15, "bold"),bg= "white", fg= "black")
        password.place(x=20, y=310)

        self.password_entry = Entry(frame,textvariable=self.var_pass,font =("times new roman", 15))
        self.password_entry.place(x=20, y=340, width=250)

        confirm_password  = Label(frame, text = "Confirm Password ", font=("times new roman", 15, "bold"),bg= "white", fg= "black")
        confirm_password.place(x=320, y=310)

        self.conf_password_entry = Entry(frame,textvariable=self.var_confpass,font =("times new roman", 15))
        self.conf_password_entry.place(x=320, y=340, width=250)

        #=========== CHECK BUTTON ==========
        self.var_check = IntVar()
        self.Checkbtn = Checkbutton(frame,variable=self.var_check,text = "I Agree on The Terms and Conditions", font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        self.Checkbtn.place(x=20, y=380)

        #=========== BUTTONS ==============
        register_now_button = Button(frame, text="Register Now", font=("Garamond", 12, "bold"), 
                                    borderwidth=3, relief="ridge", fg="white", bg="red", command= self.register_data)
        register_now_button.place(x= 170, y=430, width= 250, height= 50)

        # login_button = Button(frame, text="Login Now", font=("Garamond", 12, "bold"),
        #                     borderwidth=3, relief="ridge", fg="white", bg="blue" ,command=self.login_window)
        # login_button.place(x=300, y=430, width= 250, height= 50)

        #=========== FUNCTION DECLARATION =========
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "Please Fill All Fields")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should be Same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please Agree on The Terms and Conditions")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotel_management_system")
            my_cursor = conn.cursor()
            query = ("select * from users where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User  Already Exist, Please Try Another Email")
            else:
                my_cursor.execute("insert into users (fname, lname, contact, email, securityQ, securityA, password) values(%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully")

    def login_window(self):
        self.root.destroy()  # Destroy current register window
        import Login
        Login.main() # Destroy current register window        
    def center_window(self, win, width, height):  
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2) - 30
        
        win.geometry(f'{width}x{height}+{x}+{y}')

if __name__ ==  "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()