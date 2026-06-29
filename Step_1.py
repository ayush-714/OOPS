"""
OOPS Learning Repository Builder - Directory & Code Files
Generates the complete folder structure and all Python code examples.
"""
import os
import textwrap

BASE = "/Users/ayussh-blrm24/Desktop/Code/Dev-Tools/New/OOPS"

DIRS = [
    "01_Introduction/code_examples",
    "02_Classes_and_Objects/code_examples",
    "03_Constructors/code_examples",
    "04_Instance_and_Class_Variables/code_examples",
    "05_Methods/code_examples",
    "06_Encapsulation/code_examples",
    "07_Abstraction/code_examples",
    "08_Inheritance/code_examples",
    "09_Polymorphism/code_examples",
    "10_Special_Methods/code_examples",
    "11_Property_and_Descriptors/code_examples",
    "12_Static_and_Class_Methods/code_examples",
    "13_Composition_and_Aggregation/code_examples",
    "14_Multiple_Inheritance/code_examples",
    "15_Method_Resolution_Order/code_examples",
    "16_Abstract_Base_Classes/code_examples",
    "17_Data_Classes/code_examples",
    "18_Type_Hints/code_examples",
    "19_Design_Principles/code_examples",
    "20_Design_Patterns/code_examples",
    "21_Real_World_Projects/Project_1_Library",
    "21_Real_World_Projects/Project_2_Bank",
    "21_Real_World_Projects/Project_3_Hospital",
    "22_Interview_Preparation/code_examples",
    "23_Practice/Beginner",
    "23_Practice/Intermediate",
    "23_Practice/Advanced",
]

def make_dirs():
    for d in DIRS:
        os.makedirs(os.path.join(BASE, d), exist_ok=True)
    print("✅ All directories created.")

# ─────────────────────────────────────────────
#  CODE FILES CONTENT
# ─────────────────────────────────────────────

CODE_FILES = {}

# ── 01 Introduction ──────────────────────────
CODE_FILES["01_Introduction/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Introduction to OOP: Procedural vs Object-Oriented
Topic: What is OOP? Why use it?
"""

# ─── PROCEDURAL APPROACH ─────────────────────────────────────────────────────
print("=" * 60)
print("PROCEDURAL APPROACH")
print("=" * 60)

# Data and functions are separate
student_name = "Alice"
student_age  = 20
student_grade = "A"

def display_student(name, age, grade):
    """Display student info - data passed as arguments."""
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

def promote_student(grade):
    """Promote student to next grade."""
    grades = ["F", "D", "C", "B", "A"]
    idx = grades.index(grade)
    return grades[min(idx + 1, len(grades) - 1)]

display_student(student_name, student_age, student_grade)
new_grade = promote_student(student_grade)
print(f"After promotion: {new_grade}")

# Problem: data and functions are loosely coupled — hard to scale!

# ─── OOP APPROACH ────────────────────────────────────────────────────────────
print()
print("=" * 60)
print("OBJECT-ORIENTED APPROACH")
print("=" * 60)

class Student:
    """
    A class that bundles data (attributes) and behaviour (methods) together.

    Real-world analogy: A Student ID card — it carries all info about
    one student and the rules for updating that info.
    """

    # Class definition starts with 'class' keyword
    # __init__ is the constructor (runs when object is created)

    def __init__(self, name: str, age: int, grade: str) -> None:
        self.name  = name   # instance attribute
        self.age   = age
        self.grade = grade

    def display(self) -> None:
        """Display student info."""
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def promote(self) -> None:
        """Promote student to next letter grade."""
        grades = ["F", "D", "C", "B", "A"]
        idx = grades.index(self.grade)
        self.grade = grades[min(idx + 1, len(grades) - 1)]
        print(f"{self.name} promoted to grade: {self.grade}")


# Creating objects (instances)
alice = Student("Alice", 20, "B")
bob   = Student("Bob",   22, "C")

alice.display()
bob.display()

alice.promote()
alice.display()

# Each object is independent — modifying alice doesn't affect bob
bob.display()

# ─── KEY OOP CONCEPTS PREVIEW ────────────────────────────────────────────────
print()
print("=" * 60)
print("FOUR PILLARS OF OOP")
print("=" * 60)

pillar_map = {
    "Encapsulation" : "Bundling data + methods; hiding internal state",
    "Abstraction"   : "Exposing only what is necessary",
    "Inheritance"   : "Child class reuses parent class behaviour",
    "Polymorphism"  : "One interface, many implementations",
}

for pillar, desc in pillar_map.items():
    print(f"  {pillar:<16} → {desc}")

# ─── OUTPUT ──────────────────────────────────────────────────────────────────
# PROCEDURAL APPROACH
# Name: Alice, Age: 20, Grade: A
# After promotion: A
#
# OBJECT-ORIENTED APPROACH
# Name: Alice, Age: 20, Grade: B
# Name: Bob, Age: 22, Grade: C
# Alice promoted to grade: A
# Name: Alice, Age: 20, Grade: A
# Name: Bob, Age: 22, Grade: C
#
# FOUR PILLARS OF OOP
#   Encapsulation    → Bundling data + methods; hiding internal state
#   Abstraction      → Exposing only what is necessary
#   Inheritance      → Child class reuses parent class behaviour
#   Polymorphism     → One interface, many implementations
'''

CODE_FILES["01_Introduction/code_examples/02_intermediate.py"] = '''\
"""
02_intermediate.py - OOP vs Procedural: A deeper comparison
Topic: When OOP wins; class vs instance; identity vs equality
"""

# ─── OOP WINS: MANAGING MULTIPLE ENTITIES ────────────────────────────────────

class BankAccount:
    """Simple bank account — shows how OOP scales cleanly."""

    bank_name = "PyBank"  # class variable shared by all accounts

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner   = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"[{self.owner}] Deposited ₹{amount:,.2f} → Balance: ₹{self.balance:,.2f}")

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"[{self.owner}] Withdrew ₹{amount:,.2f} → Balance: ₹{self.balance:,.2f}")

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"


acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob",   500)

acc1.deposit(200)
acc2.withdraw(100)

print(acc1)
print(acc2)

# ─── IDENTITY vs EQUALITY ────────────────────────────────────────────────────
print()
a = BankAccount("Test", 100)
b = BankAccount("Test", 100)
c = a   # c points to the SAME object as a

print(f"a is b  → {a is b}")    # False — different objects in memory
print(f"a is c  → {a is c}")    # True  — same object
print(f"id(a)   → {id(a)}")
print(f"id(b)   → {id(b)}")
print(f"id(c)   → {id(c)}")

# ─── CLASS INTROSPECTION ─────────────────────────────────────────────────────
print()
print("Type of acc1        :", type(acc1))
print("Is BankAccount?     :", isinstance(acc1, BankAccount))
print("Class name          :", acc1.__class__.__name__)
print("Module              :", acc1.__class__.__module__)
print("Dict of instance    :", acc1.__dict__)
print("Shared bank_name    :", BankAccount.bank_name)
'''

CODE_FILES["01_Introduction/code_examples/03_real_world.py"] = '''\
"""
03_real_world.py - Real-world OOP: an e-commerce order system mini-example
"""
from datetime import datetime
from typing import List


class Product:
    """Represents a product in the store."""

    def __init__(self, product_id: str, name: str, price: float, stock: int) -> None:
        self.product_id = product_id
        self.name       = name
        self.price      = price
        self.stock      = stock

    def is_available(self, qty: int = 1) -> bool:
        return self.stock >= qty

    def reduce_stock(self, qty: int) -> None:
        if not self.is_available(qty):
            raise ValueError(f"Insufficient stock for {self.name}")
        self.stock -= qty

    def __repr__(self) -> str:
        return f"Product({self.name!r}, ₹{self.price}, stock={self.stock})"


class CartItem:
    """One line in the shopping cart."""

    def __init__(self, product: Product, quantity: int) -> None:
        self.product  = product
        self.quantity = quantity

    @property
    def subtotal(self) -> float:
        return self.product.price * self.quantity

    def __repr__(self) -> str:
        return f"CartItem({self.product.name!r} x{self.quantity} = ₹{self.subtotal})"


class ShoppingCart:
    """Manages a collection of CartItems."""

    def __init__(self, customer_name: str) -> None:
        self.customer_name = customer_name
        self._items: List[CartItem] = []

    def add(self, product: Product, qty: int = 1) -> None:
        if not product.is_available(qty):
            print(f"⚠  {product.name} not available in qty {qty}")
            return
        self._items.append(CartItem(product, qty))
        print(f"✔  Added {product.name} x{qty} to cart.")

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self._items)

    def checkout(self) -> "Order":
        for item in self._items:
            item.product.reduce_stock(item.quantity)
        order = Order(self.customer_name, list(self._items), self.total)
        self._items.clear()
        return order

    def __repr__(self) -> str:
        return f"ShoppingCart({self.customer_name!r}, items={len(self._items)}, total=₹{self.total})"


class Order:
    """Immutable record of a completed purchase."""

    _counter = 0

    def __init__(self, customer: str, items: List[CartItem], total: float) -> None:
        Order._counter += 1
        self.order_id  = f"ORD-{Order._counter:04d}"
        self.customer  = customer
        self.items     = items
        self.total     = total
        self.timestamp = datetime.now()

    def receipt(self) -> str:
        lines = [
            f"{'─' * 40}",
            f"  ORDER RECEIPT  |  {self.order_id}",
            f"  Customer: {self.customer}",
            f"  Date    : {self.timestamp.strftime('%Y-%m-%d %H:%M')}",
            f"{'─' * 40}",
        ]
        for item in self.items:
            lines.append(f"  {item.product.name:<20} x{item.quantity}  ₹{item.subtotal:>8.2f}")
        lines += [f"{'─' * 40}", f"  TOTAL:                        ₹{self.total:>8.2f}", f"{'─' * 40}"]
        return "\n".join(lines)


# ─── DEMO ────────────────────────────────────────────────────────────────────
laptop = Product("P001", "Laptop",     55000, 10)
mouse  = Product("P002", "Mouse",       800,  50)
bag    = Product("P003", "Laptop Bag", 1500,   5)

cart = ShoppingCart("Priya")
cart.add(laptop, 1)
cart.add(mouse,  2)
cart.add(bag,    1)

print(f"\nCart: {cart}")
order = cart.checkout()
print()
print(order.receipt())
print(f"\nRemaining laptop stock: {laptop.stock}")
'''

CODE_FILES["01_Introduction/code_examples/04_common_mistakes.py"] = '''\
"""
04_common_mistakes.py - Common OOP beginner mistakes
"""

# ─── MISTAKE 1: Forgetting 'self' ────────────────────────────────────────────
print("── Mistake 1: Missing self ──")

class BadCounter:
    def __init__(self):
        count = 0          # ❌ local variable, NOT an attribute!

    def increment(self):
        count += 1         # ❌ NameError at runtime

class GoodCounter:
    def __init__(self):
        self.count = 0     # ✅ instance attribute

    def increment(self):
        self.count += 1    # ✅

c = GoodCounter()
c.increment()
c.increment()
print(f"Count: {c.count}")  # 2

# ─── MISTAKE 2: Mutable default argument ─────────────────────────────────────
print("\\n── Mistake 2: Mutable class variable as shared state ──")

class BadTeam:
    members = []           # ❌ shared across ALL instances!

    def add(self, name):
        self.members.append(name)

t1 = BadTeam(); t1.add("Alice")
t2 = BadTeam(); t2.add("Bob")
print("t1.members:", t1.members)  # ['Alice', 'Bob'] — UNEXPECTED!
print("t2.members:", t2.members)  # ['Alice', 'Bob'] — same list!

class GoodTeam:
    def __init__(self):
        self.members = []  # ✅ each instance gets its own list

    def add(self, name):
        self.members.append(name)

t1 = GoodTeam(); t1.add("Alice")
t2 = GoodTeam(); t2.add("Bob")
print("t1.members:", t1.members)  # ['Alice']  ✅
print("t2.members:", t2.members)  # ['Bob']    ✅

# ─── MISTAKE 3: Not calling super().__init__ ─────────────────────────────────
print("\\n── Mistake 3: Missing super().__init__ ──")

class Animal:
    def __init__(self, name):
        self.name = name

class BadDog(Animal):
    def __init__(self, breed):
        # ❌ Forgot super().__init__ — self.name never set
        self.breed = breed

class GoodDog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # ✅
        self.breed = breed

dog = GoodDog("Rex", "Labrador")
print(f"Dog: {dog.name}, Breed: {dog.breed}")

# ─── MISTAKE 4: Overriding built-in names ────────────────────────────────────
print("\\n── Mistake 4: Shadowing built-ins ──")

# ❌ Never name attributes 'list', 'type', 'id', 'input', 'print', etc.
class BadClass:
    def __init__(self):
        self.list = [1, 2, 3]   # shadows the built-in list type
        self.id   = 42           # shadows the built-in id()

class GoodClass:
    def __init__(self):
        self.items    = [1, 2, 3]  # ✅ descriptive, no shadowing
        self.user_id  = 42          # ✅

print("Mistakes demonstrated and fixed ✅")
'''

CODE_FILES["01_Introduction/code_examples/05_best_practices.py"] = '''\
"""
05_best_practices.py - OOP Best Practices in Python
"""
from typing import Optional


# ─── BEST PRACTICE 1: Single Responsibility ──────────────────────────────────
class User:
    """Stores user data only. Does NOT handle saving, emailing, etc."""
    def __init__(self, name: str, email: str) -> None:
        self.name  = name
        self.email = email

class UserRepository:
    """Handles persistence of User objects."""
    def save(self, user: User) -> None:
        print(f"[DB] Saving user: {user.name}")

class EmailService:
    """Handles email notifications."""
    def send_welcome(self, user: User) -> None:
        print(f"[Email] Sending welcome to {user.email}")

user = User("Alice", "alice@example.com")
repo = UserRepository()
svc  = EmailService()
repo.save(user)
svc.send_welcome(user)


# ─── BEST PRACTICE 2: Use __repr__ and __str__ ───────────────────────────────
class Point:
    """Represent a 2D point."""
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """For debugging — unambiguous."""
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        """For end-users — readable."""
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))   # Point(x=3, y=4)
print(str(p))    # (3, 4)


# ─── BEST PRACTICE 3: Type hints everywhere ──────────────────────────────────
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width  = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    @classmethod
    def square(cls, side: float) -> "Rectangle":
        """Factory method for creating a square."""
        return cls(side, side)

r = Rectangle(4, 6)
print(f"Area: {r.area()}, Perimeter: {r.perimeter()}")

sq = Rectangle.square(5)
print(f"Square area: {sq.area()}")


# ─── BEST PRACTICE 4: Guard against bad input ────────────────────────────────
class Temperature:
    """Temperature in Celsius with validation."""
    ABSOLUTE_ZERO = -273.15

    def __init__(self, celsius: float) -> None:
        self.celsius = celsius  # uses the property setter below

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < self.ABSOLUTE_ZERO:
            raise ValueError(f"Temperature {value}°C is below absolute zero.")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

t = Temperature(100)
print(f"{t.celsius}°C = {t.fahrenheit}°F")

try:
    bad = Temperature(-300)
except ValueError as e:
    print(f"Caught: {e}")

print("\\nAll best practices demonstrated ✅")
'''

# ── 02 Classes and Objects ───────────────────
CODE_FILES["02_Classes_and_Objects/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Classes and Objects: fundamentals
"""

# ─── DEFINING A CLASS ────────────────────────────────────────────────────────
class Dog:
    """
    Represents a dog.

    Class body contains:
      - Class variables  (shared by all instances)
      - Instance methods (behaviour)
      - The constructor  (__init__)
    """

    species = "Canis lupus familiaris"   # class variable

    def __init__(self, name: str, breed: str, age: int) -> None:
        # instance variables — unique per object
        self.name  = name
        self.breed = breed
        self.age   = age

    def bark(self) -> str:
        return f"{self.name} says: Woof!"

    def birthday(self) -> None:
        self.age += 1
        print(f"Happy birthday {self.name}! Now {self.age} years old.")

    def __str__(self) -> str:
        return f"Dog(name={self.name!r}, breed={self.breed!r}, age={self.age})"


# ─── CREATING OBJECTS ────────────────────────────────────────────────────────
rex   = Dog("Rex",   "German Shepherd", 3)
buddy = Dog("Buddy", "Golden Retriever", 5)

print(rex)
print(buddy)
print(rex.bark())
print(buddy.bark())

rex.birthday()

# Accessing class variable through instance and through class
print(rex.species)
print(Dog.species)

# ─── MEMORY MODEL ────────────────────────────────────────────────────────────
print()
print("rex   id:", id(rex))
print("buddy id:", id(buddy))
print("Same object?", rex is buddy)      # False

# Each instance has its own __dict__
print("rex.__dict__  :", rex.__dict__)
print("buddy.__dict__:", buddy.__dict__)

# Class-level dict (does NOT include instance vars)
print("Dog.__dict__ keys:", list(Dog.__dict__.keys()))
'''

CODE_FILES["02_Classes_and_Objects/code_examples/02_intermediate.py"] = '''\
"""
02_intermediate.py - Multiple classes working together
"""
from typing import List, Optional
from datetime import date


class Author:
    def __init__(self, name: str, birth_year: int) -> None:
        self.name       = name
        self.birth_year = birth_year

    @property
    def age(self) -> int:
        return date.today().year - self.birth_year

    def __repr__(self) -> str:
        return f"Author({self.name!r})"


class Book:
    _total_books = 0

    def __init__(self, title: str, author: Author, year: int, pages: int) -> None:
        self.title  = title
        self.author = author
        self.year   = year
        self.pages  = pages
        Book._total_books += 1

    @classmethod
    def total_books(cls) -> int:
        return cls._total_books

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author.name} ({self.year})"

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r})"


