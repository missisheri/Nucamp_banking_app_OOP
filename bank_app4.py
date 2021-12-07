class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of:", self.balance)

    def withdraw(self, withdraw_amount):
        self.balance = self.balance - withdraw_amount
        return self.balance

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        return self.balance

    def transfer_money(self, receiver, transfer_amount):
        print("\nYou are transferring $" +
              str(transfer_amount), "to", receiver.name)
        print("Authentication required")
        user_pin = input("Enter your PIN: ")

        if int(user_pin) == self.pin:
            print("Transfer authorized\nTransferring $" +
                  str(transfer_amount), "to", receiver.name)
            receiver.deposit(transfer_amount)
            self.withdraw(transfer_amount)
            return True     # why return a Boolean?? In case we need it later, for another scenario
        else:
            print("Invalid PIN. Transaction canceled")
            return False

    def request_money(self, sender, request_amount):
        print("\nYou are requesting $" +
              str(request_amount), "from", sender.name)
        print("User authentication is required...")
        # created this var to include sender's name in input.
        input_message = "Enter " + sender.name + "'s PIN:"
        # you cannot have more than 1 argument in the function input
        sender_pin = input(input_message)
        if int(sender_pin) == sender.pin:
            self_password = input("Enter your password: ")
            if self_password == self.password:
                print("Request authorized")
                sender.withdraw(request_amount)
                self.deposit(request_amount)
                print(sender.name, "sent $", str(request_amount))
                return True  
            else:
                print("Invalid password. Transaction canceled")
                return False
        else:
            print("Invalid PIN. Transaction canceled")
            return False


bankuser1 = BankUser("Bob", 1234, "bobpassword")
bankuser2 = BankUser("Missi", 5678, "missipassword")
bankuser2.deposit(5000)
bankuser2.show_balance()
bankuser1.show_balance()
bankuser2.transfer_money(bankuser1, 500)

bankuser2.show_balance()
bankuser1.show_balance()

bankuser2.request_money(bankuser1, 250)

bankuser2.show_balance()
bankuser1.show_balance()

"""  Driver Code for change password, name, pin  """

""" 
user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)

user1.change_name("Bobby")
user1.change_pin(4321)
user1.change_password("newpassword")
print(user1.name, user1.pin, user1.password) 
"""
