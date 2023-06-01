import unittest
import backend.DBconnect
import backend.searchsort
import  model
import model.user


class All_Test_Database(unittest.TestCase):
    def setUp(self):
        '''  set up the method for testing'''
        self.db=backend.DBconnect.DBConnect()
        self.a=backend.searchsort.searchBox()
        self.b=backend.searchsort.sorting()

    def test_fetch(self):
        '''
        it test the fetch value of database
        '''
        query='select * from ashokhospital'
        a = self.db.Fetch(query)
        print(a)
        self.assertEqual([('Covid-19 Vacacine', '2', '4', '4', '3', '3', 'No', '12-10-2020', '12-10-2021', 'Prabesh Aryal', 'A345', 'ktm', '10-10-2000', 'asd', 'A', 'A34', 'Everyday', '120/80 mmhg'), ('Covid-19 Vacacine', '23', '4', '4', '3', '3', 'No', '12-10-2020', '12-10-2021', 'Prabesh Aryal', 'A345', 'ktm', '10-10-2000', 'asd', 'A', 'A34', 'Everyday', '120/80 mmhg'), ('Entresto', 'A1', '4', '4', '3', '3', 'No', '12-10-2020', '12-10-2021', 'Prabesh Aryal', 'A345', 'ktm', '10-10-2000', 'asd', 'A', 'A34', 'Everyday', '120/80 mmhg')],a)

        self.db.Fetch(query)

    def test_searching(self):
            '''
            it test the searching value
            '''
            query = "select * from ashokhospital "
            a = self.db.Fetch(query)
            print(a)
            b = self.a.linear_search('Adderall', a)
            print(b)
            self.assertEqual(0, b)
    def test_sorting(self):
        '''
        it test the sorting of database fetch value
        '''
        query = "select * from  ashokhospital"
        a = (self.db.Fetch(query))
        b = self.b.insertion_sort(a,0)
        print(b)
        self.assertEqual(
            [('Covid-19 Vacacine', '2', '4', '4', '3', '3', 'No', '12-10-2020', '12-10-2021', 'Prabesh Aryal', 'A345',
              'ktm', '10-10-2000', 'asd', 'A', 'A34', 'Everyday', '120/80 mmhg'), (
             'Covid-19 Vacacine', '23', '4', '4', '3', '3', 'No', '12-10-2020', '12-10-2021', 'Prabesh Aryal', 'A345',
             'ktm', '10-10-2000', 'asd', 'A', 'A34', 'Everyday', '120/80 mmhg'), (
             'Entresto', 'A1', '4', '4', '3', '3', 'No', '12-10-2020', '12-10-2021', 'Prabesh Aryal', 'A345', 'ktm',
             '10-10-2000', 'asd', 'A', 'A34', 'Everyday', '120/80 mmhg')],b)
    def test_add(self):
        '''
        it test the add method of database
        '''
        query = "insert into  ashokhospital(nameoftablets,ref) values(%s,%s)"
        nooftablets= str(input('nameoftablets:'))
        ref = str(input("Enter the ref: "))
        values =(nooftablets,ref)
        a=self.db.insert(query,values)
        print(a)
        self.assertIsNot(False,a)


    def test_add1(self):
        '''
        it test the add method of database
        '''
        query = "insert into  ashokpatient(ref,fname) values(%s,%s)"
        ref = str(input('ref:'))
        f_name = str(input("Enter the fname: "))
        values =(ref,f_name)
        a=self.db.insert(query,values)
        print(a)
        self.assertIsNot(False,a)

    def test_update(self):
        '''
        it test the update function of database
        '''
        nameoftablets=str(input("Enter the nameoftablets: "))
        ref=str(input("Enter the ref: "))
        values=nameoftablets,ref
        query = "update ashokhospital set nameoftablets=%s where ref=%s"
        d=self.db.insert(query,values)
        if d:
            print('succese')
        else:
            return False
        self.assertEqual(True, d)

    def test_del(self):
        '''
        it test the delete value of database
        '''
        ref = str(input("Enter the ref: "))
        values=ref,
        query="delete from ashokhospital where ref=%s"
        b=self.db.insert(query,values)
        if b:
            print('Success')
        else:
            return False
        self.assertEqual(True,b)

    def test_del1(self):
        '''
        it test the delete value of database
        '''
        dose= str(input("Enter the dose: "))
        values=dose,
        query="delete from ashokhospital where dose=%s"
        b=self.db.insert(query,values)
        if b:
            print('Success')
        else:
            return False
        self.assertEqual(True,b)

    def test_set_Referenceno_ref(self):
        '''
        it test the set get method of patient
        '''
        q=model.user.Recipt()
        Referenceno=str(input("Enter the ref: "))
        q.set_referenceno(Referenceno)
        a=q.get_referenceno()
        print(a)
        self.assertEqual(Referenceno,a)
    def test_set_Username_User(self):
        '''
        it test the set get method of doctor
        '''
        q=model.user.User()
        username=str(input("Enter the username: "))
        q.set_username(username)
        a=q.get_username()
        print(a)
        self.assertEqual(username,a)




    def tearDown(self):
        '''
        this method runs with setup method
        '''
        del self.db
        del self.a
        del self.b

if __name__=="__main__":
    obj=All_Test_Database()