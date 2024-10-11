import tkinter as tk
from Login import Login_Window
from Menu import HotelManagementSystem

class HotelManagementSystemMain:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hotel Management System")
        self.root.geometry("960x640+0+0")

        self.login_register = Login_Window(self.root)
        #self.login_register.pack(fill="both", expand=True)

        self.root.mainloop()

    def open_menu(self):
        #self.login_register.pack_forget()
        self.menu = HotelManagementSystem(self.root)
        #self.menu.pack(fill="both", expand=True)

    

if __name__ == "__main__":
    main = HotelManagementSystemMain()
