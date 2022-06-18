class ATM(object):
    def __init__(self, accNo, pinNo, bal):
        self.accNo=accNo
        self.pinNo=pinNo
        self.bal=bal
    
    def balance(self, bal):
        print(self.bal)
    
    def checkDetails(self):
        print("10920283000")

JoeKujo= ATM(10920283000, 360, 7000)

print(JoeKujo.balance())

    