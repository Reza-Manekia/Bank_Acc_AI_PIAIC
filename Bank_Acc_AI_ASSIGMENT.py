#!/usr/bin/env python
# coding: utf-8

# # Bank_Account:

# In[4]:


class Bank_Acc:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def check_balance(self):
        print(f"your current balance is:{self.balance}")
        
    def withdraw(self):
        withdraw = int(input("Enter Amount you want to withdraw: "))
        if withdraw > self.balance:
           print("Sorry! You have insufficient balance")
        else:
            self.balance = self.balance - withdraw
            print("Your amount of ", str(withdraw) , " withdraw succesfully")
            print("your current balance is: " , str(self.balance))
            
    def deposit(self):
        deposit = int(input("Enter amount you want to deposit: "))
        self.balance = self.balance + deposit
        print("Your amount of ", str(deposit) , " deposited succesfully")
        print("your current balance is: " , str(self.balance))
        
        
    
title = input("Enter your title name: ")
Acc1 = Bank_Acc(title)

while True:
    print("\nEnter 1 for check your current balance:\nEnter 2 for withdraw:\nEnter 3 for deposit:\nEnter 4 for quit\n")
    mode = int(input())
    if mode == 1:
        Acc1.check_balance()
    if mode == 2:
        Acc1.withdraw()
    if mode == 3:
        Acc1.deposit()
    if mode == 4:
        print("Thanks ", title , " for using our services")
        break


# In[ ]:




