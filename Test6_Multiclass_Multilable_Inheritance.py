
# <-----------------Multilable Inheritance -------------->

# Parent Class
class Bank: 
    def transcation(self):
        print("Total transaction value")
    def account_opening(self):
        print("This will show you account open status")
    def deposite(self):
        print("This will show your deposited amount")

#Child Class
class HDFC_bank(Bank): # <--- Call partent class in Child class
    def hdfc_to_icici(self):
        print("This will show you all the transaction happend to ICICI through HDFC")

class ICICI(HDFC_bank):# <--- Call HDFC class here becasue need to add method contain of HDFC class 
    pass

# Create object of ICICI class
I = ICICI()
I.hdfc_to_icici()
I.deposite()
I.account_opening()
I.transcation()