class Library:
    def __init__(self, name: str) -> None:
        self.name  = name
        self._shelf: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._shelf.append(book)
        print(f"Added: {book}")

    def search(self, keyword: str) -> List[Book]:
        keyword = keyword.lower()
        return [b for b in self._shelf
                if keyword in b.title.lower() or keyword in b.author.name.lower()]

    def list_books(self) -> None:
        print(f"\\n{'─' * 40}")
        print(f"  {self.name} — {len(self._shelf)} books")
        print(f"{'─' * 40}")
        for i, book in enumerate(self._shelf, 1):
            print(f"  {i}. {book}")

    def __len__(self) -> int:
        return len(self._shelf)


# ─── DEMO ────────────────────────────────────────────────────────────────────
rowling   = Author("J.K. Rowling", 1965)
tolkien   = Author("J.R.R. Tolkien", 1892)
orwell    = Author("George Orwell", 1903)

books = [
    Book("Harry Potter and the Sorcerer\'s Stone", rowling,  1997, 309),
    Book("The Lord of the Rings",                   tolkien, 1954, 1178),
    Book("1984",                                    orwell,  1949, 328),
    Book("Animal Farm",                             orwell,  1945, 112),
    Book("Harry Potter and the Chamber of Secrets", rowling, 1998, 341),
]

lib = Library("City Central Library")
for b in books:
    lib.add_book(b)

lib.list_books()
print(f"\\nTotal books ever created: {Book.total_books()}")

results = lib.search("harry")
print(f"\\nSearch 'harry': {results}")

results = lib.search("orwell")
print(f"Search 'orwell': {results}")
'''

CODE_FILES["02_Classes_and_Objects/code_examples/03_real_world.py"] = '''\
"""
03_real_world.py - Employee Management mini-system
"""
from typing import List, Optional
from datetime import date, timedelta
import uuid


class Department:
    def __init__(self, name: str, budget: float) -> None:
        self.name   = name
        self.budget = budget
        self._employees: List["Employee"] = []

    def hire(self, emp: "Employee") -> None:
        emp.department = self
        self._employees.append(emp)
        print(f"✔ {emp.name} joined {self.name}")

    @property
    def headcount(self) -> int:
        return len(self._employees)

    @property
    def total_salary(self) -> float:
        return sum(e.salary for e in self._employees)

    def __repr__(self) -> str:
        return f"Department({self.name!r}, headcount={self.headcount})"


class Employee:
    def __init__(self, name: str, role: str, salary: float) -> None:
        self.emp_id     = str(uuid.uuid4())[:8].upper()
        self.name       = name
        self.role       = role
        self.salary     = salary
        self.join_date  = date.today()
        self.department: Optional[Department] = None

    def give_raise(self, percent: float) -> None:
        increase      = self.salary * percent / 100
        self.salary  += increase
        print(f"{self.name} salary raised by {percent}% → ₹{self.salary:,.2f}")

    def years_of_service(self) -> float:
        delta = date.today() - self.join_date
        return round(delta.days / 365.25, 2)

    def __repr__(self) -> str:
        dept = self.department.name if self.department else "Unassigned"
        return (f"Employee(id={self.emp_id}, name={self.name!r}, "
                f"role={self.role!r}, dept={dept!r})")


# ─── DEMO ────────────────────────────────────────────────────────────────────
engineering = Department("Engineering", 5_000_000)
marketing   = Department("Marketing",   2_000_000)

e1 = Employee("Alice",   "Senior Engineer",    120_000)
e2 = Employee("Bob",     "Junior Engineer",     60_000)
e3 = Employee("Charlie", "Marketing Manager",   80_000)

engineering.hire(e1)
engineering.hire(e2)
marketing.hire(e3)

print()
e1.give_raise(15)
e2.give_raise(10)

print()
print(f"Engineering headcount   : {engineering.headcount}")
print(f"Engineering total salary: ₹{engineering.total_salary:,.2f}")
print(f"Marketing headcount     : {marketing.headcount}")

print()
print(repr(e1))
print(repr(e3))
'''

# ── 03 Constructors ──────────────────────────
CODE_FILES["03_Constructors/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Constructors: __init__ fundamentals
"""

# ─── DEFAULT CONSTRUCTOR ─────────────────────────────────────────────────────
class EmptyClass:
    """Python provides a default constructor if none is defined."""
    pass

obj = EmptyClass()
print("Default constructor:", obj)


# ─── CUSTOM __init__ ─────────────────────────────────────────────────────────
class Car:
    """Parameterized constructor."""

    def __init__(self, make: str, model: str, year: int, color: str = "White") -> None:
        """
        __init__ is called automatically after __new__ creates the object.
        'self' refers to the new instance.
        """
        self.make  = make
        self.model = model
        self.year  = year
        self.color = color
        self._mileage = 0.0    # private attribute, set internally

        print(f"  [__init__] Car created: {year} {make} {model}")

    def drive(self, km: float) -> None:
        self._mileage += km
        print(f"Drove {km} km. Total mileage: {self._mileage} km")

    def __repr__(self) -> str:
        return f"Car({self.year} {self.make} {self.model}, {self.color})"


print("\\n── Creating cars ──")
car1 = Car("Toyota", "Corolla", 2022)           # default color
car2 = Car("Honda",  "City",    2023, "Black")   # explicit color

print(car1)
print(car2)
car1.drive(120.5)


# ─── __new__ vs __init__ ─────────────────────────────────────────────────────
print("\\n── __new__ vs __init__ ──")

class Singleton:
    """Classic singleton using __new__."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("  [__new__]  Creating the single instance")
            cls._instance = super().__new__(cls)
        else:
            print("  [__new__]  Returning existing instance")
        return cls._instance

    def __init__(self):
        print("  [__init__] Initialising")


s1 = Singleton()
s2 = Singleton()
print(f"Same object? {s1 is s2}")   # True


# ─── CONSTRUCTOR WITH VALIDATION ─────────────────────────────────────────────
print("\\n── Constructor with validation ──")

class AgeValidator:
    def __init__(self, name: str, age: int) -> None:
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError(f"Invalid age: {age}")
        self.name = name
        self.age  = age
        print(f"Valid: {name}, age {age}")

AgeValidator("Alice", 25)

try:
    AgeValidator("Bob", -5)
except ValueError as e:
    print(f"Error: {e}")
'''

CODE_FILES["03_Constructors/code_examples/02_intermediate.py"] = '''\
"""
02_intermediate.py - Constructor overloading techniques in Python
(Python has no built-in overloading — we simulate it)
"""
from __future__ import annotations
from typing import Optional
from datetime import date


# ─── TECHNIQUE 1: Default parameter values ───────────────────────────────────
class Connection:
    def __init__(
        self,
        host: str    = "localhost",
        port: int    = 5432,
        db: str      = "mydb",
        ssl: bool    = False,
    ) -> None:
        self.host = host
        self.port = port
        self.db   = db
        self.ssl  = ssl

    def __repr__(self) -> str:
        return f"Connection({self.host}:{self.port}/{self.db}, ssl={self.ssl})"

c1 = Connection()                              # all defaults
c2 = Connection("prod.db.io", 5432, "prod")   # custom
c3 = Connection(ssl=True)                      # keyword only
print(c1, c2, c3, sep="\\n")


# ─── TECHNIQUE 2: Class / factory methods ────────────────────────────────────
class Employee:
    def __init__(self, name: str, salary: float, start_date: date) -> None:
        self.name       = name
        self.salary     = salary
        self.start_date = start_date

    @classmethod
    def from_dict(cls, data: dict) -> "Employee":
        return cls(data["name"], data["salary"],
                   date.fromisoformat(data["start_date"]))

    @classmethod
    def intern(cls, name: str) -> "Employee":
        """Factory: creates an intern with default salary."""
        return cls(name, 15_000, date.today())

    @classmethod
    def from_string(cls, s: str) -> "Employee":
        """Parse 'Name,Salary,YYYY-MM-DD'."""
        parts = s.split(",")
        return cls(parts[0], float(parts[1]), date.fromisoformat(parts[2]))

    def __repr__(self) -> str:
        return f"Employee({self.name!r}, ₹{self.salary:,}, {self.start_date})"

e1 = Employee("Alice", 80_000, date(2023, 1, 15))
e2 = Employee.from_dict({"name": "Bob", "salary": 70000, "start_date": "2024-03-01"})
e3 = Employee.intern("Charlie")
e4 = Employee.from_string("Diana,95000,2022-06-15")

print(e1, e2, e3, e4, sep="\\n")


# ─── TECHNIQUE 3: *args / **kwargs ───────────────────────────────────────────
class FlexPoint:
    """Accepts (x,y), (x,y,z) or keyword args."""
    def __init__(self, *args, **kwargs):
        if args:
            self.coords = args
        elif kwargs:
            self.coords = tuple(kwargs.values())
        else:
            self.coords = (0, 0)

    def __repr__(self) -> str:
        return f"FlexPoint{self.coords}"

print()
print(FlexPoint(1, 2))
print(FlexPoint(1, 2, 3))
print(FlexPoint(x=4, y=5))
print(FlexPoint())
'''

