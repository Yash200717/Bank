class ATM():

    def __init__(self,ifc,account,bank,credit_or_debit):
        self.ifc = ifc
        self.account = account
        self.bank = bank
        self.credit_or_debit = credit_or_debit
        
        
    def specs(self):
        print(f'''Your {self.ifc} and {self.account}. \nBank name is{self.bank}. \nbalance {self.credit_or_debit}.''')
    
    def cost(self,price):
        print(f"{self.ifc} {self.account}")

pnb =  ATM("ifc = S19777","ac = 2002462","PNB bank","24,000")
pnb.specs()
pnb.cost('24,880')

