from tkinter import *
from tkinter import ttk
import time
import random
import datetime
from tkinter import messagebox
import mysql.connector
import backend.DBconnect
import backend.searchsort



class HospitalMain:
    def __init__(self,root):
        self.root=root
        self.root.title("SHRESTHA HOSPITAL")
        self.root.geometry("1540x800+0+0")
        lbltitle=Label(self.root,bd=8,relief=RIDGE,text="SHRESTHA HOSPITAL MANAGEMENT SYSTEM",fg='black',bg='sky blue',font=("times new roman",30,'bold'))
        lbltitle.pack(side=TOP,fill=X)

        self.db=backend.DBconnect.DBConnect()


        self.Nameoftablets= StringVar()
        self.ref = StringVar()
        self.NoOftablets= StringVar()
        self.Dose = StringVar()
        self.DailyDose = StringVar()
        self.Lot = StringVar()
        self.SideEffects = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.PatientName = StringVar()
        self.PatientID = StringVar()
        self.Address = StringVar()
        self.Dob = StringVar()
        self.Medication = StringVar()
        self.BloodGroup = StringVar()
        self.NhsNumber = StringVar()
        self.Storage= StringVar()
        self.Blood = StringVar()
        self.Search = StringVar()



    #========================Dataframe-----------------------
        DataFrame=Frame(self.root,bd=8,relief=RIDGE,bg='#b7d8d6')
        DataFrame.place(x=0,y=65,width=1280,height=375)

        DataFrameLeft=LabelFrame(DataFrame,bd=8,padx=20,relief=RIDGE,bg='#b7d8d6',font=('times new roman',12,'bold'),text='Patient Details')
        DataFrameLeft.place(x=0,y=1,width=910,height=350)


        DataFrameRight = LabelFrame(DataFrame, bd=8, padx=20, relief=RIDGE,bg='#b7d8d6', font=('times new roman', 12, 'bold'),text='Prescription')
        DataFrameRight.place(x=920, y=3, width=340, height=350)
    #=======================button frame================


        ButtonFrame=Frame(self.root,bd=10,relief=RIDGE,bg='#b7d8d6')
        ButtonFrame.place(x=0,y=440,width=1280,height=55)

    #======================Details frame================
        Detailsframe=Frame(self.root,bd=10,relief=RIDGE,bg='#b7d8d6')
        Detailsframe.place(x=0,y=500,width=1280,height=150)

    #====================== DataframeLeft================
        lblNameTablets=Label(DataFrameLeft,text='Name of Tablets',bg='#b7d8d6',fg='black',font=('arial',12,'bold'),padx=2,pady=6)
        lblNameTablets.grid(row=0,column=0,sticky='w')

        comNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,state='readonly',font=('arial',12,'bold'),width=31)
        comNameTablet['value']=('','Ativan','Covid-19 Vacacine','Acetaminophen','Adderall','Nice','Cancer','HIV AIDS','Cymbalta', 'Doxycycline', 'Dupixent', 'Entresto','Farxiga','Gabapentin','Gilenya','Humira',
                                'Imbruvica', 'Xanax','Otezla', 'Viagra', 'Naproxen','Metoprolol','Rybelsus','Metformin','Januvia', 'Jardiance', 'Kevzara','Entyvio',
                                'Cortaid', 'Gaviscon', 'Lotrimin AF', 'Maalox Antacid', 'Midol', 'Motrin IB', 'Orajel', 'Rolaids', 'Tagamet HB', 'Tylenol', 'Zantac')
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=('arial',12,'bold'),text='Reference No',bg='#b7d8d6',fg='black',padx=2)
        lblref.grid(row=1,column=0,sticky='w')
        txtref=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=self.ref,width=33)
        txtref.grid(row=1,column=1)

        lblNoOftablets = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='No of Tablets',bg='#b7d8d6',fg='black', padx=2,pady=4)
        lblNoOftablets.grid(row=2, column=0, sticky='w')
        txtNoOftablets = Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.NoOftablets, width=33)
        txtNoOftablets.grid(row=2, column=1)

        lblDose = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Dose',bg='#b7d8d6',fg='black', padx=2,pady=6)
        lblDose.grid(row=3, column=0, sticky='w')
        txtDose = Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.Dose, width=33)
        txtDose.grid(row=3, column=1)

        lblDailyDose = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Daily Dose',bg='#b7d8d6',fg='black', padx=2,pady=6)
        lblDailyDose.grid(row=4, column=0, sticky='w')
        txtDailyDose = Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.DailyDose, width=33)
        txtDailyDose.grid(row=4, column=1)

        lblLot = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='No of Lot', bg='#b7d8d6',fg='black',padx=2,pady=6)
        lblLot.grid(row=5, column=0, sticky='w')
        txtLot = Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.Lot, width=33)
        txtLot.grid(row=5, column=1)

        lblSideEffects = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Side Effects', bg='#b7d8d6',fg='black',padx=2,pady=6)
        lblSideEffects.grid(row=6, column=0, sticky='w')
        txtSideEffects= Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.SideEffects, width=33)
        txtSideEffects.grid(row=6, column=1)

        lblIssueDate = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Issue Date', bg='#b7d8d6',fg='black',padx=2,pady=6)
        lblIssueDate.grid(row=7, column=0, sticky='w')
        txtIssueDate= Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.IssueDate, width=33)
        txtIssueDate.grid(row=7, column=1)

        lblExpDate = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Expiry Date',bg='#b7d8d6',fg='black', padx=2, pady=6)
        lblExpDate.grid(row=8, column=0, sticky='w')
        txtExpDate = Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=self.ExpDate, width=33)
        txtExpDate.grid(row=8, column=1)

        lblPatientName = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Patient Name', bg='#b7d8d6',fg='black',padx=2)
        lblPatientName.grid(row=0, column=2, sticky='w')
        txtPatientName = Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.PatientName, width=33)
        txtPatientName.grid(row=0, column=3)

        lblPatientID = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Patient ID',bg='#b7d8d6',fg='black', padx=2, pady=6)
        lblPatientID.grid(row=1, column=2, sticky='w')
        txtPatientID = Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.PatientID, width=33)
        txtPatientID.grid(row=1, column=3)

        lblAddress = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Address', bg='#b7d8d6',fg='black',padx=2, pady=6)
        lblAddress.grid(row=2, column=2, sticky='w')
        txtAddress = Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.Address, width=33)
        txtAddress.grid(row=2, column=3)

        lblDob = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='  DOB',bg='#b7d8d6',fg='black', padx=2, pady=6)
        lblDob.grid(row=3, column=2, sticky='w')
        txtDob = Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.Dob, width=33)
        txtDob.grid(row=3, column=3)

        lblMedication = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Medication', bg='#b7d8d6',fg='black',padx=2, pady=6)
        lblMedication.grid(row=4 ,column=2, sticky='w')
        txtMedication = Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.Medication, width=33)
        txtMedication.grid(row=4, column=3)

        lblBloodGroup = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Blood Group', bg='#b7d8d6',fg='black',padx=2, pady=6)
        lblBloodGroup.grid(row=5, column=2, sticky='w')
        txtBloodGroup = Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.BloodGroup, width=33)
        txtBloodGroup.grid(row=5, column=3)

        lblNhsNumber= Label(DataFrameLeft, font=('arial', 12, 'bold'), text='NHS Number', bg='#b7d8d6',fg='black',padx=2, pady=6)
        lblNhsNumber.grid(row=6, column=2, sticky='w')
        txtNhsNumber = Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.NhsNumber, width=33)
        txtNhsNumber.grid(row=6, column=3)

        lblStorage = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Storage Advice',bg='#b7d8d6',fg='black', padx=2, pady=6)
        lblStorage.grid(row=7, column=2, sticky='w')
        txtStorage = Entry(DataFrameLeft, font=('arial', 12, 'bold'),textvariable=self.Storage, width=33)
        txtStorage.grid(row=7, column=3)

        lblBlood = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Blood Pressure', bg='#b7d8d6',fg='black',padx=2, pady=6)
        lblBlood.grid(row=8, column=2, sticky='w')
        txtBlood = Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=self.Blood, width=33)
        txtBlood.grid(row=8, column=3)


        #=====================DataFrameRight====================
        self.textPrescription=Text(DataFrameRight,font=('arial',12,'bold'),width=32,height=16,padx=0,pady=6)
        self.textPrescription.grid(row=0,column=0)

        #====================Buttons============================

        self.btnPrescription = Button(ButtonFrame,command=self.iPrescription, text='Prescription', font=('ariel', 12, 'bold'),bg='brown', width=15, bd=4)
        self.btnPrescription.grid(row=0, column=0)

        self.btnPrescriptionData = Button(ButtonFrame,command=self.iPrescriptionData, text='Prescription Data', font=('ariel', 12, 'bold'),bg='brown', width=20,bd=4)
        self.btnPrescriptionData.grid(row=0, column=1)

        self.btnUpdate = Button(ButtonFrame,command=self.update, text='Update', font=('ariel', 12, 'bold'), bg='brown', width=10, bd=4)
        self.btnUpdate.grid(row=0, column=2)

        self.btnDelete = Button(ButtonFrame,command=self.delete, text='Delete', font=('ariel', 12, 'bold'),bg='brown', width=10, bd=4)
        self.btnDelete.grid(row=0, column=3)

        self.btnReset = Button(ButtonFrame, text='Reset', font=('ariel', 12, 'bold'),bg='brown', width=10, bd=4,command=self.reset)
        self.btnReset.grid(row=0, column=4)

        self.btnSearch = Button(ButtonFrame, text='search', font=('ariel', 12, 'bold'), bg='brown',width=10, bd=4,command=self.searchData)
        self.btnSearch.grid(row=0, column=5)

        self.txtSearch = Entry(ButtonFrame, font=('arial', 15, 'bold'), textvariable=self.Search, width=12,bd=8)
        self.txtSearch.grid(row=0, column=6)

        self.btnExit = Button(ButtonFrame,command=self.iExit, text='Exit', font=('ariel', 12, 'bold'),bg='red', width=10, bd=4)
        self.btnExit.grid(row=0, column=9)

        self.btnSort = Button(ButtonFrame, command=self.sort,text='Sort', font=('ariel', 12, 'bold'), bg='brown',width=15, bd=4)
        self.btnSort.grid(row=0, column=8)

        #===================Scrollbar===================
        scroll_x=ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=('nameoftablets','ref','nooftablets','dose','dailydose','lot','sideeffects','issuedate','expdate','pname','pid',
                                                              'address','dob','medication','bloodgroup','nhsnumber','storage','blood'), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y.config = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading('nameoftablets',text='Name of Tablets')
        self.hospital_table.heading('ref', text='Reference No')
        self.hospital_table.heading('nooftablets', text='No of Tablets')
        self.hospital_table.heading('dose', text='Dose')
        self.hospital_table.heading('dailydose', text='Daily Dose')
        self.hospital_table.heading('lot', text='No of Lot')
        self.hospital_table.heading('sideeffects', text='Side Effects')
        self.hospital_table.heading('issuedate', text='Issue Date')
        self.hospital_table.heading('expdate', text='Expiry Date')
        self.hospital_table.heading('pname', text='Patient Name')
        self.hospital_table.heading('pid', text='Patient ID')
        self.hospital_table.heading('address', text='Address')
        self.hospital_table.heading('dob', text='DOB')
        self.hospital_table.heading('medication', text='Medication')
        self.hospital_table.heading('bloodgroup', text='Blood Group')
        self.hospital_table.heading('nhsnumber', text='NHS Number')
        self.hospital_table.heading('storage', text='Storage Advice')
        self.hospital_table.heading('blood', text='Blood Pressure')

        self.hospital_table['show']='headings'

        self.hospital_table.column('nameoftablets',width=100)
        self.hospital_table.column('ref', width=100)
        self.hospital_table.column('nooftablets', width=100)
        self.hospital_table.column('dose', width=100)
        self.hospital_table.column('dailydose', width=100)
        self.hospital_table.column('lot', width=100)
        self.hospital_table.column('sideeffects', width=100)
        self.hospital_table.column('expdate', width=100)
        self.hospital_table.column('issuedate', width=100)
        self.hospital_table.column('pname', width=100)
        self.hospital_table.column('pid', width=100)
        self.hospital_table.column('address', width=100)
        self.hospital_table.column('dob', width=100)
        self.hospital_table.column('medication', width=100)
        self.hospital_table.column('bloodgroup',width=100)
        self.hospital_table.column('nhsnumber', width=100)
        self.hospital_table.column('storage',width=100)
        self.hospital_table.column('blood', width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fatch_data()


        #===========================Functinality Declration=========
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror('Error','All information are required')
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Stha1234@@##',database='hospitalalgorithm')
            my_cursor=conn.cursor()
            values = (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.NoOftablets.get(),
                self.Dose.get(),
                self.DailyDose.get(),
                self.Lot.get(),
                self.SideEffects.get(),
                self.IssueDate.get(),
                self.ExpDate.get(),
                self.PatientName.get(),
                self.PatientID.get(),
                self.Address.get(),
                self.Dob.get(),
                self.Medication.get(),
                self.BloodGroup.get(),
                self.NhsNumber.get(),
                self.Storage.get(),
                self.Blood.get())
            my_cursor.execute('insert into ashokhospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',values)

            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo('Record Added ','All the record has been added successfully')
    def update(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Stha1234@@##',database='hospitalalgorithm')
        my_cursor = conn.cursor()

        query = "update ashokhospital set nameoftablets=%s,nooftablets=%s,dose=%s,dailydose=%s,lot=%s,sideeffects=%s,issuedate=%s,expdate=%s,pname=%s,pid=%s,address=%s,dob=%s,medication=%s,bloodgroup=%s,nhsnumber=%s,storage=%s,blood=%s where ref=%s "
        values = (
            self.Nameoftablets.get(),
            self.NoOftablets.get(),
            self.Dose.get(),
            self.DailyDose.get(),
            self.Lot.get(),
            self.SideEffects.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.PatientName.get(),
            self.PatientID.get(),
            self.Address.get(),
            self.Dob.get(),
            self.Medication.get(),
            self.BloodGroup.get(),
            self.NhsNumber.get(),
            self.Storage.get(),
            self.Blood.get(),
            self.ref.get(),
        )

        my_cursor.execute(query,values)
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo('Record Update ', 'Record has been update successfully')



    def fatch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Stha1234@@##', database='hospitalalgorithm')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from ashokhospital')
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content['values']
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.NoOftablets.set(row[2])
        self.Dose.set(row[3])
        self.DailyDose.set(row[4])
        self.Lot.set(row[5])
        self.SideEffects.set(row[6])
        self.IssueDate.set(row[7])
        self.ExpDate.set(row[8])
        self.PatientName.set(row[9])
        self.PatientID.set(row[10])
        self.Address.set(row[11])
        self.Dob.set(row[12])
        self.Medication.set(row[13])
        self.BloodGroup.set(row[14])
        self.NhsNumber.set(row[15])
        self.Storage.set(row[16])
        self.Blood.set(row[17])


    def iPrescription(self):
        self.textPrescription.insert(END,'Name of Tatblets: \t'+self.Nameoftablets.get() + '\n')
        self.textPrescription.insert(END, 'Reference: \t' + self.ref.get() + '\n')
        self.textPrescription.insert(END, 'No of Tablets: \t' + self.NoOftablets.get() + '\n')
        self.textPrescription.insert(END, 'Dose: \t' + self.Dose.get() + '\n')
        self.textPrescription.insert(END, 'Daily Dose: \t' + self.DailyDose.get() + '\n')
        self.textPrescription.insert(END, 'No of Lot: \t' + self.Lot.get() + '\n')
        self.textPrescription.insert(END, 'Side Effects: \t' + self.SideEffects.get() + '\n')
        self.textPrescription.insert(END, 'Issue Date: \t' + self.IssueDate.get() + '\n')
        self.textPrescription.insert(END, 'Expiry date: \t' + self.ExpDate.get() + '\n')
        self.textPrescription.insert(END, 'Patient Name: \t' + self.PatientName.get() + '\n')
        self.textPrescription.insert(END, 'Patient ID: \t' + self.PatientID.get() + '\n')
        self.textPrescription.insert(END, 'Address: \t' + self.Address.get() + '\n')
        self.textPrescription.insert(END, 'DOB: \t' + self.Dob.get() + '\n')
        self.textPrescription.insert(END, 'Medication: \t' + self.Medication.get() + '\n')
        self.textPrescription.insert(END, 'Blood Group: \t' + self.BloodGroup.get() + '\n')
        self.textPrescription.insert(END, 'Nhs Number: \t' + self.NhsNumber.get() + '\n')
        self.textPrescription.insert(END, 'Storage Advice: \t' + self.Storage.get() + '\n')
        self.textPrescription.insert(END, 'Blood Pressure: \t' + self.Blood.get() + '\n')


    def delete(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Stha1234@@##', database='hospitalalgorithm')
        my_cursor = conn.cursor()
        query="delete from ashokhospital where ref=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete","Data has been deleted")

    def reset(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.NoOftablets.set("")
        self.Dose.set("")
        self.DailyDose.set("")
        self.Lot.set("")
        self.SideEffects.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.PatientName.set("")
        self.PatientID.set("")
        self.Address.set("")
        self.Dob.set("")
        self.Medication.set("")
        self.BloodGroup.set("")
        self.NhsNumber.set("")
        self.Storage.set("")
        self.Blood.set("")
        self.textPrescription.delete("1.0",END)

    def searchData(self):
        query = "select * from ashokhospital"
        rows = self.db.Fetch(query)
        doSearch = self.Search.get()
        d = backend.searchsort.searchBox().linear_search(doSearch,rows)
        if d != False:
            self.hospital_table.delete(*self.hospital_table.get_children())
            self.hospital_table.insert("", END, values=rows[d])

    def sort(self):
        index=0
        query = "select * from ashokhospital"
        row = self.db.Fetch(query)
        try:
            sorted_record = backend.searchsort.sorting().insertion_sort(row, index)
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in sorted_record:
                self.hospital_table.insert("", END, values=i)
        except:
            messagebox.showerror("error", "error")



    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System", "Confirm if you want to exit")
        if iExit > 0:
            self.root.destroy()
            return




