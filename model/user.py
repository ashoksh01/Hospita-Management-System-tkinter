class User:
    def __init__(self,uname=None,passw=None,blood=None,gen=None):
        self.__username=uname
        self.__password=passw
        self.__bloodgroup=blood
        self.__gender=gen

    def set_username(self,uname):
        self.__username=uname

    def get_username(self):
         return self.__username

    def set_password(self,passw):
        self.__password=passw

    def get_password(self):
        return self.__password

    def set_bloodgroup(self,blood):
        self.__bloodgroup=blood

    def get_bloodgroup(self):
        return self.__bloodgroup

    def set_gender(self,gen):
        self.__gender=gen

    def get_gender(self):
        return self.__gender

class Recipt:
    def __init__(self, ref=None, fname=None, lname=None, address=None,postcode=None,telephone=None,date=None,proof=None,member=None,payment=None,fees=None):
        self.__referenceno = ref
        self.__firstname = fname
        self.__lastname = lname
        self.__address = address
        self.__postcode = postcode
        self.__telephone = telephone
        self.__date = date
        self.__proofofid = proof
        self.__memberoftype = member
        self.__methodofpayment = payment
        self.__patientfees = fees


    def set_referenceno(self,ref):
        self.__referenceno=ref

    def get_referenceno(self):
         return self.__referenceno

    def set_firstname(self, fname):
        self.__firstname = fname

    def get_firstname(self):
        return self.__firstname

    def set_lastname(self, lname):
        self.__lastname = lname

    def get_lastname(self):
        return self.__lastname

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_postcode(self, postcode):
        self.__postcode = postcode

    def get_postcode(self):
        return self.__postcode

    def set_telephone(self, telephone):
        self.__telephone =telephone

    def get_telephone(self):
        return self.__telephone

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def set_proofofid(self, proof):
        self.__proofofid = proof

    def get_proofofid(self):
        return self.__proofofid

    def set_memberoftype(self, member):
        self.__memberoftype = member

    def get_memberoftype(self):
        return self.__memberoftype

    def set_methodofpayment(self, payment):
        self.__methodofpayment= payment

    def get_methodofpayment(self):
        return self.__methodofpayment

    def set_patientfees(self, fees):
        self.__referenceno = fees

    def get_patientfees(self):
        return self.__patientfees


