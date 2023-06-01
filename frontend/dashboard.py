from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import mysql.connector
import backend.DBconnect
import model.user

db=backend.DBconnect.DBConnect()

class Patient:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Administration System"),
        self.root.geometry('1350x750+0+0')
        self.frame = Frame(self.root)
        self.frame.pack()


        self.Date= StringVar()
        self.IDtype = StringVar()
        self.Member = StringVar()
        self.Payment = StringVar()
        self.Patientfee = IntVar()
        self.Firstname = StringVar()
        self.Lastname = StringVar()
        self.Address = StringVar()
        self.Telephone = StringVar()
        self.Postcode = StringVar()
        self.ref = StringVar()
        self.Patientfees = StringVar()
        self.Patientfees.set("0")

        #====================== Tile frame================
        TitleFrame = Frame(self.frame, bd=10, width=1350, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, text="Patient Administration", font=('ariel', 30, 'bold'),bg='deep sky blue',fg='red')
        self.lblTitle.grid()
        #================== button frame=============================

        MemberDetailsFrame = LabelFrame(self.frame, width=1350, height=500, bd=8, pady=30, relief=RIDGE,bg='#789e9e')
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailsFrame, width=880, height=500, bd=8, relief=RIDGE,bg='#789e9e')
        FrameDetails.pack(side=LEFT)

        MemberName_F = LabelFrame(FrameDetails, bd=8, width=35, height=500,bg='#789e9e',font=('ariel', 14, 'bold'),
                                  text='Patient Details', relief=RIDGE)
        MemberName_F.pack(side=LEFT)

        Reciept_ButtonFrame = LabelFrame(MemberDetailsFrame, bd=8, width=1000, height=400, relief=RIDGE,bg='#789e9e')
        Reciept_ButtonFrame.pack(side=RIGHT)

        #=====================patient detail frame=================================
        self.lblReferenceNo = Label(MemberName_F, text="Reference No", bg='#789e9e',font=('ariel', 12, 'bold'), bd=5)
        self.lblReferenceNo.grid(row=0, column=0, sticky=W)
        self.txtReferenceNo = Entry(MemberName_F, font=('ariel', 12, 'bold'), bd=5, textvariable=self.ref,insertwidth=2)
        self.txtReferenceNo.grid(row=0, column=1)

        self.lblFirstname = Label(MemberName_F, text="Firstname",bg='#789e9e', font=('ariel', 12, 'bold'), bd=5)
        self.lblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname = Entry(MemberName_F, font=('ariel', 12, 'bold'), bd=5, textvariable=self.Firstname,
                                  insertwidth=2)
        self.txtFirstname.grid(row=1, column=1)

        self.lblLastname = Label(MemberName_F, text="Lastname", bg='#789e9e',font=('ariel', 12, 'bold'), bd=5)
        self.lblLastname.grid(row=2, column=0, sticky=W)
        self.txtLastname = Entry(MemberName_F, font=('ariel', 12, 'bold'), bd=5, textvariable=self.Lastname,
                                 insertwidth=2)
        self.txtLastname.grid(row=2, column=1)

        self.lblAddress = Label(MemberName_F, text="Address",bg='#789e9e', font=('ariel', 12, 'bold'), bd=5)
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(MemberName_F, font=('ariel', 12, 'bold'), bd=5, textvariable=self.Address,
                                insertwidth=2)
        self.txtAddress.grid(row=3, column=1)

        self.lblPostcode = Label(MemberName_F, text="Postcode",bg='#789e9e', font=('ariel', 12, 'bold'), bd=5)
        self.lblPostcode.grid(row=4, column=0, sticky=W)
        self.txtPostcode = Entry(MemberName_F, font=('ariel', 12, 'bold'), bd=5, textvariable=self.Postcode,
                                 insertwidth=2)
        self.txtPostcode.grid(row=4, column=1)

        self.lblTelephone = Label(MemberName_F, text="Telephone", bg='#789e9e',font=('ariel', 12, 'bold'), bd=5)
        self.lblTelephone.grid(row=5, column=0, sticky=W)
        self.txtTelephone = Entry(MemberName_F, font=('ariel', 12, 'bold'), bd=5, textvariable=self.Telephone, insertwidth=2)
        self.txtTelephone.grid(row=5, column=1)

        self.lblDate = Label(MemberName_F, text="Date", bg='#789e9e',font=('ariel', 12, 'bold'), bd=5)
        self.lblDate.grid(row=6, column=0, sticky=W)
        self.txtDate = Entry(MemberName_F, font=('ariel', 12, 'bold'), bd=5, textvariable=self.Date,insertwidth=2)
        self.txtDate.grid(row=6, column=1)

        self.lblProve_of_ID = Label(MemberName_F, text="Prove of ID",bg='#789e9e', font=('ariel', 12, 'bold'), bd=5)
        self.lblProve_of_ID.grid(row=7, column=0, sticky=W)

        self.cboProve_of_ID = ttk.Combobox(MemberName_F,font=('ariel', 12, 'bold'), textvariable=self.IDtype,state='readonly', width=19)
        self.cboProve_of_ID['value'] = ('', 'Citizenship', 'Driving License', 'Passport', 'Student')
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7, column=1)

        self.lblType_of_member = Label(MemberName_F, text="Type of member",bg='#789e9e', font=('ariel', 12, 'bold'), bd=5)
        self.lblType_of_member.grid(row=8, column=0, sticky=W)

        self.cboType_of_member = ttk.Combobox(MemberName_F,font=('ariel', 12, 'bold'), textvariable=self.Member,
                                              state='readonly', width=19)
        self.cboType_of_member['value'] = ('', 'Full Member', 'Annual Membership', 'Pay after Discharge')
        self.cboType_of_member.current(0)
        self.cboType_of_member.grid(row=8, column=1)

        self.lblMethod_of_Payment = Label(MemberName_F, text="Method of Payment",bg='#789e9e', font=('ariel', 12, 'bold'), bd=3)
        self.lblMethod_of_Payment.grid(row=9, column=0, sticky=W)

        self.cboMethod_of_Payment = ttk.Combobox(MemberName_F, font=('ariel', 12, 'bold'), textvariable=self.Payment,
                                                 state='readonly', width=19)
        self.cboMethod_of_Payment['value'] = ('', 'Visa Card', 'Debit Card', 'Master Card', 'Cash')
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=9, column=1)

        self.chkPatientfees = Checkbutton(MemberName_F,bg='#789e9e', text="Patient Fees", variable=self.Patientfee, onvalue=1, offvalue=0,
                                          font=('ariel', 12, 'bold'), command=self.Patient_fees)
        self.chkPatientfees.grid(row=10, column=0, sticky=W)

        self.txtPatientfees = Entry(MemberName_F, font=('ariel', 14, 'bold'), bd=7, textvariable=self.Patientfees,
                                    insertwidth=2, state=DISABLED, justify=RIGHT)
        self.txtPatientfees.grid(row=10, column=1)

        #===============Button frame=====================================

        # self.txtReciept = Text(Reciept_ButtonFrame, width=112, height=22, font=('ariel', 10, 'bold'))
        # self.txtReciept.grid(row=1, column=0, columnspan=4)

        self.btnExit = Button(Reciept_ButtonFrame, padx=18, pady=10,font=('ariel', 10, 'bold'),width=15, text="Exit",bg='red',bd=3, command=self.iExit )
        self.btnExit.place(x=562,y=230)

        self.btnReset = Button(Reciept_ButtonFrame, padx=18, font=('ariel', 10, 'bold'), pady=10, width=24,text="Reset",bg='silver', bd=3)
        self.btnReset.place(x=300,y=230)

        self.btnReciept = Button(Reciept_ButtonFrame, padx=18, font=('ariel', 10, 'bold'), pady=10, width=13,text="Reciept",bg='silver',bd=3,command=self.Reciept)
        self.btnReciept.place(x=0,y=230)

        self.btnUpdate= Button(Reciept_ButtonFrame, padx=18, font=('ariel', 10, 'bold'), pady=10, width=13,bg='silver',bd=3,text="Update",command=self.update)
        self.btnUpdate.place(x=150,y=230)

        scroll_x = ttk.Scrollbar(Reciept_ButtonFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Reciept_ButtonFrame, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Reciept_ButtonFrame, column=("ref","fname","lname","address","postcode","telephone",'date',"proof","member","payment","fees"), xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)
        scroll_x.grid()
        scroll_y.grid()

        scroll_x = ttk.Scrollbar(Reciept_ButtonFrame,command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(Reciept_ButtonFrame,command=self.hospital_table.yview)

        self.hospital_table.heading('ref', text='Reference No')
        self.hospital_table.heading('fname', text='First Name')
        self.hospital_table.heading('lname', text='Last Name')
        self.hospital_table.heading('address', text='Address')
        self.hospital_table.heading('postcode', text='Post Code')
        self.hospital_table.heading('telephone', text='Telephone')
        self.hospital_table.heading('date', text='Date')
        self.hospital_table.heading('proof', text='Proof of ID')
        self.hospital_table.heading('member', text='Type of Member')
        self.hospital_table.heading('payment', text='Method of Payment')
        self.hospital_table.heading('fees', text='Patient Fees')


        self.hospital_table['show'] = 'headings'

        self.hospital_table.column('ref', width=100)
        self.hospital_table.column('fname', width=100)
        self.hospital_table.column('lname', width=100)
        self.hospital_table.column('address', width=100)
        self.hospital_table.column('postcode', width=100)
        self.hospital_table.column('telephone', width=100)
        self.hospital_table.column('date', width=100)
        self.hospital_table.column('proof', width=100)
        self.hospital_table.column('member', width=100)
        self.hospital_table.column('payment', width=100)
        self.hospital_table.column('fees', width=100)


        self.hospital_table.grid(row=0,column=0)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fatch_data()










    def Reciept(self):

        ref_no = self.txtReferenceNo.get()
        f_name = self.txtFirstname.get()
        l_name = self.txtLastname.get()
        add_ress = self.txtAddress.get()
        post_code= self.txtPostcode.get()
        tele_phone=self.txtTelephone.get()
        da_te=self.txtDate.get()
        proof_ofid=self.cboProve_of_ID.get()
        member_type=self.cboType_of_member.get()
        payment_method=self.cboMethod_of_Payment.get()
        patient_fees= self.txtPatientfees.get()

        if ref_no=="":
            messagebox.showerror("Error","Fill all the Data")

        else:
            u=model.user.Recipt(ref_no,f_name,l_name,add_ress,post_code,tele_phone,da_te,proof_ofid,member_type,payment_method,patient_fees)
            query= "insert into ashokpatient(ref,fname,lname,address,postcode,telephone,date,proof,member,payment,fees) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (u.get_referenceno(),u.get_firstname(),u.get_lastname(),u.get_address(),u.get_postcode(),u.get_telephone(),u.get_date(),u.get_proofofid(),u.get_memberoftype(),u.get_methodofpayment(),u.get_patientfees())
            db.insert(query,values)
            messagebox.showinfo("Success","User Registered")
            self.fatch_data()


    def fatch_data(self):
        query='select * from ashokpatient'
        rows=  db.select(query)
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)


    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content['values']
        self.ref.set(row[0])
        self.Firstname.set(row[1])
        self.Lastname.set(row[2])
        self.Address.set(row[3])
        self.Postcode.set(row[4])
        self.Telephone.set(row[5])
        self.Date.set(row[6])
        self.IDtype.set(row[7])
        self.Member.set(row[8])
        self.Payment.set(row[9])
        self.Patientfees.set(row[10])

    def update(self):

        ref_no = self.txtReferenceNo.get()
        f_name = self.txtFirstname.get()
        l_name = self.txtLastname.get()
        add_ress = self.txtAddress.get()
        post_code= self.txtPostcode.get()
        tele_phone=self.txtTelephone.get()
        da_te=self.txtDate.get()
        proof_ofid=self.cboProve_of_ID.get()
        member_type=self.cboType_of_member.get()
        payment_method=self.cboMethod_of_Payment.get()
        patient_fees= self.txtPatientfees.get()

        if ref_no=="":
            messagebox.showerror("Error","Fill all the Data")

        else:
            u=model.user.Recipt(f_name,l_name,add_ress,post_code,tele_phone,da_te,proof_ofid,member_type,payment_method,patient_fees,ref_no)
            query= "update ashokpatient set fname=%s,lname=%s,address=%s,postcode=%s,telephone=%s,date=%s,proof=%s,member=%s,payment=%s,fees=%s where ref=%s"
            values = (u.get_referenceno(),u.get_firstname(),u.get_lastname(),u.get_address(),u.get_postcode(),u.get_telephone(),u.get_date(),u.get_proofofid(),u.get_memberoftype(),u.get_methodofpayment(),u.get_patientfees())
            db.insert(query,values)
            messagebox.showinfo("Success","User Data Changed")
            self.fatch_data()




    def iExit(self):
        iExit =messagebox.askyesno("Patient Administration System", "Confirm if you want to exit")
        if iExit > 0:
            self.root.destroy()
            return

        self.Patient_table=ttk.Treeview(Button)



    def Patient_fees(self):
        if (self.Patientfee.get() == 1):
            self.txtPatientfees.configure(state=NORMAL)
            Item1 = float(500)
            self.Patientfees.set("Rs. " + str(Item1))

        elif (self.Patientfee.get() == 0):
            self.txtPatientfees.configure(state=DISABLED)
            self.Patientfees.set("0")