# ── 04 Variables ─────────────────────────────
CODE_FILES["04_Instance_and_Class_Variables/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Instance vs Class Variables
"""

# ─── CLASS VARIABLE (shared) vs INSTANCE VARIABLE (unique) ───────────────────

class Employee:
    # CLASS VARIABLES — defined at class level, shared across instances
    company     = "TechCorp Ltd"
    employee_count = 0

    def __init__(self, name: str, salary: float) -> None:
        # INSTANCE VARIABLES — unique to each object
        self.name   = name
        self.salary = salary
        Employee.employee_count += 1   # modify through class, NOT self

    def display(self) -> None:
        print(f"  Name: {self.name}, Salary: ₹{self.salary:,}, "
              f"Company: {self.company}, Total: {Employee.employee_count}")


e1 = Employee("Alice", 80_000)
e2 = Employee("Bob",   60_000)
e3 = Employee("Carol", 90_000)

e1.display()
e2.display()
e3.display()

print("\\n── Changing class variable ──")
Employee.company = "TechCorp Global"   # affects ALL instances
e1.display()                           # ✅ sees new value

print("\\n── Instance variable shadows class variable ──")
e2.company = "Freelancer"   # creates instance var that HIDES class var
e1.display()                # company = TechCorp Global (class)
e2.display()                # company = Freelancer      (instance shadow)

print("\\n── Checking __dict__ ──")
print("e1.__dict__:", e1.__dict__)
print("e2.__dict__:", e2.__dict__)   # contains 'company' key
print("Employee.__dict__[company]:", Employee.__dict__["company"])
print("Employee.__dict__[employee_count]:", Employee.__dict__["employee_count"])
'''

CODE_FILES["04_Instance_and_Class_Variables/code_examples/02_intermediate.py"] = '''\
"""
02_intermediate.py - Counters, constants, and variable scope
"""

class Circle:
    """Demonstrates class constant, instance var, and computed property."""

    PI = 3.141592653589793   # class-level constant (by convention, UPPER_CASE)
    _total_circles = 0

    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = radius
        Circle._total_circles += 1

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value

    @property
    def area(self) -> float:
        return Circle.PI * self._radius ** 2

    @property
    def circumference(self) -> float:
        return 2 * Circle.PI * self._radius

    @classmethod
    def total(cls) -> int:
        return cls._total_circles

    def __repr__(self) -> str:
        return f"Circle(r={self._radius}, area={self.area:.4f})"


c1 = Circle(5)
c2 = Circle(3)
c3 = Circle(7)

for c in (c1, c2, c3):
    print(c)

print(f"Total circles created: {Circle.total()}")

c1.radius = 10
print(f"After resize: {c1}")

try:
    Circle(-1)
except ValueError as e:
    print(f"Caught: {e}")


# ─── CLASS VAR AS REGISTRY ────────────────────────────────────────────────────
print()

class Plugin:
    """Auto-register subclasses via class variable."""
    _registry: dict = {}

    def __init_subclass__(cls, plugin_name: str, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin._registry[plugin_name] = cls

class CSVPlugin(Plugin, plugin_name="csv"):
    def process(self): return "Processing CSV"

class JSONPlugin(Plugin, plugin_name="json"):
    def process(self): return "Processing JSON"

class XMLPlugin(Plugin, plugin_name="xml"):
    def process(self): return "Processing XML"

print("Registered plugins:", Plugin._registry)
for name, cls in Plugin._registry.items():
    print(f"  {name}: {cls().process()}")
'''

# ── 05 Methods ───────────────────────────────
CODE_FILES["05_Methods/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Instance, Class, and Static Methods
"""

class MathHelper:
    """Demonstrates all three method types."""

    precision = 4   # class variable

    def __init__(self, value: float) -> None:
        self.value = value   # instance variable

    # ── INSTANCE METHOD: has access to instance (self) and class ──
    def square(self) -> float:
        """Uses self.value — instance method."""
        return round(self.value ** 2, self.precision)

    def cube(self) -> float:
        return round(self.value ** 3, self.precision)

    def display(self) -> None:
        print(f"Value: {self.value}, Square: {self.square()}, Cube: {self.cube()}")

    # ── CLASS METHOD: has access to class (cls), NOT instance ──
    @classmethod
    def set_precision(cls, p: int) -> None:
        """Changes class-level precision for ALL instances."""
        cls.precision = p
        print(f"Precision set to {p}")

    @classmethod
    def from_string(cls, s: str) -> "MathHelper":
        """Factory method — alternative constructor."""
        return cls(float(s))

    # ── STATIC METHOD: has NO access to class or instance ──
    @staticmethod
    def is_prime(n: int) -> bool:
        """Pure utility — no class or instance state needed."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def fibonacci(n: int) -> list:
        """Returns first n Fibonacci numbers."""
        fib = [0, 1]
        for _ in range(n - 2):
            fib.append(fib[-1] + fib[-2])
        return fib[:n]


# ─── DEMO ────────────────────────────────────────────────────────────────────
m = MathHelper(3.14159)
m.display()

MathHelper.set_precision(2)
m.display()                 # precision changed globally

m2 = MathHelper.from_string("7.5")
m2.display()

print()
for n in [2, 7, 15, 17, 100]:
    print(f"  {n} is prime: {MathHelper.is_prime(n)}")

print()
print("Fibonacci(10):", MathHelper.fibonacci(10))

# Static methods can be called on class OR instance
print("Called on instance:", m.is_prime(13))
print("Called on class   :", MathHelper.is_prime(13))
'''

# ── 06 Encapsulation ─────────────────────────
CODE_FILES["06_Encapsulation/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Encapsulation: Public, Protected, Private
"""

# ─── ACCESS MODIFIERS IN PYTHON ──────────────────────────────────────────────
# Python uses naming conventions (no true access enforcement):
#  public   → name         (accessible everywhere)
#  protected→ _name        (convention: don't access outside class/subclass)
#  private  → __name       (name-mangled to _ClassName__name)

class BankAccount:
    """Demonstrates all three access levels."""

    bank_name = "PyBank"   # public class variable

    def __init__(self, owner: str, initial_balance: float) -> None:
        self.owner       = owner           # public
        self._account_no = self._gen_no()  # protected
        self.__balance   = initial_balance # private (name-mangled)
        self.__pin       = "0000"          # private

    def _gen_no(self) -> str:
        """Protected helper method."""
        import random
        return f"AC{random.randint(100000, 999999)}"

    # ── Public interface ──────────────────────────────────────────────────────
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount
        print(f"Deposited ₹{amount:,.2f} | New balance: ₹{self.__balance:,.2f}")

    def withdraw(self, amount: float, pin: str) -> None:
        self.__verify_pin(pin)
        if amount > self.__balance:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount
        print(f"Withdrawn ₹{amount:,.2f} | New balance: ₹{self.__balance:,.2f}")

    def get_balance(self, pin: str) -> float:
        self.__verify_pin(pin)
        return self.__balance

    def change_pin(self, old_pin: str, new_pin: str) -> None:
        self.__verify_pin(old_pin)
        if len(new_pin) != 4 or not new_pin.isdigit():
            raise ValueError("PIN must be 4 digits.")
        self.__pin = new_pin
        print("PIN changed successfully.")

    def __verify_pin(self, pin: str) -> None:
        """Private method — internal use only."""
        if pin != self.__pin:
            raise PermissionError("Incorrect PIN.")

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, acct={self._account_no})"


acc = BankAccount("Alice", 10_000)
print(acc)

acc.deposit(5_000)
acc.withdraw(2_000, "0000")
print("Balance:", acc.get_balance("0000"))

print()
print("Accessing public   :", acc.owner)
print("Accessing protected:", acc._account_no)   # works, but frowned upon

# Accessing private (name-mangled)
try:
    print(acc.__balance)                           # AttributeError
except AttributeError as e:
    print(f"Direct access fails: {e}")

# Name-mangled access (for debugging only — avoid in production!)
print("Mangled access:", acc._BankAccount__balance)

acc.change_pin("0000", "1234")
print("Balance with new PIN:", acc.get_balance("1234"))
'''

CODE_FILES["06_Encapsulation/code_examples/02_intermediate.py"] = '''\
"""
02_intermediate.py - Getters, Setters, and @property
"""

# ─── WITHOUT PROPERTY (bad — no validation) ──────────────────────────────────
class BadPerson:
    def __init__(self, name, age):
        self.name = name
        self.age  = age   # nothing prevents age = -5

p = BadPerson("Alice", -5)   # silently accepts garbage
print("Bad:", p.name, p.age)


# ─── WITH EXPLICIT GETTERS / SETTERS ─────────────────────────────────────────
class OkPerson:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self.set_age(age)

    def get_name(self) -> str:
        return self._name

    def set_name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip().title()

    def get_age(self) -> int:
        return self._age

    def set_age(self, value: int) -> None:
        if not (0 <= value <= 150):
            raise ValueError(f"Age {value} out of range [0, 150].")
        self._age = value


# ─── WITH @property (Pythonic — recommended) ──────────────────────────────────
class Person:
    """Uses @property for clean, validated attribute access."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name   # calls setter
        self.age  = age    # calls setter

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip().title()

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int) or not (0 <= value <= 150):
            raise ValueError(f"Invalid age: {value}")
        self._age = value

    @property
    def is_adult(self) -> bool:
        """Read-only computed property."""
        return self._age >= 18

    # No setter for is_adult — it's derived, not stored
    def __repr__(self) -> str:
        return f"Person(name={self._name!r}, age={self._age})"


p = Person("alice", 25)
print(p)
print("Is adult:", p.is_adult)

p.name = "  bob smith  "   # auto-cleaned to "Bob Smith"
print("After name change:", p.name)

try:
    p.age = -10
except ValueError as e:
    print(f"Caught: {e}")

try:
    p.is_adult = False   # cannot set computed property
except AttributeError as e:
    print(f"Caught: {e}")
'''

# ── 07 Abstraction ───────────────────────────
CODE_FILES["07_Abstraction/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Abstraction with ABC (Abstract Base Classes)
"""
from abc import ABC, abstractmethod
from typing import List


# ─── ABSTRACT CLASS: defines a contract ──────────────────────────────────────

class Shape(ABC):
    """
    Abstract base class for all 2D shapes.
    - Cannot be instantiated directly.
    - Subclasses MUST implement abstract methods.
    """

    @abstractmethod
    def area(self) -> float:
        """Calculate and return the area."""
        ...

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate and return the perimeter."""
        ...

    # Concrete method (shared behaviour)
    def describe(self) -> str:
        return (f"{self.__class__.__name__}: "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f}")


# ─── CONCRETE SUBCLASSES ─────────────────────────────────────────────────────

class Circle(Shape):
    PI = 3.141592653589793

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return self.PI * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * self.PI * self.radius


class Rectangle(Shape):
    def __init__(self, w: float, h: float) -> None:
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h

    def perimeter(self) -> float:
        return 2 * (self.w + self.h)


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return (s * (s-self.a) * (s-self.b) * (s-self.c)) ** 0.5

    def perimeter(self) -> float:
        return self.a + self.b + self.c


# ─── DEMO ────────────────────────────────────────────────────────────────────

# Cannot instantiate ABC
try:
    s = Shape()
except TypeError as e:
    print(f"Cannot instantiate ABC: {e}")

shapes: List[Shape] = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5),
]

print()
for shape in shapes:
    print(shape.describe())

# Polymorphic usage — same interface, different implementations
total_area = sum(s.area() for s in shapes)
print(f"\\nTotal area of all shapes: {total_area:.2f}")

print()
print("isinstance checks:")
print(f"  Circle is Shape?    {isinstance(Circle(1), Shape)}")
print(f"  int is Shape?       {isinstance(42, Shape)}")
'''

# ── 08 Inheritance ───────────────────────────
CODE_FILES["08_Inheritance/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Inheritance: single, multilevel, hierarchical
"""

# ─── SINGLE INHERITANCE ───────────────────────────────────────────────────────
print("=" * 50)
print("SINGLE INHERITANCE")
print("=" * 50)

class Animal:
    """Base class (parent)."""

    def __init__(self, name: str, sound: str) -> None:
        self.name  = name
        self.sound = sound
        print(f"  [Animal.__init__] {name}")

    def speak(self) -> str:
        return f"{self.name} says {self.sound}!"

    def breathe(self) -> str:
        return f"{self.name} breathes air."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name!r})"


class Dog(Animal):
    """Derived class — inherits everything from Animal."""

    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name, "Woof")   # call parent constructor
        self.breed = breed
        print(f"  [Dog.__init__]    {name} ({breed})")

    def fetch(self, item: str) -> str:
        return f"{self.name} fetches the {item}!"

    # Method OVERRIDING
    def speak(self) -> str:
        base = super().speak()
        return f"{base} ({self.breed} bark)"


rex = Dog("Rex", "Labrador")
print(rex.speak())        # uses Dog.speak (overridden)
print(rex.breathe())      # inherited from Animal
print(rex.fetch("ball"))  # Dog-specific method

print()
print("MRO:", [c.__name__ for c in Dog.__mro__])


# ─── MULTILEVEL INHERITANCE ───────────────────────────────────────────────────
print()
print("=" * 50)
print("MULTILEVEL INHERITANCE")
print("=" * 50)

class Vehicle:
    def __init__(self, brand: str) -> None:
        self.brand = brand

    def start(self) -> str:
        return f"{self.brand} engine started."


class Car(Vehicle):
    def __init__(self, brand: str, seats: int) -> None:
        super().__init__(brand)
        self.seats = seats

    def honk(self) -> str:
        return f"{self.brand}: Beep beep!"


class ElectricCar(Car):
    def __init__(self, brand: str, seats: int, range_km: int) -> None:
        super().__init__(brand, seats)
        self.range_km = range_km

    def charge(self) -> str:
        return f"{self.brand} charging... range will be {self.range_km} km."


tesla = ElectricCar("Tesla", 5, 500)
print(tesla.start())   # from Vehicle
print(tesla.honk())    # from Car
print(tesla.charge())  # from ElectricCar


# ─── HIERARCHICAL INHERITANCE ─────────────────────────────────────────────────
print()
print("=" * 50)
print("HIERARCHICAL INHERITANCE")
print("=" * 50)

class Cat(Animal):
    def __init__(self, name: str, indoor: bool = True) -> None:
        super().__init__(name, "Meow")
        self.indoor = indoor

    def purr(self) -> str:
        return f"{self.name} purrs contentedly."


class Bird(Animal):
    def __init__(self, name: str, can_fly: bool = True) -> None:
        super().__init__(name, "Tweet")
        self.can_fly = can_fly

    def fly(self) -> str:
        if self.can_fly:
            return f"{self.name} soars through the sky!"
        return f"{self.name} cannot fly."


whiskers = Cat("Whiskers")
tweety   = Bird("Tweety")
penguin  = Bird("Tux", can_fly=False)

for animal in (rex, whiskers, tweety, penguin):
    print(animal.speak())

print(tweety.fly())
print(penguin.fly())
'''

CODE_FILES["08_Inheritance/code_examples/02_intermediate.py"] = '''\
"""
02_intermediate.py - super(), method resolution, hybrid inheritance
"""

# ─── UNDERSTANDING super() ────────────────────────────────────────────────────

class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        super().method()   # calls A.method
        print("B.method")

class C(A):
    def method(self):
        super().method()   # calls A.method
        print("C.method")

class D(B, C):             # Multiple + hierarchical
    def method(self):
        super().method()   # follows MRO: D → B → C → A
        print("D.method")

print("MRO of D:", [cls.__name__ for cls in D.__mro__])
print()
D().method()

# ─── HYBRID INHERITANCE ───────────────────────────────────────────────────────
print()
print("─" * 40)

class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> str:
        return f"I am {self.name}."


class Student(Person):
    def __init__(self, name: str, student_id: str) -> None:
        super().__init__(name)
        self.student_id = student_id

    def study(self) -> str:
        return f"{self.name} is studying."


class Employee(Person):
    def __init__(self, name: str, emp_id: str, salary: float) -> None:
        super().__init__(name)
        self.emp_id = emp_id
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is working."


