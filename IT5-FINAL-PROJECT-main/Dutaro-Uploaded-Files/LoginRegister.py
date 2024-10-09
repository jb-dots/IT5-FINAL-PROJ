import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Application")

        # Initialize the login frame
        self.login_frame = LoginRegister(self.root, self)
        self.login_frame.pack(fill="both", expand=True)

    def open_menu(self):
        # Destroy the current frame (login) and load a new frame (menu)
        self.login_frame.pack_forget()
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(fill="both", expand=True)

        welcome_label = tk.Label(menu_frame, text="Welcome to the Main Menu!", font=("Arial", 24))
        welcome_label.pack(pady=50)

        logout_button = tk.Button(menu_frame, text="Logout", font=("Arial", 14), command=self.logout)
        logout_button.pack(pady=20)

    def logout(self):
        # Reload the login frame
        self.login_frame = LoginRegister(self.root, self)
        self.login_frame.pack(fill="both", expand=True)


class LoginRegister(tk.Frame):  # Inherit from tk.Frame
    def __init__(self, root, main):
        super().__init__(root)  # Initialize the frame
        self.root = root
        self.main = main
        self.root.resizable(0, 0)
        self.root.title("LOGIN")

        window_width = 960
        window_height = 640
        self.center_window(self.root, window_width, window_height)

        # Background Image
        bgImage = ImageTk.PhotoImage(Image.open("LoginBg.png"))
        bgLabel = tk.Label(self, image=bgImage)  # Changed self.root to self to place in the frame
        bgLabel.place(x=0, y=0)

        # Login Panel
        panel_color = '#89b0a4'
        panel = tk.Frame(self, bg=panel_color, width=350, height=380, relief="raised", bd=2)
        panel.place(x=70, y=150)

        # Welcome Heading
        heading = tk.Label(panel, text="Welcome", font=("Garamond", 32, "bold"), fg='white', bg=panel_color)
        heading.place(x=80, y=20)

        # Username Entry
        username_label = tk.Label(panel, text="Username", font=("Arial", 12), bg=panel_color)
        username_label.place(x=30, y=80)
        self.username_entry = tk.Entry(panel, font=("Arial", 12), width=31)
        self.username_entry.place(x=30, y=110)

        # Password Entry
        password_label = tk.Label(panel, text="Password", font=("Arial", 12), bg=panel_color)
        password_label.place(x=30, y=140)
        self.password_entry = tk.Entry(panel, font=("Arial", 12), width=31, show='*')
        self.password_entry.place(x=30, y=170)

        # Show Password Checkbox
        show_password_var = tk.IntVar()
        show_password_check = tk.Checkbutton(panel, text="Show Password", font=("Arial", 12),
                                             variable=show_password_var, onvalue=1, offvalue=0, bg=panel_color,
                                             command=self.show_password)
        show_password_check.place(x=30, y=200)

        # Login Button
        login_button = tk.Button(panel, text="Login", font=("Garamond", 16, "bold"), width=20, fg="white", bg="#aeaf95",
                                 command=self.login)
        login_button.place(x=45, y=270)

        # Prevent garbage collection of the image
        self.bgImage = bgImage

    def center_window(self, win, width, height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2) - 30

        win.geometry(f'{width}x{height}+{x}+{y}')

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "admin":
            messagebox.showinfo("Login Success", f"Welcome {username}!")
            self.main.open_menu()  # Call open_menu method to switch views
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!")

    def show_password(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')


# Start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
