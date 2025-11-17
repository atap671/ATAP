# 1
class Account:
    def __init__(self, balance=0):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
        
class SavingsAccount(Account):
    def __init__(self, balance=0, interest_rate=0.01):
        super().__init__(balance)
        self.interest_rate = interest_rate
        
    def calculate_interest(self):
        return self.balance * self.interest_rate

class CurrentAccount(Account):
    def __init__(self, balance=0, overdraft_limit=1000):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        return False

# Тестування наслідування
sa = SavingsAccount(100)
ca = CurrentAccount(100)
sa.deposit(50)
ca.withdraw(200)
print(sa.balance, ca.balance)

# 2
class Bird:
    def fly(self):
        return "Якась пташка летить."

class Sparrow(Bird):
    def fly(self):
        return "Горобець швидко пурхає."

class Penguin(Bird):
    def fly(self):
        # Пінгвіни не літають, тому метод перевизначається
        return "Пінгвін не літає, він плаває."

# Тестування поліморфізму
def test_fly(bird):
    print(bird.fly())

test_fly(Bird())
test_fly(Sparrow())
test_fly(Penguin())

# 3
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        # Метод повинен бути реалізований у класах-нащадках
        pass

class Car(Transport):
    def move(self):
        return "Автомобіль рухається по дорозі."

class Boat(Transport):
    def move(self):
        return "Човен пливе по воді."

# Тестування абстрактного класу
car = Car()
boat = Boat()
print(car.move())
print(boat.move())

# Спроба ініціалізувати абстрактний клас призведе до помилки
# transport = Transport()