class TeachingAssistant(Student, Employee):
    """A person who is both a student and an employee — diamond problem."""

    def __init__(self, name: str, student_id: str, emp_id: str, salary: float) -> None:
        # super() handles MRO cooperatively
        Student.__init__(self, name, student_id)
        Employee.__init__(self, name, emp_id, salary)

    def role(self) -> str:
        return f"{self.name}: TA with student_id={self.student_id}, emp_id={self.emp_id}"


ta = TeachingAssistant("Dr. Alice", "S001", "E101", 25_000)
print(ta.introduce())
print(ta.study())
print(ta.work())
print(ta.role())
print("MRO:", [c.__name__ for c in TeachingAssistant.__mro__])
'''

# ── 09 Polymorphism ──────────────────────────
CODE_FILES["09_Polymorphism/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Polymorphism: method overriding, duck typing, operator overloading
"""

# ─── METHOD OVERRIDING ───────────────────────────────────────────────────────

class Shape:
    def area(self) -> float:
        raise NotImplementedError

    def draw(self) -> str:
        return f"Drawing {self.__class__.__name__}"


class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self) -> float: return 3.14159 * self.r ** 2


class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self) -> float: return self.s ** 2


class Triangle(Shape):
    def __init__(self, b, h): self.b = b; self.h = h
    def area(self) -> float: return 0.5 * self.b * self.h


shapes = [Circle(5), Square(4), Triangle(6, 3)]

print("Polymorphic area() calls:")
for s in shapes:
    print(f"  {s.draw()}: area = {s.area():.2f}")   # same call, different result


# ─── DUCK TYPING ─────────────────────────────────────────────────────────────
print()
print("Duck Typing:")

class Duck:
    def quack(self): return "Quack!"
    def walk(self):  return "Waddle waddle"

class Person:
    def quack(self): return "I\'m quacking like a duck!"
    def walk(self):  return "Walking like a duck"

class RubberDuck:
    def quack(self): return "Squeak!"
    def walk(self):  return "Doesn\'t walk (it\'s rubber)"

def in_the_pond(duck_like):
    """Works with anything that has quack() and walk() — no isinstance check."""
    print(f"  {duck_like.__class__.__name__}: {duck_like.quack()} | {duck_like.walk()}")

for creature in [Duck(), Person(), RubberDuck()]:
    in_the_pond(creature)


# ─── OPERATOR OVERLOADING ─────────────────────────────────────────────────────
print()
print("Operator Overloading:")

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x; self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> "Vector":
        return self.__mul__(scalar)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector): return NotImplemented
        return self.x == other.x and self.y == other.y

    def __abs__(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"  v1         = {v1}")
print(f"  v2         = {v2}")
print(f"  v1 + v2    = {v1 + v2}")
print(f"  v1 - v2    = {v1 - v2}")
print(f"  v1 * 3     = {v1 * 3}")
print(f"  3 * v1     = {3 * v1}")
print(f"  |v1|       = {abs(v1):.2f}")
print(f"  v1 == v1   = {v1 == Vector(3, 4)}")
print(f"  v1 == v2   = {v1 == v2}")
'''

