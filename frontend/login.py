from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import tkinter.ttk as ttk
import frontend.Register
import frontend.dashboard
import frontend.dashboard1
import backend.DBconnect


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x1250+0+0")
        self.root.resizable(False, False)

        self.db = backend.DBconnect.DBConnect()

        # ===================== Adding frame ========================================
        Labeltitle = Label(root, text="SHRESTHA CENTRAL HOSPITAL KATHMANDU", font=('ariel', 30, 'bold'),bd=10, fg='white',bg='deep sky blue')
        Labeltitle.pack(fill=X)

        self.bg= ImageTk.PhotoImage(Image.open("frontend/image/hospital1.jpg"))
        self.bg1= ImageTk.PhotoImage(Image.open("frontend/image/hospital2.jpg"))

        bg1=Label(self.root,image=self.bg).pack()


        login_system_frame = Frame(self.root)
        login_system_frame.place(x=20, y=80,height=265, width=550)

        login_frame=Label(login_system_frame,image=self.bg1).pack()



        # ==================================Title for Frame#========================
        title = Label(login_system_frame, text=" Login Here", fg="black",font=("arial Bold", 15))
        title.place(x=0, y=0, relwidth=1)

        username = Label(login_system_frame, text=" Username", fg='black', font=("arial bold", 14),bd=5)
        username.place(x=60, y=90)

        # ====================================Entry  Username===================
        self.entry1 = StringVar()
        self.username_entry = Entry(login_system_frame, bd=8, textvar=self.entry1, width=15,font=("arial bold", 14))
        self.username_entry.place(x=200, y=90)
        # ====================================password lebel====================
        password_entry = Label(login_system_frame, text="Password", fg='black', font=("Arial bold", 14), bd=5)
        password_entry.place(x=60, y=160)
        # =================Entry for password==================================
        self.entry2 = StringVar()
        self.password1_entry = Entry(login_system_frame, bd=8, textvar=self.entry2, show="*****", width=15, font=("arial bold", 14))
        self.password1_entry.place(x=200, y=160)

        #=================================Button for Login=====================
        self.button2 = Button(login_system_frame, text="Login", command=self.login, width=8, height=1, bd=6, fg="black", font=("arial bold", 14))
        self.button2.place(x=10, y=210)

        self.button3 = Button(login_system_frame, text="Reset", width=8, height=1, bd=6,command=self.Reset,
                              fg="black", font=("arial bold", 14))
        self.button3.place(x=123, y=210)

        self.button4 = Button(login_system_frame, text="Exit", command=self.Exit,width=8, height=1, bd=6,
                               fg="black", font=("arial bold", 14))
        self.button4.place(x=233, y=210)

        self.button5 = Button(login_system_frame, text=" Patient Register", bd=6,fg="Red",
                              font=("arial bold", 14),command=self.register)
        self.button5.place(x=345, y=210)


    # =======================Login into hospital management system=====================
    def login(self):
        uname = self.username_entry.get()
        passw = self.password1_entry.get()

        if self.username_entry.get() == '' or self.password1_entry.get() == '':
            messagebox.showerror('Error', 'plz fill the empty field')
        else:
            query = "select * from ashokregister where username=%s and password=%s"
            values = (uname, passw)
            rows = self.db.login(query,values)
            data = []
            print(rows)
            if len(rows) != 0:
                for row in rows:
                    data.append(row[0])
                    data.append(row[1])
                print(data)
                if uname == data[0] and passw == data[1]:

                    self.btnRegistration = Button(self.root, text="Patient Administration System", bd=10,fg="red",
                                                  command=self.PatienAdministrationSystem, font=('ariel', 12, 'bold'))

                    self.btnRegistration.place(x=30,y=350)

                    self.btnHospital = Button(self.root, text="Hospital Management System", bd=10,fg="red",
                                              command=self.HospitalManagementSystem, font=('ariel', 12, 'bold'))
                    self.btnHospital.place(x=30,y=400)

                    messagebox.showinfo('Success', 'login successfull')




                else:
                    messagebox.showerror('Error', 'Invalid username and password')
            else:
                messagebox.showinfo("Error", "User not registered !! Register first")





    def Reset(self):
        self.entry1.set(""),
        self.entry2.set("")


    def Exit(self):
        self.Exit = messagebox.askyesno("Login","Confirm if you want to exit")
        if self.Exit>0:
            self.root.destroy()
            return


    def register(self):
        root = Toplevel()
        frontend.Register.Register_Page(root)

    def PatienAdministrationSystem(self):
        root = Toplevel()
        frontend.dashboard.Patient(root)


    def HospitalManagementSystem(self):
        root = Toplevel()
        frontend.dashboard1.HospitalMain(root)



