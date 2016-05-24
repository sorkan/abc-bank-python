from abcbank.transaction import Transaction

CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2


class Account:
    def __init__(self, accountType):
        self.accountType = accountType
        self.transactions = []

    def deposit(self, amount):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(amount))

    def withdraw(self, amount):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            # check for withdrawal over available funds - overdraft
            if (self.sumTransactions() < amount):
               raise ValueError("amount greater than avail funds")
            else:
               self.transactions.append(Transaction(-amount))

    def transferFunds(self, Account_t, amount):
        """
          The account you are transferring to is Account_t 
          (ie: savings, checking,maxi-savings).  the self represents
          the account you are transferring from.  amount is
          how much is being transferred
        """
        try:
           self.withdraw(amount)       # call self's withdraw method
           Account_t.deposit(amount)   # call the destination account deposit
        except ValueError as err:
           raise ValueError("transfer exception: "+err[0])


    def interestEarned(self):
        amount = self.sumTransactions()
        if self.accountType == SAVINGS:
            if (amount <= 1000):
                return amount * 0.001
            else:
                return 1 + (amount - 1000) * 0.002
        if self.accountType == MAXI_SAVINGS:
            if (amount <= 1000):
                return amount * 0.02
            elif (amount <= 2000):
                return 20 + (amount - 1000) * 0.05
            else:
                return 70 + (amount - 2000) * 0.1
        else:
            return amount * 0.001

    def sumTransactions(self, checkAllTransactions=True):
        return sum([t.amount for t in self.transactions])
