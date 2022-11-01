# Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment.

class Budget():
    def __init__(self,name):
        self.name=name
        self.balance=0
        
        
    # Allows for depositing    
    def deposit(self,amount):
        self.balance=self.balance+amount
        
        result=("Successful Deposit\n")
        result+=(f"You have successfully deposited €{amount} to the {self.name} budget\n")
        result+=(f"Your new balance in the {self.name} budget is €{self.balance}")
        
        return result
        
    
    # Allows withdrawals    
    def withdraw(self, amount):
        # don't allow more to be taken out than the balance
        if self.balance < amount:
            print("Transaction Failed")
            print("Insufficient funds")
            
        else:
            self.balance=self.balance-amount
            
            result=("Successful Transaction\n")
            result+= (f"You have successfully withdrawn €{amount} from the {self.name} budget \n")
            result+= (f"Your new balance for the {self.name} budget is €{self.balance}")
    
            return result
    
    
    
    def get_balance(self):
        balance=(f"The current balance of the {self.name} budget is €{self.balance}")
        return balance
    
    def transfer(self, amount, category):
        if self.name==category.name:
            result=("Error")
            result+=("You can only transfer funds to another category")
            
            return result

        else:
            if self.balance<amount:
                print("Transaction Failed - Insufficient Funds")
            
            else:
                self.balance-=amount
                category.balance+=amount
                
                transaction_result=("Successful Transfer\n")
                transaction_result+=(f"You have successfully transferred €{amount} from the {self.name} budget to the {category.name} budget\n")
                transaction_result+=(f"The current balance for the {self.name} budget is €{self.balance}\n")
                transaction_result+=(f"The current balance for the {category.name} budget is €{category.balance}")

                return transaction_result
    
food=Budget("food")
clothes=Budget("clothes")
entertainment=Budget("entertainment")
        

# Test deposit
print(food.deposit(10000))
print("------------------"*3)
print(clothes.deposit(2500))
print("------------------"*3)
print(entertainment.deposit(3000))


# Test withdrawal
print("------------------"*3)
print(food.withdraw(900))
print("------------------"*3)
print(clothes.withdraw(500))
print("------------------"*3)

# Test transfer
print(food.transfer(2000, clothes))

# Test balance
print(food.get_balance())
print("------------------"*3)
print(clothes.get_balance())
print("------------------"*3)
print(entertainment.get_balance())
