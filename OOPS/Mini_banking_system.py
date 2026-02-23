# Mini Banking System using OOP
# Feature set: create account + deposit + withdraw + transfer (via Bank)

class Logger:
    def log(self, msg: str) -> None:
        # Simple reusable component (COMPOSITION will use this)
        print(f"[LOG] {msg}")


class BankAccount:
    def __init__(self, owner: str, opening_balance: float = 0.0):
        # Class + object: this setas up object state
        self.owner = owner

        # ENCAPSULATION:
        # __balance is private using name mangling.
        # People should not directly modify balance from outside.
        self.__balance = float(opening_balance)

    def deposit(self, amount: float) -> None:
        # ABSTRACTION:
        # Caller uses deposit(amount) without caring how balance is stored.
        if amount <= 0:
            raise ValueError("Deposit must be positive.")

        # ENCAPSULATION:
        # Only this method can update balance safely.
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        # ABSTRACTION:
        # Caller uses withdraw(amount) without caring about internal checks.
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")

        # ENCAPSULATION:
        # Controlled update again
        self.__balance -= amount

    def get_balance(self) -> float:
        # ENCAPSULATION:
        # Controlled read access to private data
        return self.__balance


class Bank:
    def __init__(self, logger: Logger):
        # COMPOSITION:
        # Bank HAS a Logger (dependency injected so it can be replaced later)
        self._logger = logger

        # COMPOSITION:
        # Bank HAS many accounts stored in a dict
        self._accounts: dict[str, BankAccount] = {}

    def open_account(self, owner: str, opening_balance: float = 0.0) -> BankAccount:
        # ABSTRACTION:
        # Instead of creating accounts everywhere, Bank provides a clean API.
        if owner in self._accounts:
            raise ValueError("Account already exists. Please log in.")

        acc = BankAccount(owner, opening_balance)
        self._accounts[owner] = acc

        self._logger.log(f"Opened account for {owner} with £{opening_balance:.2f}")
        return acc

    def get_account(self, owner: str) -> BankAccount:
        if owner not in self._accounts:
            raise ValueError("Account does not exist.")
        return self._accounts[owner]

    def transfer(self, from_owner: str, to_owner: str, amount: float) -> None:
        # ABSTRACTION:
        # transfer() hides the multi step process: locate accounts, withdraw, deposit, log.
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than 0.")

        sender = self.get_account(from_owner)
        receiver = self.get_account(to_owner)

        # ENCAPSULATION:
        # Bank cannot access sender.__balance directly.
        # It must use public methods withdraw() and deposit().
        sender.withdraw(amount)
        receiver.deposit(amount)

        self._logger.log(f"Transferred £{amount:.2f} from {from_owner} to {to_owner}")


# -------- Demo --------
logger = Logger()
bank = Bank(logger)

asif_acc = bank.open_account("Asif", 200)
sara_acc = bank.open_account("Sara", 50)

bank.transfer("Asif", "Sara", 30)

print("Asif balance:", asif_acc.get_balance())
print("Sara balance:", sara_acc.get_balance())
