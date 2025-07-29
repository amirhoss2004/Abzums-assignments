import cowsay
from datetime import datetime as dt
today=dt.now()
class BankAccount:

    bank_name="first national bank"
    

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.initial_balance=float(initial_balance)
        self.account_holder=account_holder
        self.transaction:list =transaction
        self.balance=0.0
        self.balance+=self.initial_balance
    
            
            
    
    def deposite(self, amount:float):
        if amount>0:
            self.balance+=amount
            print(f"\t💲+{amount}$ to {self.account_holder}'s account succecfully deposited!✔")
            self.transaction.append(f"+{amount} deposite at {today}")

        else:
            print("\tno valid deposite amaount")
    
    def withdraw(self , amount:float):
        if amount <=self.balance:
            self.balance-=amount
            print(f"\t💲-{amount}$ from {self.account_holder}'s account succecfully transferd!✔")
            self.transaction.append(f"-{amount} withdraw at {today}")
        else:
            print("\t❌invalid withdrawal emount! ")




    def show_transactions(self) -> None:
        print(f"{BankAccount.bank_name} transactions:")
        print(self.transaction)

        

    @classmethod
    def change_bank_name(cls, new_name: str) -> None:
        cls.bank_name=new_name

    
    @staticmethod
    def validate_amount(amount: float) -> bool:
        if amount >0:
            True
        elif amount<0:
            False
        else:
            None
        pass

    def __str__(self) -> str:
        print(f"""
                 ||
                 ||
               \\||//
        ________\\//__________________________________________________________
        
        account Holeder: {self.account_holder} | total balance: {self.balance}  | initial balance: {self.initial_balance}
        
        I didnt understand what validate_amount actually do?

        _______________________________________________________________________
        -----------------------------------------------------------------------

        """)
    
    
   
class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, initial_balance: float = 0.0, interest_rate: float = 0.01):
        super().__init__( account_holder , initial_balance)
        self.interst_rate=interest_rate

    def add_interest(self) -> None:
        self.balance=self.balance*self.interst_rate+self.balance
        
    
    def __str__(self) -> str:
        print(f"""
                 ||
                 ||
               \\||//
        ________\\//__________________________________________________________
        
        saving account:
        account holder: {self.account_holder} | current balance; {self.balance} |  current interest rate: {self.interst_rate}
        ______________________________________________________________________
        ----------------------------------------------------------------------
        
    """)
    
        
transaction=[]

my_bank=r"""
\_ |          
  \_\      _______________________________
    \\    /   _________________________   \
      \  /   |                         |   \
        /    |          BANK           |    \ 
      _|     |__ ____ _________ ____ __|     |_  
    _|_________________________________________|_
    |___________________________________________|
      \---/    |                     |    \---/           
       |||     |                     |     |||                  
       | |     |       _______       |     | |
       |||     |      /___ ___\      |     |||  
       | |     |      |   |   |      |     | |  
     _ |||     |      | . | . |      |     ||| _ 
    //----------______|___|___|______----------\\
   // -   -  -_|_____________________|_ -  -  - \\   
  //  -  ____|_________________________|____  -  \\
 //   - |___________________________________| -   \\ 




"""

cowsay.draw(f"hello and welcom to {BankAccount.bank_name}" , my_bank)

# accounts
user1=BankAccount("mamad", 2.1)

user2=BankAccount("ALice", 30.00)


user1.deposite(30)
user1.deposite(10)
user1.withdraw(20)
user1.__str__()

BankAccount.change_bank_name("new horizens bank")

# SavingsAccount
user3=SavingsAccount("Charlie",50.0 ,0.05 )

user3.deposite(1000)
user3.add_interest()
user3.__str__()
#transactions
user1.show_transactions()

cowsay.draw(f"""Thanks for choosing our service
                   -from {BankAccount.bank_name}""", my_bank)