# ── 10 Special Methods ───────────────────────
CODE_FILES["10_Special_Methods/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Dunder (Magic) Methods: comprehensive guide
"""
from typing import Iterator


class Matrix:
    """
    A 2D matrix class demonstrating many dunder methods.
    """

    def __init__(self, rows: list[list]) -> None:
        self._data = [list(row) for row in rows]
        self._rows = len(rows)
        self._cols = len(rows[0]) if rows else 0

    # ── Representation ────────────────────────────────────────────────────────
    def __repr__(self) -> str:
        """For developers — should be unambiguous."""
        return f"Matrix({self._data!r})"

    def __str__(self) -> str:
        """For users — readable grid."""
        return "\\n".join("  " + " ".join(f"{v:4}" for v in row) for row in self._data)

    # ── Size / truth ──────────────────────────────────────────────────────────
    def __len__(self) -> int:
        return self._rows

    def __bool__(self) -> bool:
        return self._rows > 0 and self._cols > 0

    # ── Arithmetic ────────────────────────────────────────────────────────────
    def __add__(self, other: "Matrix") -> "Matrix":
        if (self._rows, self._cols) != (other._rows, other._cols):
            raise ValueError("Matrix dimensions must match.")
        result = [
            [self._data[r][c] + other._data[r][c] for c in range(self._cols)]
            for r in range(self._rows)
        ]
        return Matrix(result)

    def __mul__(self, scalar: int | float) -> "Matrix":
        result = [[v * scalar for v in row] for row in self._data]
        return Matrix(result)

    def __rmul__(self, scalar): return self.__mul__(scalar)

    # ── Comparison ────────────────────────────────────────────────────────────
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix): return NotImplemented
        return self._data == other._data

    # ── Item access ───────────────────────────────────────────────────────────
    def __getitem__(self, key: tuple) -> int | float:
        r, c = key
        return self._data[r][c]

    def __setitem__(self, key: tuple, value) -> None:
        r, c = key
        self._data[r][c] = value

    # ── Iteration ─────────────────────────────────────────────────────────────
    def __iter__(self) -> Iterator:
        for row in self._data:
            yield row

    # ── Contains ──────────────────────────────────────────────────────────────
    def __contains__(self, item) -> bool:
        return any(item in row for row in self._data)


# ─── DEMO ────────────────────────────────────────────────────────────────────
m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[7, 8, 9], [1, 2, 3]])

print("m1:")
print(m1)

print("\\nrepr:", repr(m1))
print("bool(m1):", bool(m1))
print("len(m1) :", len(m1), " (rows)")

print("\\nm1 + m2:")
print(m1 + m2)

print("\\nm1 * 2:")
print(m1 * 2)

print("\\nm1 == m1:", m1 == Matrix([[1,2,3],[4,5,6]]))
print("m1 == m2:", m1 == m2)

print("\\nm1[0,1] :", m1[0, 1])
m1[0, 1] = 99
print("After m1[0,1]=99:", m1[0, 1])

print("\\n5 in m1:", 5 in m1)
print("99 in m1:", 99 in m1)

print("\\nIterating rows:")
for row in m1:
    print(" ", row)
'''

CODE_FILES["10_Special_Methods/code_examples/02_context_managers.py"] = '''\
"""
02_context_managers.py - __enter__, __exit__, __call__, __del__
"""
import time


# ─── CONTEXT MANAGER ─────────────────────────────────────────────────────────

class Timer:
    """Measures elapsed time using with statement."""

    def __enter__(self):
        self._start = time.perf_counter()
        print("[Timer] Started")
        return self   # available as 'as' target

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self._start
        print(f"[Timer] Elapsed: {elapsed:.6f}s")
        # Return False (or None) to propagate exceptions
        return False


with Timer() as t:
    total = sum(range(1_000_000))
print(f"Sum: {total}")


# ─── DATABASE CONNECTION (simulation) ────────────────────────────────────────

class FakeDB:
    def __init__(self, url: str) -> None:
        self.url = url
        self._connected = False

    def __enter__(self):
        print(f"[DB] Connecting to {self.url}")
        self._connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connected = False
        print(f"[DB] Connection closed.")
        if exc_type:
            print(f"[DB] Exception occurred: {exc_val} — rolled back.")
        return False   # don't suppress exceptions

    def query(self, sql: str) -> list:
        if not self._connected:
            raise RuntimeError("Not connected!")
        print(f"[DB] Executing: {sql}")
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]


with FakeDB("sqlite:///test.db") as db:
    rows = db.query("SELECT * FROM users")
    for row in rows:
        print(" ", row)


# ─── CALLABLE OBJECTS ────────────────────────────────────────────────────────
print()

class Multiplier:
    """An object that behaves like a function."""

    def __init__(self, factor: float) -> None:
        self.factor = factor

    def __call__(self, value: float) -> float:
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))    # 10.0 — calling the object
print(triple(7))    # 21.0
print(callable(double))   # True


# ─── __del__ (destructor) ────────────────────────────────────────────────────
print()

class Resource:
    def __init__(self, name: str) -> None:
        self.name = name
        print(f"[Resource] Acquired: {name}")

    def __del__(self) -> None:
        print(f"[Resource] Released: {self.name}")

r = Resource("GPU")
del r   # triggers __del__ immediately (in CPython)
print("After del")
'''

# ── 11 Properties and Descriptors ────────────
CODE_FILES["11_Property_and_Descriptors/code_examples/01_basic.py"] = '''\
"""
01_basic.py - @property and Descriptors
"""

# ─── @property: full example ─────────────────────────────────────────────────

class Circle:
    """Radius is validated; area and diameter are computed properties."""

    def __init__(self, radius: float) -> None:
        self.radius = radius   # calls the setter

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value < 0:
            raise ValueError(f"Radius must be non-negative, got {value}.")
        self._radius = float(value)

    @radius.deleter
    def radius(self) -> None:
        print("Deleting radius")
        del self._radius

    @property
    def diameter(self) -> float:
        return 2 * self._radius

    @property
    def area(self) -> float:
        import math
        return math.pi * self._radius ** 2

    @property
    def circumference(self) -> float:
        import math
        return 2 * math.pi * self._radius

    def __repr__(self) -> str:
        return f"Circle(radius={self._radius})"


c = Circle(5)
print(c)
print(f"  diameter      = {c.diameter:.4f}")
print(f"  area          = {c.area:.4f}")
print(f"  circumference = {c.circumference:.4f}")

c.radius = 10
print(f"\\nAfter resize: {c}, area={c.area:.2f}")

try:
    c.radius = -1
except ValueError as e:
    print(f"Caught: {e}")


# ─── DESCRIPTOR PROTOCOL ─────────────────────────────────────────────────────
print()
print("── Descriptor Protocol ──")

class PositiveNumber:
    """
    A descriptor that enforces positive values.
    Can be reused across many classes.

    __set_name__  — called when class is created; knows attribute name
    __get__       — called on attribute read
    __set__       — called on attribute write
    __delete__    — called on attribute delete
    """

    def __set_name__(self, owner, name: str) -> None:
        self._name = name
        self._private = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self   # accessed on class, not instance
        return getattr(obj, self._private, None)

    def __set__(self, obj, value: float) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{self._name} must be a positive number, got {value!r}.")
        setattr(obj, self._private, float(value))

    def __delete__(self, obj) -> None:
        raise AttributeError(f"Cannot delete {self._name}.")


class Product:
    price    = PositiveNumber()
    quantity = PositiveNumber()

    def __init__(self, name: str, price: float, qty: int) -> None:
        self.name     = name
        self.price    = price      # triggers PositiveNumber.__set__
        self.quantity = qty

    @property
    def total_value(self) -> float:
        return self.price * self.quantity

    def __repr__(self) -> str:
        return f"Product({self.name!r}, ₹{self.price}, qty={self.quantity})"


p = Product("Widget", 25.50, 100)
print(p)
print(f"Total value: ₹{p.total_value:,.2f}")

try:
    p.price = -10
except ValueError as e:
    print(f"Caught: {e}")

try:
    del p.price
except AttributeError as e:
    print(f"Caught: {e}")
'''

# ── 12 Static and Class Methods ──────────────
CODE_FILES["12_Static_and_Class_Methods/code_examples/01_basic.py"] = '''\
"""
01_basic.py - @staticmethod and @classmethod deep dive
"""
from datetime import date, datetime
from typing import Optional


class DateHelper:
    """
    @staticmethod: utility methods — no class or instance state needed.
    @classmethod:  factory methods, modify class state.
    """

    _created_count = 0

    def __init__(self, d: date) -> None:
        self._date = d
        DateHelper._created_count += 1

    # ── STATIC METHODS ───────────────────────────────────────────────────────
    @staticmethod
    def is_leap_year(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and DateHelper.is_leap_year(year):
            return 29
        return days[month]

    @staticmethod
    def day_of_year(d: date) -> int:
        return d.timetuple().tm_yday

    # ── CLASS METHODS (factory constructors) ─────────────────────────────────
    @classmethod
    def today(cls) -> "DateHelper":
        return cls(date.today())

    @classmethod
    def from_string(cls, s: str) -> "DateHelper":
        """Parse 'YYYY-MM-DD'."""
        return cls(date.fromisoformat(s))

    @classmethod
    def from_parts(cls, year: int, month: int, day: int) -> "DateHelper":
        return cls(date(year, month, day))

    @classmethod
    def total_created(cls) -> int:
        return cls._created_count

    def __repr__(self) -> str:
        return f"DateHelper({self._date})"

    def __str__(self) -> str:
        return self._date.strftime("%d %B %Y")


# ─── DEMO ────────────────────────────────────────────────────────────────────
# Static method calls (no object needed)
print("Leap year 2024?:", DateHelper.is_leap_year(2024))
print("Leap year 2023?:", DateHelper.is_leap_year(2023))
print("Days in Feb 2024:", DateHelper.days_in_month(2, 2024))
print("Day of year (2024-03-15):", DateHelper.day_of_year(date(2024, 3, 15)))

# Factory methods (class methods)
d1 = DateHelper.today()
d2 = DateHelper.from_string("2024-07-04")
d3 = DateHelper.from_parts(2023, 12, 25)

print()
for d in (d1, d2, d3):
    print(str(d), "→", repr(d))

print(f"\\nTotal DateHelper objects created: {DateHelper.total_created()}")

# Can also call static method on instance (works but unusual)
print("\\nCalled on instance:", d1.is_leap_year(2024))
print("Called on class   :", DateHelper.is_leap_year(2024))
'''

# ── 13 Composition & Aggregation ─────────────
CODE_FILES["13_Composition_and_Aggregation/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Composition vs Aggregation vs Association
"""

# ─── ASSOCIATION: loose relationship ─────────────────────────────────────────
# Object A uses object B temporarily

class Printer:
    def print_doc(self, doc: str) -> None:
        print(f"[Printer] {doc}")

class Office:
    def send_report(self, printer: "Printer", text: str) -> None:
        """Office uses a Printer but doesn't own it."""
        printer.print_doc(text)

p = Printer()
o = Office()
o.send_report(p, "Q4 Financial Report")   # association: temporary use


# ─── AGGREGATION: "has-a" but parts can exist independently ──────────────────
print()

class Author:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Author({self.name!r})"


class Book:
    """A book HAS-A author. If Book is deleted, Author still exists."""

    def __init__(self, title: str, author: Author) -> None:
        self.title  = title
        self.author = author   # aggregated — passed in from outside

    def __repr__(self) -> str:
        return f"Book({self.title!r}, author={self.author.name!r})"


author = Author("George Orwell")           # created independently
book1  = Book("1984",          author)     # aggregation
book2  = Book("Animal Farm",   author)     # same author in two books

print(book1, book2, sep="\\n")
print("Author still exists:", author)     # not destroyed with books


# ─── COMPOSITION: "has-a" and OWNS the parts ─────────────────────────────────
print()

class Engine:
    def __init__(self, horsepower: int) -> None:
        self.hp      = horsepower
        self.running = False

    def start(self) -> str:
        self.running = True
        return f"Engine ({self.hp}hp) started."

    def stop(self) -> str:
        self.running = False
        return "Engine stopped."


class Car:
    """A Car OWNS its Engine — composition. Engine created inside Car."""

    def __init__(self, make: str, model: str, hp: int) -> None:
        self.make   = make
        self.model  = model
        self._engine = Engine(hp)    # created HERE — Car owns the Engine

    def drive(self) -> None:
        print(self._engine.start())
        print(f"{self.make} {self.model} is driving!")

    def park(self) -> None:
        print(self._engine.stop())
        print(f"{self.make} {self.model} is parked.")

    def __repr__(self) -> str:
        return f"Car({self.make} {self.model}, {self._engine.hp}hp)"


car = Car("Toyota", "Corolla", 140)
car.drive()
car.park()
print(car)

# ─── SUMMARY TABLE ───────────────────────────────────────────────────────────
print()
print(f"{'Relationship':<16} | {'Coupling':<10} | {'Lifecycle':<20} | Example")
print("─" * 70)
rows = [
    ("Association",  "Weak",   "Independent",   "Office uses Printer"),
    ("Aggregation",  "Medium", "Independent",   "Book has Author"),
    ("Composition",  "Strong", "Same lifetime", "Car owns Engine"),
    ("Dependency",   "Weak",   "Temporary",     "Function takes param"),
]
for name, coupling, lifecycle, example in rows:
    print(f"{name:<16} | {coupling:<10} | {lifecycle:<20} | {example}")
'''

# ── 14 Multiple Inheritance ──────────────────
CODE_FILES["14_Multiple_Inheritance/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Multiple Inheritance and Mixins
"""

# ─── MULTIPLE INHERITANCE ────────────────────────────────────────────────────

class Flyable:
    def fly(self) -> str:
        return f"{self.__class__.__name__} is flying!"

    def land(self) -> str:
        return f"{self.__class__.__name__} has landed."


class Swimmable:
    def swim(self) -> str:
        return f"{self.__class__.__name__} is swimming!"

    def surface(self) -> str:
        return f"{self.__class__.__name__} surfaced."


class Walkable:
    def walk(self) -> str:
        return f"{self.__class__.__name__} is walking."


class Duck(Flyable, Swimmable, Walkable):
    """A duck can fly, swim, and walk."""
    def quack(self) -> str:
        return "Quack!"


class FlyingFish(Flyable, Swimmable):
    """Can fly and swim but not walk."""
    pass


class Human(Walkable, Swimmable):
    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> str:
        return f"Hi, I'm {self.name}!"


donald = Duck()
print(donald.fly())
print(donald.swim())
print(donald.walk())
print(donald.quack())

print()
fish = FlyingFish()
print(fish.fly())
print(fish.swim())

print()
bob = Human("Bob")
print(bob.introduce())
print(bob.walk())
print(bob.swim())


# ─── MIXIN PATTERN ───────────────────────────────────────────────────────────
print()
print("─ Mixins ─")

class JSONMixin:
    """Add .to_json() and .from_json() to any class."""
    import json as _json

    def to_json(self) -> str:
        import json
        return json.dumps(self.__dict__, default=str)

    @classmethod
    def from_json(cls, s: str):
        import json
        data = json.loads(s)
        obj = cls.__new__(cls)
        obj.__dict__.update(data)
        return obj


class LogMixin:
    """Add logging to method calls."""
    def log(self, msg: str) -> None:
        print(f"[{self.__class__.__name__}] {msg}")


class ValidateMixin:
    """Add basic validation."""
    def validate(self) -> bool:
        raise NotImplementedError("Subclass must implement validate()")


class User(JSONMixin, LogMixin):
    def __init__(self, name: str, email: str, age: int) -> None:
        self.name  = name
        self.email = email
        self.age   = age

    def save(self) -> None:
        self.log(f"Saving user {self.name}")
        print(f"  JSON: {self.to_json()}")


user = User("Alice", "alice@example.com", 28)
user.save()

reconstructed = User.from_json(user.to_json())
print(f"Reconstructed: {reconstructed.name}, {reconstructed.email}")
'''

# ── 15 MRO ───────────────────────────────────
CODE_FILES["15_Method_Resolution_Order/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Method Resolution Order (MRO) and C3 Linearization
"""

# ─── MRO BASICS ──────────────────────────────────────────────────────────────

class A:
    def hello(self): return "Hello from A"
    def who(self):   return "A"

class B(A):
    def hello(self): return "Hello from B"
    def who(self):   return f"B → {super().who()}"

class C(A):
    def hello(self): return "Hello from C"
    def who(self):   return f"C → {super().who()}"

class D(B, C):
    def who(self): return f"D → {super().who()}"

# MRO = D, B, C, A  (C3 linearization)
print("MRO of D:", [cls.__name__ for cls in D.__mro__])
print()
d = D()
print("d.hello():", d.hello())     # B (first in MRO that has hello)
print("d.who()  :", d.who())       # D → B → C → A (cooperative super() chain)


# ─── THE DIAMOND PROBLEM ──────────────────────────────────────────────────────
print()
print("── Diamond Problem ──")

class Base:
    def __init__(self):
        print("  Base.__init__")

class Left(Base):
    def __init__(self):
        print("  Left.__init__")
        super().__init__()   # cooperative — won't call Base twice

class Right(Base):
    def __init__(self):
        print("  Right.__init__")
        super().__init__()

class Diamond(Left, Right):
    def __init__(self):
        print("  Diamond.__init__")
        super().__init__()

print("MRO:", [c.__name__ for c in Diamond.__mro__])
print("Creating Diamond:")
d = Diamond()   # Base.__init__ called ONCE — cooperative super() handles this


# ─── C3 LINEARIZATION EXPLAINED ──────────────────────────────────────────────
print()
print("── C3 Linearization ──")

# L[C] = C + merge(L[B1], L[B2], ..., [B1, B2, ...])
# Rule: take the head of the first list if it doesn't appear
#        in the tail of any other list.

class X: pass
class Y: pass
class Z: pass
class P(X, Y): pass
class Q(Y, Z): pass
class R(P, Q): pass

for cls in (X, Y, Z, P, Q, R):
    mro_names = [c.__name__ for c in cls.__mro__]
    print(f"  MRO({cls.__name__}): {' → '.join(mro_names)}")


# ─── VERIFYING MRO WITH help() ───────────────────────────────────────────────
print()
print("── Checking MRO at runtime ──")
print("D.__mro__       :", D.__mro__)
print("D.mro()         :", D.mro())       # equivalent
print("issubclass(B,A) :", issubclass(B, A))
print("issubclass(D,A) :", issubclass(D, A))
print("issubclass(A,D) :", issubclass(A, D))
'''

# ── 16 Abstract Base Classes ─────────────────
CODE_FILES["16_Abstract_Base_Classes/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Abstract Base Classes (ABC module) — complete guide
"""
from abc import ABC, abstractmethod, ABCMeta
from typing import Protocol, runtime_checkable


# ─── BASIC ABC ────────────────────────────────────────────────────────────────

class Animal(ABC):
    """Abstract base — cannot be instantiated."""

    @abstractmethod
    def speak(self) -> str: ...

    @abstractmethod
    def move(self)  -> str: ...

    @property
    @abstractmethod
    def category(self) -> str: ...

    # Concrete method available to all subclasses
    def breathe(self) -> str:
        return f"{self.__class__.__name__} breathes."


class Dog(Animal):
    def speak(self)    -> str: return "Woof!"
    def move(self)     -> str: return "Runs on 4 legs"
    @property
    def category(self) -> str: return "Mammal"


class Snake(Animal):
    def speak(self)    -> str: return "Hiss!"
    def move(self)     -> str: return "Slithers"
    @property
    def category(self) -> str: return "Reptile"


# Cannot instantiate ABC
try:
    a = Animal()
except TypeError as e:
    print(f"ABC error: {e}")

for animal in (Dog(), Snake()):
    print(f"{animal.__class__.__name__}: {animal.speak()}, "
          f"{animal.move()}, {animal.category}, {animal.breathe()}")


# ─── ABSTRACT CLASSMETHOD / STATICMETHOD ────────────────────────────────────
print()

class DataSource(ABC):

    @classmethod
    @abstractmethod
    def connect(cls, url: str) -> "DataSource": ...

    @staticmethod
    @abstractmethod
    def validate_url(url: str) -> bool: ...

    @abstractmethod
    def fetch(self, query: str) -> list: ...


class SQLiteSource(DataSource):
    def __init__(self, url: str) -> None:
        self.url = url

    @classmethod
    def connect(cls, url: str) -> "SQLiteSource":
        print(f"Connecting to SQLite: {url}")
        return cls(url)

    @staticmethod
    def validate_url(url: str) -> bool:
        return url.startswith("sqlite:///")

    def fetch(self, query: str) -> list:
        print(f"Fetching: {query}")
        return [{"id": 1}, {"id": 2}]


db = SQLiteSource.connect("sqlite:///test.db")
print("Valid URL?", SQLiteSource.validate_url("sqlite:///test.db"))
print("Results:", db.fetch("SELECT * FROM users"))


# ─── PROTOCOL (structural subtyping / duck typing + type checks) ─────────────
print()

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...
    def color(self) -> str: ...


class Circle:
    def draw(self)  -> str: return "Drawing circle"
    def color(self) -> str: return "Red"

class Square:
    def draw(self)  -> str: return "Drawing square"
    def color(self) -> str: return "Blue"

class Unrelated:
    def hello(self) -> str: return "Hi"


for obj in (Circle(), Square(), Unrelated()):
    print(f"{obj.__class__.__name__} implements Drawable? "
          f"{isinstance(obj, Drawable)}")
'''

# ── 17 Data Classes ──────────────────────────
CODE_FILES["17_Data_Classes/code_examples/01_basic.py"] = '''\
"""
01_basic.py - @dataclass: modern Python data modelling
"""
from dataclasses import dataclass, field, asdict, astuple, replace
from typing import List, ClassVar
from datetime import date


# ─── BASIC DATACLASS ─────────────────────────────────────────────────────────

@dataclass
class Point:
    """Auto-generates __init__, __repr__, __eq__."""
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5


p1 = Point(3, 4)
p2 = Point(0, 0)

print(repr(p1))                      # Point(x=3, y=4)
print(p1 == Point(3, 4))             # True
print(p1.distance_to(p2))           # 5.0


# ─── DATACLASS WITH DEFAULTS AND FACTORY ──────────────────────────────────────

@dataclass
class Student:
    name:       str
    student_id: str
    gpa:        float = 0.0
    courses:    List[str] = field(default_factory=list)   # mutable default
    enrolled:   date     = field(default_factory=date.today)

    # ClassVar is NOT included in __init__
    PASSING_GPA: ClassVar[float] = 2.0

    def is_passing(self) -> bool:
        return self.gpa >= self.PASSING_GPA

    def enroll(self, course: str) -> None:
        self.courses.append(course)


s1 = Student("Alice", "S001", 3.8)
s2 = Student("Bob",   "S002", 1.5)

s1.enroll("Math")
s1.enroll("Physics")

print(s1)
print(f"Passing: {s1.is_passing()}")
print(f"Bob passing: {s2.is_passing()}")

# asdict / astuple
print("As dict :", asdict(s1))
print("As tuple:", astuple(p1))


# ─── FROZEN DATACLASS (immutable) ────────────────────────────────────────────

@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

    def __post_init__(self):
        for name, val in (("r", self.r), ("g", self.g), ("b", self.b)):
            if not (0 <= val <= 255):
                raise ValueError(f"{name}={val} out of range [0, 255].")

    @property
    def hex(self) -> str:
        return f"#{self.r:02X}{self.g:02X}{self.b:02X}"


red   = Color(255, 0, 0)
green = Color(0, 255, 0)

print(f"Red hex  : {red.hex}")
print(f"Green hex: {green.hex}")

try:
    red.r = 100          # frozen!
except Exception as e:
    print(f"Frozen error: {e}")

# 'replace' creates a new instance with changes
brighter_red = replace(red, r=200)
print(f"Brighter red: {brighter_red.hex}")

# Frozen dataclasses are hashable (can be in sets / dict keys)
palette = {red, green, Color(0, 0, 255)}
print(f"Palette: {palette}")
'''

# ── 18 Type Hints ────────────────────────────
CODE_FILES["18_Type_Hints/code_examples/01_basic.py"] = '''\
"""
01_basic.py - Type Hints: from basics to generics and protocols
"""
from __future__ import annotations
from typing import (
    List, Dict, Tuple, Set, Optional, Union,
    Callable, TypeVar, Generic, Sequence, Any
)
from collections.abc import Iterator


# ─── BASIC ANNOTATIONS ───────────────────────────────────────────────────────

def greet(name: str, times: int = 1) -> str:
    return ("Hello, " + name + "! ") * times

result: str = greet("Alice", 3)
print(result)

def square(n: int | float) -> int | float:
    """Union via | (Python 3.10+)."""
    return n * n

print(square(4), square(3.14))


# ─── CONTAINER TYPES ─────────────────────────────────────────────────────────

def sum_list(nums: list[int]) -> int:
    return sum(nums)

def word_lengths(words: list[str]) -> dict[str, int]:
    return {w: len(w) for w in words}

def first_last(seq: Sequence[Any]) -> tuple[Any, Any]:
    return seq[0], seq[-1]

print(sum_list([1, 2, 3, 4, 5]))
print(word_lengths(["hello", "world"]))
print(first_last([10, 20, 30, 40]))


# ─── OPTIONAL ────────────────────────────────────────────────────────────────

def find_user(user_id: int) -> Optional[str]:
    db = {1: "Alice", 2: "Bob"}
    return db.get(user_id)    # returns str or None

print(find_user(1))
print(find_user(99))


# ─── CALLABLE ────────────────────────────────────────────────────────────────

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

print(apply(lambda x: x * 2, 10))


# ─── GENERICS ────────────────────────────────────────────────────────────────

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")

class Stack(Generic[T]):
    """Type-safe stack."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("Stack is empty.")
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items})"


int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)
print(int_stack)
print("Pop:", int_stack.pop())
print(int_stack)

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")
print(str_stack)


# ─── ITERATOR TYPE ───────────────────────────────────────────────────────────

def countdown(n: int) -> Iterator[int]:
    while n >= 0:
        yield n
        n -= 1

print(list(countdown(5)))
print("Type hints demo complete ✅")
'''

# ── 19 Design Principles (SOLID) ─────────────
CODE_FILES["19_Design_Principles/code_examples/01_basic.py"] = '''\
"""
01_basic.py - SOLID Principles in Python
"""

# ════════════════════════════════════════════════
# S - Single Responsibility Principle (SRP)
# ════════════════════════════════════════════════

# ❌ BAD: one class does too many things
class BadUserManager:
    def save_to_db(self, user):     ...
    def send_email(self, user):     ...
    def generate_report(self, user): ...

# ✅ GOOD: each class has ONE reason to change
class UserRepository:
    def save(self, user: dict) -> None:
        print(f"[DB] Saved {user['name']}")

class EmailService:
    def send_welcome(self, user: dict) -> None:
        print(f"[Email] Welcome, {user['name']}!")

class ReportGenerator:
    def generate(self, user: dict) -> str:
        return f"Report for {user['name']}"

user = {"name": "Alice", "email": "alice@ex.com"}
UserRepository().save(user)
EmailService().send_welcome(user)
print(ReportGenerator().generate(user))


# ════════════════════════════════════════════════
# O - Open/Closed Principle (OCP)
# ════════════════════════════════════════════════
print()
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float: ...

class NoDiscount(Discount):
    def apply(self, price: float) -> float: return price

class PercentDiscount(Discount):
    def __init__(self, pct: float) -> None: self.pct = pct
    def apply(self, price: float) -> float: return price * (1 - self.pct/100)

class FlatDiscount(Discount):
    def __init__(self, amount: float) -> None: self.amount = amount
    def apply(self, price: float) -> float: return max(0, price - self.amount)

class Order:
    def __init__(self, price: float, discount: Discount) -> None:
        self.final = discount.apply(price)

# Adding new discount type = add new class, NOT modify Order
print(Order(1000, NoDiscount()).final)
print(Order(1000, PercentDiscount(10)).final)
print(Order(1000, FlatDiscount(150)).final)


# ════════════════════════════════════════════════
# L - Liskov Substitution Principle (LSP)
# ════════════════════════════════════════════════
print()

class Bird(ABC):
    @abstractmethod
    def move(self) -> str: ...

class FlyingBird(Bird):
    def move(self) -> str: return "Flying"

class Penguin(Bird):         # Penguin IS-A Bird but cannot fly
    def move(self) -> str: return "Swimming"   # ✅ LSP: substitutable

def let_it_move(bird: Bird) -> None:
    print(f"{bird.__class__.__name__}: {bird.move()}")

for b in (FlyingBird(), Penguin()):
    let_it_move(b)   # works without knowing the concrete type


# ════════════════════════════════════════════════
# I - Interface Segregation Principle (ISP)
# ════════════════════════════════════════════════
print()

# ❌ FAT interface forces classes to implement unused methods
class FatWorker(ABC):
    @abstractmethod
    def work(self): ...
    @abstractmethod
    def eat(self):  ...
    @abstractmethod
    def sleep(self): ...

# ✅ Slim, focused interfaces
class Workable(ABC):
    @abstractmethod
    def work(self) -> str: ...

class Eatable(ABC):
    @abstractmethod
    def eat(self) -> str: ...

class HumanWorker(Workable, Eatable):
    def work(self) -> str: return "Human working"
    def eat(self)  -> str: return "Human eating"

class RobotWorker(Workable):
    def work(self) -> str: return "Robot working"
    # Robots don\'t eat — no need to implement eat()!

print(HumanWorker().work(), HumanWorker().eat())
print(RobotWorker().work())


# ════════════════════════════════════════════════
# D - Dependency Inversion Principle (DIP)
# ════════════════════════════════════════════════
print()

class MessageSender(ABC):
    @abstractmethod
    def send(self, msg: str) -> None: ...

class EmailSender(MessageSender):
    def send(self, msg: str) -> None:
        print(f"[Email] {msg}")

class SMSSender(MessageSender):
    def send(self, msg: str) -> None:
        print(f"[SMS] {msg}")

class Notification:
    """Depends on ABSTRACTION, not concrete sender."""
    def __init__(self, sender: MessageSender) -> None:
        self._sender = sender

    def notify(self, msg: str) -> None:
        self._sender.send(msg)

# Swap sender without changing Notification
Notification(EmailSender()).notify("Server is down!")
Notification(SMSSender()).notify("Server is down!")

print("\\nSOLID principles demonstrated ✅")
'''

# ── 20 Design Patterns ───────────────────────
CODE_FILES["20_Design_Patterns/code_examples/01_creational.py"] = '''\
"""
01_creational.py - Singleton, Factory, Builder, Prototype
"""
import copy

# ════════════════════════════════════════════════
# SINGLETON PATTERN
# ════════════════════════════════════════════════

class Config:
    """Only one Config instance exists application-wide."""
    _instance: "Config | None" = None

    def __new__(cls) -> "Config":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._data = {}
        return cls._instance

    def set(self, key: str, value) -> None:
        self._data[key] = value

    def get(self, key: str):
        return self._data.get(key)

    def __repr__(self) -> str:
        return f"Config({self._data})"


c1 = Config()
c2 = Config()
c1.set("db_host", "localhost")
print("c1 is c2 :", c1 is c2)     # True
print("c2.db_host:", c2.get("db_host"))  # localhost — same object!


# ════════════════════════════════════════════════
# FACTORY PATTERN
# ════════════════════════════════════════════════
print()
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, msg: str) -> None: ...

class EmailNotification(Notification):
    def send(self, msg: str) -> None: print(f"[Email] {msg}")

class SMSNotification(Notification):
    def send(self, msg: str) -> None: print(f"[SMS] {msg}")

class PushNotification(Notification):
    def send(self, msg: str) -> None: print(f"[Push] {msg}")

class NotificationFactory:
    """Create notification objects without exposing creation logic."""

    _registry = {
        "email": EmailNotification,
        "sms"  : SMSNotification,
        "push" : PushNotification,
    }

    @classmethod
    def create(cls, kind: str) -> Notification:
        klass = cls._registry.get(kind.lower())
        if klass is None:
            raise ValueError(f"Unknown notification type: {kind!r}")
        return klass()

for kind in ("email", "sms", "push"):
    n = NotificationFactory.create(kind)
    n.send("Server alert!")


# ════════════════════════════════════════════════
# BUILDER PATTERN
# ════════════════════════════════════════════════
print()

class Pizza:
    def __init__(self) -> None:
        self.size   = ""
        self.crust  = ""
        self.sauce  = ""
        self.cheese = ""
        self.toppings: list = []

    def __str__(self) -> str:
        tops = ", ".join(self.toppings) or "none"
        return (f"Pizza [{self.size}, {self.crust} crust, "
                f"{self.sauce} sauce, {self.cheese} cheese, toppings: {tops}]")


class PizzaBuilder:
    def __init__(self)         : self._pizza = Pizza()
    def size(self, s: str)     : self._pizza.size   = s;  return self
    def crust(self, c: str)    : self._pizza.crust  = c;  return self
    def sauce(self, s: str)    : self._pizza.sauce  = s;  return self
    def cheese(self, c: str)   : self._pizza.cheese = c;  return self
    def topping(self, t: str)  : self._pizza.toppings.append(t); return self
    def build(self) -> Pizza   : return self._pizza


my_pizza = (PizzaBuilder()
            .size("large")
            .crust("thin")
            .sauce("tomato")
            .cheese("mozzarella")
            .topping("mushrooms")
            .topping("olives")
            .build())

print(my_pizza)


# ════════════════════════════════════════════════
# PROTOTYPE PATTERN
# ════════════════════════════════════════════════
print()

class DocumentTemplate:
    def __init__(self, title: str, header: str, footer: str) -> None:
        self.title  = title
        self.header = header
        self.footer = footer
        self.sections: list[str] = []

    def add_section(self, text: str) -> None:
        self.sections.append(text)

    def clone(self) -> "DocumentTemplate":
        return copy.deepcopy(self)

    def __repr__(self) -> str:
        return f"Doc({self.title!r}, sections={len(self.sections)})"


template = DocumentTemplate("Company Report", "ACME Corp", "Confidential")
template.add_section("Introduction")

# Clone for different departments
q1 = template.clone()
q1.title = "Q1 Report"
q1.add_section("Q1 Sales Data")

q2 = template.clone()
q2.title = "Q2 Report"
q2.add_section("Q2 Sales Data")

print(template)
print(q1)
print(q2)
print("Are different objects:", template is not q1)
'''

CODE_FILES["20_Design_Patterns/code_examples/02_structural.py"] = '''\
"""
02_structural.py - Adapter, Decorator, Observer, Strategy
"""

# ════════════════════════════════════════════════
# ADAPTER PATTERN
# ════════════════════════════════════════════════

class EuropeanSocket:
    """Existing interface — provides 230V."""
    def provide_power(self) -> str:
        return "230V AC"

class USASocket:
    """Target interface — client expects 110V."""
    def supply_power(self) -> str: ...

class SocketAdapter(USASocket):
    """Adapts EuropeanSocket to USASocket interface."""

    def __init__(self, european: EuropeanSocket) -> None:
        self._euro = european

    def supply_power(self) -> str:
        raw = self._euro.provide_power()
        return f"Converted {raw} → 110V AC"


euro = EuropeanSocket()
adapter = SocketAdapter(euro)
print("Adapter:", adapter.supply_power())


# ════════════════════════════════════════════════
# DECORATOR PATTERN (structural, NOT @decorator syntax)
# ════════════════════════════════════════════════
print()
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float: ...
    @abstractmethod
    def description(self) -> str: ...

class SimpleCoffee(Coffee):
    def cost(self) -> float: return 50
    def description(self) -> str: return "Simple Coffee"

class MilkDecorator(Coffee):
    def __init__(self, coffee: Coffee) -> None: self._coffee = coffee
    def cost(self) -> float: return self._coffee.cost() + 15
    def description(self) -> str: return self._coffee.description() + " + Milk"

class SugarDecorator(Coffee):
    def __init__(self, coffee: Coffee) -> None: self._coffee = coffee
    def cost(self) -> float: return self._coffee.cost() + 5
    def description(self) -> str: return self._coffee.description() + " + Sugar"

class VanillaDecorator(Coffee):
    def __init__(self, coffee: Coffee) -> None: self._coffee = coffee
    def cost(self) -> float: return self._coffee.cost() + 20
    def description(self) -> str: return self._coffee.description() + " + Vanilla"


order = VanillaDecorator(SugarDecorator(MilkDecorator(SimpleCoffee())))
print(f"Order: {order.description()}")
print(f"Cost : ₹{order.cost()}")


# ════════════════════════════════════════════════
# OBSERVER PATTERN
# ════════════════════════════════════════════════
print()

class EventSystem:
    """Simple event emitter."""
    def __init__(self) -> None:
        self._listeners: dict[str, list] = {}

    def subscribe(self, event: str, listener) -> None:
        self._listeners.setdefault(event, []).append(listener)

    def emit(self, event: str, **data) -> None:
        for listener in self._listeners.get(event, []):
            listener(**data)


class StockMarket:
    def __init__(self) -> None:
        self.events = EventSystem()
        self._prices: dict[str, float] = {}

    def update_price(self, ticker: str, price: float) -> None:
        old = self._prices.get(ticker, 0)
        self._prices[ticker] = price
        self.events.emit("price_change", ticker=ticker, old=old, new=price)


def email_alert(ticker, old, new):
    print(f"  [Email] {ticker}: {old} → {new}")

def sms_alert(ticker, old, new):
    if abs(new - old) / max(old, 1) > 0.05:
        print(f"  [SMS!] Big move in {ticker}: {old} → {new}")


market = StockMarket()
market.events.subscribe("price_change", email_alert)
market.events.subscribe("price_change", sms_alert)

market.update_price("AAPL", 150)
market.update_price("AAPL", 160)   # >5% change triggers SMS


# ════════════════════════════════════════════════
# STRATEGY PATTERN
# ════════════════════════════════════════════════
print()

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list: ...

class BubbleSort(SortStrategy):
    def sort(self, data: list) -> list:
        d = data.copy()
        for i in range(len(d)):
            for j in range(len(d)-i-1):
                if d[j] > d[j+1]: d[j], d[j+1] = d[j+1], d[j]
        return d

class QuickSort(SortStrategy):
    def sort(self, data: list) -> list:
        if len(data) <= 1: return data
        p = data[len(data)//2]
        left   = [x for x in data if x < p]
        middle = [x for x in data if x == p]
        right  = [x for x in data if x > p]
        return self.sort(left) + middle + self.sort(right)

class Sorter:
    def __init__(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def sort(self, data: list) -> list:
        return self._strategy.sort(data)

    def set_strategy(self, strategy: SortStrategy) -> None:
        self._strategy = strategy


data = [64, 34, 25, 12, 22, 11, 90]
sorter = Sorter(BubbleSort())
print("Bubble:", sorter.sort(data))

sorter.set_strategy(QuickSort())
print("Quick :", sorter.sort(data))
'''

# ── Interview Preparation ────────────────────
CODE_FILES["22_Interview_Preparation/code_examples/01_tricky.py"] = '''\
"""
01_tricky.py - Tricky OOP Interview Questions with solutions
"""

# ─── Q1: What is the output? ─────────────────────────────────────────────────
print("Q1:")
class A:
    x = 1

class B(A): pass
class C(A): pass

A.x = 2          # change class variable in A
print(B.x, C.x)  # 2 2  — B and C inherit from A

B.x = 3          # now B has its OWN x (shadows A.x)
print(A.x, B.x, C.x)  # 2 3 2


# ─── Q2: __new__ vs __init__ ─────────────────────────────────────────────────
print("\\nQ2:")
class Meta:
    def __new__(cls, *args, **kwargs):
        print(f"  __new__ called with cls={cls.__name__}")
        return super().__new__(cls)

    def __init__(self, value):
        print(f"  __init__ called with value={value}")
        self.value = value

m = Meta(42)
# __new__ creates the object (allocates memory)
# __init__ initialises it


# ─── Q3: Mutable default argument (classic trap) ─────────────────────────────
print("\\nQ3:")
class Store:
    def __init__(self, items=[]):   # ❌ shared across instances!
        self.items = items

    def add(self, item):
        self.items.append(item)

s1 = Store(); s1.add("apple")
s2 = Store()
print("s2.items:", s2.items)   # ['apple'] — SURPRISE!

# Fix:
class GoodStore:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def add(self, item):
        self.items.append(item)

g1 = GoodStore(); g1.add("apple")
g2 = GoodStore()
print("g2.items:", g2.items)   # [] ✅


# ─── Q4: Name mangling ───────────────────────────────────────────────────────
print("\\nQ4:")
class Secret:
    __code = "TOP_SECRET"   # __code → _Secret__code

    def reveal(self):
        return self.__code

s = Secret()
print(s.reveal())
try:
    print(s.__code)
except AttributeError:
    print("s.__code raises AttributeError ✅")

print("Mangled:", s._Secret__code)   # works — just obfuscated, not truly private


# ─── Q5: super() in multiple inheritance ─────────────────────────────────────
print("\\nQ5:")
class Base:
    def greet(self): print("Base.greet")

class Left(Base):
    def greet(self):
        print("Left.greet")
        super().greet()

class Right(Base):
    def greet(self):
        print("Right.greet")
        super().greet()

class Child(Left, Right):
    def greet(self):
        print("Child.greet")
        super().greet()

Child().greet()
# MRO: Child → Left → Right → Base
# Each super() goes to the NEXT class in MRO


# ─── Q6: isinstance vs type ──────────────────────────────────────────────────
print("\\nQ6:")
class Animal: pass
class Dog(Animal): pass

d = Dog()
print("type(d) == Dog    :", type(d) == Dog)       # True
print("type(d) == Animal :", type(d) == Animal)    # False  ← misses subclass!
print("isinstance(d, Dog)    :", isinstance(d, Dog))     # True
print("isinstance(d, Animal) :", isinstance(d, Animal))  # True  ← handles subclass
# ✅ Prefer isinstance() — it respects inheritance


# ─── Q7: Property vs attribute ───────────────────────────────────────────────
print("\\nQ7:")
class Temperature:
    def __init__(self, celsius):
        self._c = celsius

    @property
    def celsius(self): return self._c

    @celsius.setter
    def celsius(self, v):
        if v < -273.15: raise ValueError("Below absolute zero!")
        self._c = v

    @property
    def fahrenheit(self): return self._c * 9/5 + 32

t = Temperature(100)
print(f"{t.celsius}°C = {t.fahrenheit}°F")
t.celsius = 0
print(f"{t.celsius}°C = {t.fahrenheit}°F")


# ─── Q8: __slots__ ───────────────────────────────────────────────────────────
print("\\nQ8:")
class WithSlots:
    __slots__ = ("x", "y")   # prevents __dict__; saves memory

    def __init__(self, x, y):
        self.x = x; self.y = y

p = WithSlots(3, 4)
print(f"x={p.x}, y={p.y}")
try:
    p.z = 5   # no __dict__, so this fails!
except AttributeError as e:
    print(f"Caught: {e}")
'''

# ── Real World Projects ──────────────────────
CODE_FILES["21_Real_World_Projects/Project_1_Library/library_system.py"] = '''\
"""
Library Management System — complete OOP project
Features: add books, register members, issue/return books, fines
"""
from datetime import date, timedelta
from typing import Optional
from dataclasses import dataclass, field
import uuid


# ─── MODELS ──────────────────────────────────────────────────────────────────

@dataclass
class Book:
    title:    str
    author:   str
    isbn:     str
    copies:   int = 1
    available: int = field(init=False)

    def __post_init__(self):
        self.available = self.copies

    def is_available(self) -> bool:
        return self.available > 0

    def checkout(self) -> bool:
        if self.is_available():
            self.available -= 1
            return True
        return False

    def return_book(self) -> None:
        if self.available < self.copies:
            self.available += 1


@dataclass
class Member:
    name:        str
    email:       str
    member_id:   str = field(default_factory=lambda: str(uuid.uuid4())[:8].upper())
    active_loans: list = field(default_factory=list)
    MAX_LOANS:   int  = 3

    def can_borrow(self) -> bool:
        return len(self.active_loans) < self.MAX_LOANS


@dataclass
class Loan:
    book:        Book
    member:      Member
    loan_date:   date = field(default_factory=date.today)
    due_date:    date = field(init=False)
    return_date: Optional[date] = None
    LOAN_DAYS:   int = 14
    FINE_PER_DAY: float = 5.0

    def __post_init__(self):
        self.due_date = self.loan_date + timedelta(days=self.LOAN_DAYS)

    @property
    def is_overdue(self) -> bool:
        check = self.return_date or date.today()
        return check > self.due_date

    @property
    def fine(self) -> float:
        if not self.is_overdue:
            return 0.0
        check = self.return_date or date.today()
        days_late = (check - self.due_date).days
        return days_late * self.FINE_PER_DAY

    def __repr__(self) -> str:
        return (f"Loan({self.book.title!r} → {self.member.name!r}, "
                f"due={self.due_date})")


# ─── LIBRARY ──────────────────────────────────────────────────────────────────

class Library:
    def __init__(self, name: str) -> None:
        self.name    = name
        self._books:   dict[str, Book]   = {}   # isbn → Book
        self._members: dict[str, Member] = {}   # member_id → Member
        self._loans:   list[Loan]        = []

    # Books
    def add_book(self, book: Book) -> None:
        if book.isbn in self._books:
            self._books[book.isbn].copies   += book.copies
            self._books[book.isbn].available += book.copies
        else:
            self._books[book.isbn] = book
        print(f"[Library] Added: {book.title!r}")

    def find_book(self, query: str) -> list[Book]:
        q = query.lower()
        return [b for b in self._books.values()
                if q in b.title.lower() or q in b.author.lower() or q == b.isbn]

    # Members
    def register_member(self, member: Member) -> None:
        self._members[member.member_id] = member
        print(f"[Library] Registered: {member.name!r} (ID: {member.member_id})")

    # Loans
    def issue_book(self, isbn: str, member_id: str) -> Optional[Loan]:
        book   = self._books.get(isbn)
        member = self._members.get(member_id)

        if not book:
            print("Book not found.")
            return None
        if not member:
            print("Member not found.")
            return None
        if not book.is_available():
            print(f"No copies of {book.title!r} available.")
            return None
        if not member.can_borrow():
            print(f"{member.name} has reached max loan limit ({member.MAX_LOANS}).")
            return None

        book.checkout()
        loan = Loan(book, member)
        self._loans.append(loan)
        member.active_loans.append(loan)
        print(f"[Library] Issued {book.title!r} to {member.name!r}. Due: {loan.due_date}")
        return loan

    def return_book(self, loan: Loan) -> float:
        loan.return_date = date.today()
        loan.book.return_book()
        if loan in loan.member.active_loans:
            loan.member.active_loans.remove(loan)
        fine = loan.fine
        if fine > 0:
            print(f"[Library] {loan.book.title!r} returned LATE. Fine: ₹{fine:.2f}")
        else:
            print(f"[Library] {loan.book.title!r} returned on time.")
        return fine

    def report(self) -> None:
        print(f"\\n{'═'*50}")
        print(f"  {self.name.upper()} — REPORT")
        print(f"{'═'*50}")
        print(f"  Books   : {len(self._books)} titles")
        print(f"  Members : {len(self._members)}")
        print(f"  Loans   : {len(self._loans)} total")
        active = [l for l in self._loans if l.return_date is None]
        print(f"  Active  : {len(active)}")
        overdue = [l for l in active if l.is_overdue]
        print(f"  Overdue : {len(overdue)}")
        print(f"{'═'*50}")


# ─── DEMO ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    lib = Library("City Central Library")

    # Add books
    books = [
        Book("Python Crash Course",     "Eric Matthes",     "978-1593279288", 3),
        Book("Clean Code",              "Robert C. Martin", "978-0132350884", 2),
        Book("Design Patterns",         "Gang of Four",     "978-0201633610", 1),
        Book("The Pragmatic Programmer","Hunt & Thomas",    "978-0135957059", 2),
    ]
    for book in books:
        lib.add_book(book)

    # Register members
    members = [
        Member("Alice Kumar",  "alice@email.com"),
        Member("Bob Sharma",   "bob@email.com"),
        Member("Carol Singh",  "carol@email.com"),
    ]
    for m in members:
        lib.register_member(m)

    print()
    # Issue books
    loan1 = lib.issue_book("978-1593279288", members[0].member_id)
    loan2 = lib.issue_book("978-0132350884", members[0].member_id)
    loan3 = lib.issue_book("978-0201633610", members[1].member_id)

    # Search
    print()
    results = lib.find_book("python")
    print(f"Search 'python': {[b.title for b in results]}")

    # Return
    print()
    if loan1:
        lib.return_book(loan1)

    lib.report()
'''

# ── Practice questions ────────────────────────
CODE_FILES["23_Practice/Beginner/01_questions.py"] = '''\
"""
Beginner Practice — 30 OOP questions
Run this file to see questions. Solutions in 02_solutions.py.
"""

questions = [
    # Basics
    " 1. Create a class `Circle` with a `radius` attribute and a method `area()` that returns π*r².",
    " 2. Create a class `Rectangle` with `width` and `height`. Add methods: `area()`, `perimeter()`, `is_square()`.",
    " 3. Create a class `Person` with name and age. Add a `greet()` method.",
    " 4. Create a `BankAccount` class with `deposit()`, `withdraw()`, and `get_balance()` methods.",
    " 5. Create a `Counter` class with `increment()`, `decrement()`, `reset()`, and `value` property.",
    " 6. Create a class variable `species` shared by all `Animal` instances.",
    " 7. Write a class `Converter` with static methods: `km_to_miles()`, `celsius_to_fahrenheit()`.",
    " 8. Use `__str__` and `__repr__` in a `Book` class.",
    " 9. Create a `Student` class. Use a class method `from_string()` that parses 'Name,Age,Grade'.",
    "10. Create a `Car` class with `make`, `model`, `year`. Override `__eq__` to compare by make+model+year.",
    # Constructors & Variables
    "11. Create a class with a default constructor (no parameters) that assigns default values.",
    "12. Make a class `Pizza` that allows: `Pizza('Large')` and `Pizza()` (medium by default).",
    "13. Track how many `Dog` objects are created using a class variable.",
    "14. Demonstrate that instance variables are independent across objects.",
    "15. Create a class `Temperature` with `celsius` property and computed `fahrenheit` and `kelvin` properties.",
    # Methods
    "16. Write a `Stack` class with `push`, `pop`, `peek`, `is_empty`, `size` methods.",
    "17. Implement a `Queue` class with `enqueue`, `dequeue`, `front`, `is_empty`.",
    "18. Create a `StringHelper` class with static methods: `reverse()`, `is_palindrome()`, `count_vowels()`.",
    "19. Add `__len__` and `__contains__` to a `Playlist` class.",
    "20. Create a `Logger` class with a class method that creates instances pre-configured for different log levels.",
    # Encapsulation
    "21. Create a `Person` class where `age` is protected and validated (must be 0–150).",
    "22. Implement private `__balance` in `Wallet` class; expose via `balance` property.",
    "23. Demonstrate name mangling: show how `__private` becomes `_ClassName__private`.",
    "24. Create a `Config` class where settings can be read freely but only set via `update()` method.",
    "25. Implement a `Timer` class where `start_time` is read-only after set.",
    # OOP design
    "26. Model a `TrafficLight` with states: red, yellow, green. Add a `next()` method to cycle states.",
    "27. Create a `Matrix` class supporting `+`, `-`, and `*` (scalar) operators.",
    "28. Implement `__iter__` and `__next__` in a `Range` class that mimics Python's `range()`.",
    "29. Create a `Fraction` class that simplifies fractions. Support `+`, `-`, `*`, `/`, `==`, `__str__`.",
    "30. Build a simple `Todo` list class: `add()`, `complete()`, `remove()`, `list_pending()`, `list_done()`.",
]

print("=" * 60)
print("BEGINNER OOP PRACTICE — 30 QUESTIONS")
print("=" * 60)
for q in questions:
    print(q)

print("\\nSee 02_solutions.py for complete solutions.")
'''

CODE_FILES["23_Practice/Beginner/02_solutions.py"] = '''\
"""
Beginner Solutions — selected solutions (Q1–Q10)
"""
import math

# ─── Q1: Circle ─────────────────────────────
class Circle:
    def __init__(self, radius: float) -> None:
        if radius < 0: raise ValueError("Radius must be non-negative")
        self.radius = radius
    def area(self) -> float: return math.pi * self.radius ** 2
    def circumference(self) -> float: return 2 * math.pi * self.radius
    def __repr__(self) -> str: return f"Circle(r={self.radius})"

c = Circle(5)
print(f"Q1: Circle area={c.area():.4f}")

# ─── Q2: Rectangle ──────────────────────────
class Rectangle:
    def __init__(self, w: float, h: float) -> None:
        self.width = w; self.height = h
    def area(self) -> float: return self.width * self.height
    def perimeter(self) -> float: return 2 * (self.width + self.height)
    def is_square(self) -> bool: return self.width == self.height

r = Rectangle(4, 4)
print(f"Q2: area={r.area()}, is_square={r.is_square()}")

# ─── Q3: Person ─────────────────────────────
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name; self.age = age
    def greet(self) -> str: return f"Hi, I\'m {self.name}, {self.age} years old."

print(f"Q3: {Person('Alice', 30).greet()}")

# ─── Q4: BankAccount ────────────────────────
class BankAccount:
    def __init__(self, owner: str) -> None:
        self.owner = owner; self._balance = 0.0
    def deposit(self, amount: float) -> None:
        if amount > 0: self._balance += amount
    def withdraw(self, amount: float) -> bool:
        if amount > self._balance: return False
        self._balance -= amount; return True
    def get_balance(self) -> float: return self._balance

acc = BankAccount("Bob")
acc.deposit(1000)
acc.withdraw(300)
print(f"Q4: Balance={acc.get_balance()}")

# ─── Q5: Counter ────────────────────────────
class Counter:
    def __init__(self) -> None: self._value = 0
    def increment(self, by: int = 1) -> None: self._value += by
    def decrement(self, by: int = 1) -> None: self._value -= by
    def reset(self) -> None: self._value = 0
    @property
    def value(self) -> int: return self._value

cnt = Counter()
cnt.increment(); cnt.increment(); cnt.decrement()
print(f"Q5: Counter={cnt.value}")

# ─── Q29: Fraction ───────────────────────────
from math import gcd

class Fraction:
    def __init__(self, num: int, den: int) -> None:
        if den == 0: raise ZeroDivisionError
        g = gcd(abs(num), abs(den))
        sign = -1 if den < 0 else 1
        self.num = sign * num // g
        self.den = abs(den) // g

    def __add__(self, o): return Fraction(self.num*o.den + o.num*self.den, self.den*o.den)
    def __sub__(self, o): return Fraction(self.num*o.den - o.num*self.den, self.den*o.den)
    def __mul__(self, o): return Fraction(self.num*o.num, self.den*o.den)
    def __truediv__(self, o): return Fraction(self.num*o.den, self.den*o.num)
    def __eq__(self, o): return self.num == o.num and self.den == o.den
    def __str__(self) -> str: return f"{self.num}/{self.den}" if self.den != 1 else str(self.num)
    def __repr__(self) -> str: return f"Fraction({self.num}, {self.den})"

a, b = Fraction(1, 2), Fraction(1, 3)
print(f"Q29: {a} + {b} = {a+b}, {a} * {b} = {a*b}")

# ─── Q30: Todo ───────────────────────────────
class Todo:
    def __init__(self) -> None:
        self._pending: list[str] = []
        self._done:    list[str] = []

    def add(self, task: str) -> None:
        self._pending.append(task)

    def complete(self, task: str) -> None:
        if task in self._pending:
            self._pending.remove(task)
            self._done.append(task)

    def remove(self, task: str) -> None:
        self._pending.discard if hasattr(self._pending, "discard") else None
        if task in self._pending: self._pending.remove(task)

    def list_pending(self) -> list: return list(self._pending)
    def list_done(self)    -> list: return list(self._done)

todo = Todo()
todo.add("Buy groceries"); todo.add("Read book"); todo.add("Exercise")
todo.complete("Buy groceries")
print(f"Q30: Pending={todo.list_pending()}, Done={todo.list_done()}")

print("\\n✅ Solutions complete!")
'''

CODE_FILES["23_Practice/Intermediate/01_questions.py"] = '''\
"""
Intermediate Practice — 30 OOP questions
"""
questions = [
    " 1. Implement a `LinkedList` class with `append`, `prepend`, `delete`, `search`, `__len__`, `__str__`.",
    " 2. Create a `BST` (Binary Search Tree) class with `insert`, `search`, `inorder` traversal.",
    " 3. Implement the `Observer` design pattern for a weather station.",
    " 4. Write a generic `Cache` class using `__getitem__`, `__setitem__`, with TTL (time-to-live).",
    " 5. Implement `__enter__` and `__exit__` for a `DatabaseTransaction` context manager.",
    " 6. Create a `Polynomial` class supporting `+`, `-`, `*`, evaluation at a point, `__str__`.",
    " 7. Design an `EventBus` system with subscribe/publish and priority levels.",
    " 8. Implement `Strategy` pattern for a payment processor (Credit, UPI, Wallet).",
    " 9. Create a `TypedList` descriptor that enforces element types.",
    "10. Write a `Retry` decorator class that retries a function N times on exception.",
    "11. Implement `__slots__` in a high-performance `Point3D` class. Benchmark vs normal class.",
    "12. Build a `Pipeline` class: `pipeline = Pipeline() | step1 | step2 | step3`.",
    "13. Create an `Enum`-like class manually (without using the `enum` module).",
    "14. Implement a `Memento` pattern for an undo/redo text editor.",
    "15. Write a `Proxy` pattern for lazy loading expensive objects.",
    "16. Design a `CommandPattern` for a smart home (lights, thermostat, door).",
    "17. Create a `Decorator` pattern for a text formatter (bold, italic, underline, color).",
    "18. Implement `__hash__` and `__eq__` for a custom `Email` class; use in a `set`.",
    "19. Write a metaclass `Singleton` and use it on three different classes.",
    "20. Build a `JSONSerializer` mixin that any class can inherit for serialization.",
    "21. Create a `Validated` descriptor that checks types and ranges using Python annotations.",
    "22. Implement a `Thread-safe Singleton` using a lock.",
    "23. Write a `Chain of Responsibility` for HTTP request middleware (auth, logging, rate-limit).",
    "24. Build a mini `ORM`: `Model`, `Field`, `StringField`, `IntField` with `save()`, `find()`.",
    "25. Implement a `Publisher-Subscriber` pattern with topic filtering.",
    "26. Create a `Flyweight` pattern for a game with thousands of particle objects.",
    "27. Design a `Builder` pattern for generating complex SQL queries.",
    "28. Write a `Template Method` pattern for data processing (CSV, JSON, XML).",
    "29. Implement a `State` machine for an order: placed → confirmed → shipped → delivered → cancelled.",
    "30. Build a `Composite` pattern for a file system (files and folders, `size()`, `display()`).",
]

print("=" * 60)
print("INTERMEDIATE OOP PRACTICE — 30 QUESTIONS")
print("=" * 60)
for q in questions:
    print(q)
print("\\n💡 Tip: implement one per day. Focus on clean design, not just working code.")
'''

CODE_FILES["23_Practice/Advanced/01_questions.py"] = '''\
"""
Advanced Practice — 30 OOP questions
"""
questions = [
    " 1. Write a metaclass that auto-registers all subclasses in a plugin registry.",
    " 2. Implement a `__init_subclass__` hook that validates subclass interface at class creation time.",
    " 3. Build a `Descriptor` that supports both instance and class-level access with caching.",
    " 4. Create a full `dataclass`-like decorator from scratch (without using @dataclass).",
    " 5. Implement cooperative multiple inheritance with `super()` across 6 classes.",
    " 6. Write a thread-safe `LRU Cache` using a class with `__getitem__`, `__setitem__`, `__len__`.",
    " 7. Build a `lazy property` descriptor that computes value once and caches it.",
    " 8. Implement a `Visitor` pattern for an AST (abstract syntax tree) with 5 node types.",
    " 9. Write an `Abstract Factory` for cross-platform UI widgets (Windows/Mac buttons, dialogs).",
    "10. Create a `Proxy` that logs, caches, and rate-limits method calls transparently.",
    "11. Implement Python\'s `abc.ABCMeta` functionality from scratch using metaclasses.",
    "12. Write a `__class_getitem__` that makes your class support generics: `MyClass[int]`.",
    "13. Build a `Protocol` checker that validates duck-typing at import time.",
    "14. Implement `copy.deepcopy` support in a complex object graph with circular references.",
    "15. Design a `reactive` attribute system where changes trigger callbacks (like Vue.js reactivity).",
    "16. Write a `mixin` that adds `__eq__`, `__lt__`, `__hash__` from a single `key()` method.",
    "17. Build a `SQLAlchemy`-style `Column` descriptor and `Model` base class.",
    "18. Implement `__set_name__` to auto-name form fields from class body.",
    "19. Create a full `event-sourcing` system where state is rebuilt from an event log.",
    "20. Write a `Type-safe heterogeneous container` using generics and `__class_getitem__`.",
    "21. Implement `dataclasses.field()` functionality using a custom descriptor.",
    "22. Build a `Context Variable`-based scope system (like Python\'s contextvars).",
    "23. Write a `metaclass` that makes all methods automatically thread-safe with a lock.",
    "24. Implement `__getattr__`, `__setattr__`, `__delattr__` to create a `DotDict` class.",
    "25. Build a `tracing` proxy that records every attribute access and method call.",
    "26. Design a `permission system` using descriptors and decorators.",
    "27. Implement `structural pattern matching` dispatch using `__match_args__`.",
    "28. Write a full `dependency injection container` using metaclasses and type hints.",
    "29. Build an `immutable record` type that generates `replace()` (like `dataclasses.replace`).",
    "30. Implement `Python\'s slot` mechanism from scratch using descriptors and `__new__`.",
]

print("=" * 60)
print("ADVANCED OOP PRACTICE — 30 QUESTIONS")
print("=" * 60)
for q in questions:
    print(q)
print("\\n🎓 These questions cover expert-level Python OOP. Take your time!")
'''

# ── README ────────────────────────────────────
CODE_FILES["README.md"] = '''\
# 🐍 OOPS — Complete Python Object-Oriented Programming Repository

> From absolute beginner to production-ready OOP in Python 3.12+

---

## 📚 What You Will Learn

| # | Topic | Level | Est. Time |
|---|-------|-------|-----------|
| 01 | Introduction to OOP | Beginner | 2h |
| 02 | Classes and Objects | Beginner | 3h |
| 03 | Constructors | Beginner | 2h |
| 04 | Instance & Class Variables | Beginner | 2h |
| 05 | Methods | Beginner | 2h |
| 06 | Encapsulation | Beginner | 3h |
| 07 | Abstraction | Beginner | 2h |
| 08 | Inheritance | Intermediate | 4h |
| 09 | Polymorphism | Intermediate | 3h |
| 10 | Special (Dunder) Methods | Intermediate | 4h |
| 11 | Property & Descriptors | Intermediate | 3h |
| 12 | Static & Class Methods | Beginner | 2h |
| 13 | Composition & Aggregation | Intermediate | 3h |
| 14 | Multiple Inheritance | Intermediate | 3h |
| 15 | Method Resolution Order | Intermediate | 2h |
| 16 | Abstract Base Classes | Intermediate | 3h |
| 17 | Data Classes | Intermediate | 2h |
| 18 | Type Hints | Intermediate | 3h |
| 19 | Design Principles (SOLID) | Advanced | 5h |
| 20 | Design Patterns | Advanced | 10h |
| 21 | Real-World Projects | Advanced | 15h |
| 22 | Interview Preparation | All Levels | 6h |
| 23 | Practice Exercises | All Levels | 20h |

**Total Estimated Time: ~95 hours** (study + practice)

---

## 🗺️ Learning Roadmap

```
Phase 1 — FOUNDATION (Week 1-2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
01 Introduction → 02 Classes → 03 Constructors
→ 04 Variables → 05 Methods → 12 Static/Class Methods

Phase 2 — FOUR PILLARS (Week 3-4)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
06 Encapsulation → 07 Abstraction
→ 08 Inheritance → 09 Polymorphism

Phase 3 — PYTHON-SPECIFIC (Week 5-6)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
10 Dunder Methods → 11 Properties & Descriptors
→ 13 Composition → 14 Multiple Inheritance
→ 15 MRO → 16 ABC → 17 Data Classes → 18 Type Hints

Phase 4 — DESIGN & ARCHITECTURE (Week 7-9)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
19 SOLID → 20 Design Patterns

Phase 5 — APPLICATION (Week 10-12)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
21 Real Projects → 22 Interview Prep → 23 Practice
```

---

## ✅ Progress Checklist

### Foundation
- [ ] Understand OOP vs procedural
- [ ] Create classes with attributes and methods
- [ ] Understand `self`, `cls`, and static methods
- [ ] Work with `__init__` and constructor overloading
- [ ] Differentiate instance vs class variables

### Pillars
- [ ] Implement encapsulation with `@property`
- [ ] Create abstract classes with `ABC`
- [ ] Write inheritance hierarchies (single, multi, hybrid)
- [ ] Use polymorphism with duck typing

### Python OOP
- [ ] Implement 10+ dunder methods from memory
- [ ] Write custom descriptors
- [ ] Handle MRO and `super()` correctly
- [ ] Build data classes and type-annotated code

### Design
- [ ] Apply all 5 SOLID principles
- [ ] Implement Singleton, Factory, Builder, Observer, Strategy
- [ ] Know when NOT to use design patterns

### Application
- [ ] Complete all 3 real-world projects
- [ ] Solve 30 beginner + 30 intermediate + 30 advanced exercises
- [ ] Answer 100 interview questions confidently

---

## 📋 Prerequisites

- Python 3.8+ (repo uses 3.12 features)
- Basic Python: variables, loops, functions, lists, dicts
- Recommended: `python -m venv oops_env && pip install -r requirements.txt`

---

## 🗂️ Folder Structure

```
OOPS/
├── README.md                         ← You are here
├── 01_Introduction/
│   ├── OOP_Introduction.pdf          ← Theory notes
│   └── code_examples/                ← Runnable Python files
│       ├── 01_basic.py
│       ├── 02_intermediate.py
│       ├── 03_real_world.py
│       ├── 04_common_mistakes.py
│       └── 05_best_practices.py
├── 02_Classes_and_Objects/ ...       ← Same structure for each topic
...
├── 21_Real_World_Projects/
│   ├── Project_1_Library/            ← Library Management System
│   ├── Project_2_Bank/               ← Bank Management System
│   └── Project_3_Hospital/           ← Hospital Management System
├── 22_Interview_Preparation/
│   └── code_examples/01_tricky.py    ← Tricky interview questions
└── 23_Practice/
    ├── Beginner/     ← 30 questions + solutions
    ├── Intermediate/ ← 30 questions
    └── Advanced/     ← 30 questions
```

---

## 🎯 How To Use This Repository

1. **Read the PDF** for each topic first (theory + diagrams)
2. **Run `01_basic.py`** and understand every line
3. **Progress through** `02_intermediate.py` → `03_real_world.py`
4. **Study `04_common_mistakes.py`** — avoid these pitfalls
5. **Apply `05_best_practices.py`** — write production-quality code
6. **Solve practice questions** after each phase
7. **Build the projects** to solidify everything

---

## 📖 Recommended Resources

- [Python Official Docs — Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Real Python — OOP](https://realpython.com/python3-object-oriented-programming/)
- [Python Design Patterns](https://refactoring.guru/design-patterns/python)
- [Fluent Python — Luciano Ramalho](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)

---

## 🧑‍💻 Author & License

Built with ❤️ for Python learners worldwide.  
MIT License — free to use, share, and adapt.
'''

def write_code_files():
    for rel_path, content in CODE_FILES.items():
        full_path = os.path.join(BASE, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
    print(f"✅ {len(CODE_FILES)} code/doc files written.")

if __name__ == "__main__":
    make_dirs()
    write_code_files()
    print("✅ Phase 1 complete: directories + code files created.")
