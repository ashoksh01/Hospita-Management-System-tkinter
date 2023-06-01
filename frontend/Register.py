from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import model.user
import backend.DBconnect


class Register_Page:
    def __init__(self,root):
        self.root=root
        self.root.title('Patient Registration')
        self.root.geometry('450x400')

        lbl_heading=Label(self.root,text='Patient Registration:',bg='deep sky blue',fg='red',font=('arial',20,'bold'))
        lbl_heading.pack(side=TOP,fill=X)

        main_frame=Frame(self.root,bd=10,relief=SUNKEN,bg='green')
        main_frame.place(x=10,y=50,width=410,height=250)

        self.db=backend.DBconnect.DBConnect()

        lbl_uname=Label(main_frame,text='Username',font=('arial',15,'bold'),bg='green',fg='black')
        lbl_uname.grid(row=0,column=0,padx=8,pady=10)

        self.username=Entry(main_frame,font=('arial',15,'bold'))
        self.username.grid(row=0,column=1,padx=8,pady=10)

        lbl_password = Label(main_frame, text='Password', font=('arial', 15, 'bold'),bg='green', fg='black')
        lbl_password.grid(row=1, column=0, padx=8, pady=10)

        self.ent_password = Entry(main_frame, font=('arial', 15, 'bold'))
        self.ent_password.grid(row=1, column=1, padx=8, pady=10)

        lbl_add = Label(main_frame, text='Blood Group', font=('arial', 15, 'bold'),bg='green', fg='black')
        lbl_add.grid(row=2, column=0, padx=8, pady=10)

        self.ent_blood = Entry(main_frame, font=('arial', 15, 'bold'))
        self.ent_blood.grid(row=2, column=1, padx=8, pady=10)

        lbl_add = Label(main_frame,text='Gender',font=('arial',15,'bold'),bg='green',fg='black')
        lbl_add.grid(row=3,column=0,padx=8,pady=10)

        self.cmb_gender=ttk.Combobox(main_frame,font=('arial', 14, 'bold'))
        self.cmb_gender['values']=('Male','Female','Others')
        self.cmb_gender.grid(row=3,column=1)

        btn_frame=Frame(self.root,bd=5,relief=GROOVE,bg='red')
        btn_frame.place(x=20,y=310,width=400,height=60)

        btn_register=Button(btn_frame,text='Register',font=('arial', 15, 'bold'),width=8,bd=8,relief=GROOVE,command=self.Add,padx=5)
        btn_register.place(x=10)

        btn_reset = Button(btn_frame, text='Reset', font=('arial', 15, 'bold'), width=8, bd=8, relief=GROOVE,command=self.Reset,padx=5)
        btn_reset.place(x=135)

        btn_Exit = Button(btn_frame, text='Exit', font=('arial', 15, 'bold'), width=8, bd=8, relief=GROOVE,command=self.Exit, padx=5)
        btn_Exit.place(x=260)

    def Reset(self):
        self.username.delete(0,END)
        self.ent_password.delete(0,END)
        self.ent_blood.delete(0,END)

        self.username.insert(0,'')
        self.ent_password.insert(0,'')
        self.ent_blood.insert(0,'')

    def Exit(self):
        self.Exit = messagebox.askyesno("Patient Registration","Confirm if you want to exit")
        if self.Exit>0:
            self.root.destroy()
            return

    def Add(self):
        username = self.username.get()
        password = self.ent_password.get()
        blood = self.ent_blood.get()
        gender = self.cmb_gender.get()

        if username == '' or password == '' or blood == '' or gender == '':
            messagebox.showerror('Error', 'Please fill the empty field')
            return
        else:

            u = model.user.User(username,password,blood,gender)

            query = "insert into ashokregister(Username,Password,BloodGroup,Gender) values(%s,%s,%s,%s)"
            values = (u.get_username(), u.get_password(), u.get_bloodgroup(), u.get_gender())

            self.db.insert(query, values)
            messagebox.showinfo('Success', 'User Registration successfull')
            self.root.destroy()



