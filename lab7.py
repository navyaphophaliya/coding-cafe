
# EXERCISE 1 & 2: Account Records
class AccountRecord:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.history = []


alice = AccountRecord("Alice", 1200)
bob = AccountRecord("Bob", 300)
charlie = AccountRecord("Charlie", 100)

# Transfer 250 from Alice to Bob
alice.balance -= 250
bob.balance += 250
alice.history.append(("sent", "Bob", 250))
bob.history.append(("received", "Alice", 250))

# Transfer 200 from Bob to Charlie
bob.balance -= 200
charlie.balance += 200
bob.history.append(("sent", "Charlie", 200))
charlie.history.append(("received", "Bob", 200))

# Attempt to transfer 500 from Charlie to Alice
if charlie.balance >= 500:
    charlie.balance -= 500
    alice.balance += 500
    charlie.history.append(("sent", "Alice", 500))
    alice.history.append(("received", "Charlie", 500))
else:
    print("Transfer rejected: insufficient balance.")

print("\nExercise 2:")
print("Alice:", alice.balance, alice.history)
print("Bob:", bob.balance, bob.history)
print("Charlie:", charlie.balance, charlie.history)

# EXERCISE 3 & 4: BankAccount Class

class BankAccount:
    def __init__(self, owner, opening_balance):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self.owner = owner
        self._balance = opening_balance
        self._history = []

    def get_balance(self):
        return self._balance

    def get_history(self):
        return self._history.copy()

    def transfer_to(self, recipient, amount):
        if amount <= 0:
            return "Transfer rejected: amount must be positive."

        if amount < 10:
            return "Transfer rejected: minimum amount is Rs 10."

        if recipient is self:
            return "Transfer rejected: choose another account."

        if amount > self._balance:
            return "Transfer rejected: insufficient balance."

        self._balance -= amount
        recipient._balance += amount

        self._history.append(("sent", recipient.owner, amount))
        recipient._history.append(("received", self.owner, amount))

        return f"Transferred Rs {amount} to {recipient.owner}."



# EXERCISE 5: Bank Account Transfers

alice = BankAccount("Alice", 1200)
bob = BankAccount("Bob", 300)
charlie = BankAccount("Charlie", 100)

print("\nExercise 5:")
print(alice.transfer_to(bob, 250))
print(bob.transfer_to(charlie, 200))
print(charlie.transfer_to(alice, 500))

print("Alice:", alice.get_balance())
print("Bob:", bob.get_balance())
print("Charlie:", charlie.get_balance())

print("Bob's history:", bob.get_history())


# EXERCISE 6: Meera and Kabir

meera = BankAccount("Meera", 800)
kabir = BankAccount("Kabir", 200)

print("\nExercise 6:")
print(meera.transfer_to(kabir, 150))
print(meera.transfer_to(kabir, 0))
print(meera.transfer_to(meera, 50))
print(kabir.transfer_to(meera, 500))
print(kabir.transfer_to(meera, 100))

print("Meera's balance:", meera.get_balance())
print("Kabir's balance:", kabir.get_balance())

print("Meera's history:", meera.get_history())
print("Kabir's history:", kabir.get_history())

# EXERCISE 7: Minimum Transfer

print("\nExercise 7:")
meera = BankAccount("Meera", 800)
kabir = BankAccount("Kabir", 200)

print(meera.transfer_to(kabir, 5))
print(meera.transfer_to(kabir, 10))

print("Meera:", meera.get_balance())
print("Kabir:", kabir.get_balance())


# EXERCISE 8: Coffee Machine

class CoffeeMachine:
    def __init__(self, water_ml):
        if water_ml < 0:
            raise ValueError("Water cannot be negative.")

        self._water_ml = water_ml

    def get_water(self):
        return self._water_ml

    def refill_water(self, amount):
        if amount <= 0:
            return False

        self._water_ml += amount
        return True

    def make_coffee(self):
        if self._water_ml < 100:
            return "Not enough water."

        print("Heating water...")
        print("Brewing coffee...")
        print("Pouring coffee...")

        self._water_ml -= 100

        return "Coffee ready!"


# EXERCISE 9: Coffee Machine Demo


print("\nExercise 9:")

machine = CoffeeMachine(150)

print(machine.make_coffee())
print("Remaining water:", machine.get_water())

print(machine.make_coffee())

machine.refill_water(200)

print("After refill:", machine.get_water())
print(machine.make_coffee())
print("Remaining water:", machine.get_water())
