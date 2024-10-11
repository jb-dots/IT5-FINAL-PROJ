from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from Register import Register
from Menu import HotelManagementSystem
import mysql.connector

def main():
    win = Tk()
    app= Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.resizable(0, 0)
        self.root.title("Login")
        
        window_width = 960
        window_height = 640
        self.center_window(self.root, window_width, window_height)

        self.bg = ImageTk.PhotoImage(file = "LoginBg.png")
        lbl_bg =Label(self.root, image =self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        panel = Frame(self.root, bg= "#89b0a4", width=350, height=380, relief="raised", bd=2)
        panel.place(x=70, y=150)

        heading = Label(panel, text="Welcome", font=("Garamond", 32, "bold"), fg='white', bg= "#89b0a4")
        heading.place(x=80, y=20)

        email_label = Label(panel, text="Email", font=("Arial", 12), bg= "#89b0a4")
        email_label.place(x=30, y=80)
        self.email_entry = Entry(panel, font=("Arial", 12), width=31)
        self.email_entry.place(x=30, y=110)

        password_label = Label(panel, text="Password", font=("Arial", 12), bg= "#89b0a4")
        password_label.place(x=30, y=140)
        self.password_entry = Entry(panel, font=("Arial", 12), width=31, show='*')
        self.password_entry.place(x=30, y=170)

        show_password_var = IntVar()
        show_password_check = Checkbutton(panel, text="Show Password", font=("Arial", 12), variable=show_password_var, onvalue=1, offvalue=0, bg="#89b0a4", command=self.show_password)
        show_password_check.place(x=30, y=200)

        login_button = Button(panel, text="Login", command=self.login, font=("Garamond", 16, "bold"), width=20, fg="white", bg="#aeaf95")
        login_button.place(x=45, y=240)

        register_button = Button(panel, text="New User Register",command=self.register_window, font=("Garamond", 12, "bold"),borderwidth=0, fg="white", bg="#89b0a4")
        register_button.place(x= 30, y=305, width= 135)

        # Forget Pass Button
        forget_button = Button(panel, text="Forget Password",command = self.forgot_password_window, font=("Garamond", 12, "bold"),borderwidth=0, fg="white", bg="#89b0a4")
        forget_button.place(x=30, y=340, width= 120)
        
    def center_window(self, win, width, height):  
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2) - 30
        
        win.geometry(f'{width}x{height}+{x}+{y}')

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)
    
    #==================================== RESET PASSWORD ==========================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error", "Select Security Question")
        elif self.security_entry.get()=="":
            messagebox.showerror("Error", "Please enter the answer")
        elif self.new_password_entry.get()=="":
            messagebox.showerror("Error", "Please enter the new password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotel_management_system")
            my_cursor = conn.cursor()
            query = ("select * from users where email=%s and securityQ =%s and SecurityA = %s")
            value = (self.email_entry.get(), self.combo_security_Q.get(),self.security_entry.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error","Please enter correct answer")
            else:
                query = ("update users set password = %s where email =%s")
                value = (self.new_password_entry.get(),self.email_entry.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login with the new password")

    #==================================== FORGOT PASSWORD WINDOW ==================
    def forgot_password_window(self):
        if self.email_entry.get()=="":
            messagebox.showerror("Error","Please enter the Email Address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotel_management_system")
            my_cursor = conn.cursor()
            query = ("select * from users where email = %s")
            value = (self.email_entry.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("My Error","Please enter the valid email")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("300x330+575+375")

                l = Label(self.root2, text="Forgot Password", font = ("times new roman", 20, "bold"),fg = "red", bg= "white")
                l.place(x = 0, y = 10, relwidth= 1)
                
                security_Q = Label(self.root2, text="Select Security Questions", font= ("times new roman", 15, "bold"), bg = "white", fg = "black")
                security_Q.place(x=20, y=60)
                
                self.combo_security_Q = ttk.Combobox(self.root2, font = ("times new roman", 15, "bold"))
                self.combo_security_Q['values'] = ('Select', 'Your Pet Name', 'Your Birth Place', 'Your Favorite Color', 'Your Best Friend Name')
                self.combo_security_Q.place(x =20, y = 100, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Select Answer", font= ("times new roman", 15, "bold"), bg = "white", fg = "black")
                security_A.place(x=20, y=140)

                self.security_entry = Entry(self.root2,font =("times new roman", 15))
                self.security_entry.place(x=20, y=170, width=250)

                new_password = Label(self.root2, text="New Password", font= ("times new roman", 15, "bold"), bg = "white", fg = "black")
                new_password.place(x=20, y=210)

                self.new_password_entry = Entry(self.root2,font =("times new roman", 15))
                self.new_password_entry.place(x=20, y=240, width=250)

                btn = Button(self.root2, text = "Reset",command=self.reset_pass,font = ("times new roman", 15, "bold"), fg = "white", bg= "green")
                btn.place(x=100, y = 280)



    def menu_window(self):
        self.root_menu = Tk()
        self.app = HotelManagementSystem(self.root_menu)
        self.root_menu.mainloop()    

    def login(self):
        username = self.email_entry.get()
        password = self.password_entry.get()
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotel_management_system")
        my_cursor = conn.cursor()
        query = ("select * from users where email = %s and password = %s")
        value = (username, password)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()
        if row == None:
            messagebox.showerror("Login Failed", "Invalid credentials!")
        else:
            messagebox.showinfo("Login Success", f"Welcome {row[1]}!")
            self.root.destroy() 
            self.menu_window()         
        conn.close()


    def show_password(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')


if __name__ == "__main__":
    main()