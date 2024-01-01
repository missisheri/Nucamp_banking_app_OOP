class User:
    """
    A class representing a user with a name, PIN, and password.

    Attributes:
        name (str): The user's name.
        pin (int): The user's PIN.
        password (str): The user's password.
    """

    def __init__(self, name: str, pin: int, password: str):
        """Initializes a new User object."""
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        """Change the user's name."""
        self.name = name

    def change_pin(self, pin):
        """Change the user's PIN."""
        self.pin = pin

    def change_password(self, password):
        """Change the user's password."""
        self.password = password


class BankUser(User):
    """
    A class representing a bank user that inherits from the User class and
    includes additional functionality for managing account balance.

    Attributes:
        balance (float): The user's account balance.
    """

    def __init__(self, name, pin, password):
        """Initializes a new BankUser object."""
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        """Display the user's account balance."""
        print(self.name, "has an account balance of:", self.balance)

    def withdraw(self, withdraw_amount: float) -> float:
        """Update account balance after a withdrawal."""
        if withdraw_amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= withdraw_amount
        return self.balance

    def deposit(self, deposit_amount: float) -> float:
        """Update account balance after a deposit."""
        self.balance += deposit_amount
        return self.balance

    def transfer_money(self, receiver, transfer_amount) -> bool:
        """
        Transfer money to another user's account.

        Args:
            receiver (BankUser): The recipient of the transfer.
            transfer_amount (float): The amount to transfer.

        Returns:
            bool: True if the transfer is successful, False otherwise.
        """
        print("\nYou are transferring $", transfer_amount, "to", receiver.name)
        print("Authentication required")
        user_pin = input("Enter your PIN: ")

        if int(user_pin) == self.pin:
            print("Transfer authorized\nTransferring $", transfer_amount, "to", receiver.name)
            receiver.deposit(transfer_amount)
            self.withdraw(transfer_amount)
            return True
        else:
            print("Invalid PIN. Transaction canceled")
            return False

    def request_money(self, sender, request_amount) -> bool:
        """
        Request money from another user.

        Args:
            sender (BankUser): The sender from whom money is requested.
            request_amount (float): The amount to request.

        Returns:
            bool: True if the request is successful, False otherwise.
        """
        print("\nYou are requesting $", request_amount, "from", sender.name)
        print("User authentication is required...")
        input_message = "Enter " + sender.name + "'s PIN:"
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

# Create instances of BankUser
bankuser1 = BankUser("Bob", 1234, "bobpassword")
bankuser2 = BankUser("Missi", 5678, "missipassword")

# Perform operations
bankuser2.deposit(5000)
bankuser2.show_balance()
bankuser1.show_balance()
bankuser2.transfer_money(bankuser1, 500)

bankuser2.show_balance()
bankuser1.show_balance()

bankuser2.request_money(bankuser1, 250)

bankuser2.show_balance()
bankuser1.show_balance()
