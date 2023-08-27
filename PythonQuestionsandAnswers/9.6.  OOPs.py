#1. Implement a program that simulates a basic bank account using a bank account class.
class BankAccount:
    dict2 = {'account_number': 855532704}
    dict = {'email': '', 'phone_number':''}
    def __init__(self):
         self.balance=0
         self.loggedin=False
    # def openaccount(self):
    #         self.dict['email']=input('Enter your email id: ')
    #         self.dict['phone_number']=input('Enter your phone number:')
    #         print(self.dict)
    #         print('Account is successfully created.')


    #
    # def login(self):
    #         self.email=input('To login enter your mail id: ')
    #         self.phone_number=input('Enter phone number: ')
    #         if self.email == self.dict['email'] and self.phone_number == self.dict['phone_number']:
    #             print('login is successful.')
    #             self.loggedin=True
    #         else:
    #             print('Invalid credentials.')


    def deposit(self,amount):
        if self.loggedin:
            self.balance=self.balance+amount
            print('Total available balance is:',self.balance)

        else:
            print('Please login before deposit')



    def withdraw(self,draw):
      if self.loggedin:
            self.balance=self.balance-draw
            print(f'withdrawn amount is: {draw}')
            print('Remaining balance is:', self.balance)
      else:
            print('Please login before withdraw.')
#
#     def transfer(self,transfer_amount,target_account):
#                 if target_account==self.dict2['account_number']:
#                      self.balance=self.balance-transfer_amount
#                      print(f'transfered amount is: {transfer_amount}')
#                      print('Remaining balance is:', self.balance)
#                 else:
#                     print('Check account number.')
#
#
account1=BankAccount()
#print(account1.openaccount())
#print(account1.login())
print(account1.deposit(1000))
print(account1.withdraw(500))
# print(account1.transfer(200,855532704))











