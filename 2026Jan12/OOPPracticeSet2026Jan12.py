# easy level
# Q1 Student Class
print("----------Q1 Student Class----------")
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am in grade {self.grade}.")

student1 = Student("Justin", 12)
student2 = Student("Victor", 12)
student1.introduce()
student2.introduce()

# Q2
print()
print("----------Q2 Rectangle Class----------")
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"The area of this rectangle is", (self.length*self.width))

    def perimeter(self):
        print(f"The perimeter of this rectangle is", (2* (self.length+self.width)))

testRect = Rectangle(4, 5)
testRect.area()
testRect.perimeter()

# Medium Level
# Q4
print()
print("----------Q4 Bank Account----------")
class BankAccount:
    def __init__(self, _balance):
        self._balance = _balance

    def deposit(self, amount):
        if amount >= 0:
            self._balance += amount
        else:
            print("Cannot deposit negative values!")
            return
        print(f"Success! You have deposit ${amount} into your account, now you have ${self._balance} in your account.")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
            return
        else:
            self._balance -= amount
        print(f"Success! You have withdraw ${amount} out from your account, now you have ${self._balance} in your account.")

    def get_balance(self):
        print(f"You have ${self._balance} in your account")

testAccount = BankAccount(0)
print("trying to deposit $-1000 into the account (should not be execute because it is a negative number)")
testAccount.deposit(-1000)
print("trying to deposit $1000 into the account")
testAccount.deposit(1000)
print("trying to withdraw $1200 out from the account (should not be execute because 1000<1200)")
testAccount.withdraw(1200)
print("trying to withdraw $900 out from the account")
testAccount.withdraw(900)
print("get the balance (should have $100 because 1000-900=100)")
testAccount.get_balance()

# Q5
print()
print("----------Q5 User Account----------")
class UserAccount:
    def __init__(self, _password):
        self._password = _password

    def login(self, password):
        if password == self._password:
            print("Login Success!")
        else:
            print("Incorrect Password!")

    def change_password(self, old_password, new_password):
        if old_password == self._password:
            self._password = new_password
            print(f"Success! Password has being changed to \"{self._password}\"")
        else:
            print("Incorrect Password!")

testUser = UserAccount("0000")
print("should be wrong this time")
testUser.login("0101")
print("should be correct this time")
testUser.login("0000")
print("should be wrong this time")
testUser.change_password("0202", "0101")
print("should be correct this time")
testUser.change_password("0000", "0101")

# Hard Level
# Q7
print()
print("----------Q7 School Management System----------")
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id

class School:
    def __init__(self, students): # the student here should be a list
        self.students = students

    def add_student(self, student):
        for stu in self.students:
            if stu.get_student_id() == student.get_student_id():
                print("Error, duplicate student ID")
                return
        self.students.append(student)

    def remove_student(self, name):
        for i in range(0, len(self.students)):
            if name == self.students[i].get_name():
                self.students.pop(i)
                return
        print("Student not found")

    def list_students(self):
        print("Student list: ")
        for stu in self.students:
            print(stu.get_name())

student_list = []
NGS = School(student_list)

print("adding 6 student into the test...")
NGS.add_student(Student("Victor", "0000"))
NGS.add_student(Student("Justin", "0001"))
NGS.add_student(Student("Stu3", "0002"))
NGS.add_student(Student("Stu4", "0003"))
NGS.add_student(Student("Stu5", "0004"))
NGS.add_student(Student("Stu6", "0005"))
NGS.list_students()
print()
print("remove Victor from the school")
NGS.remove_student("Victor")
print("should be no Victor in the list below: ")
NGS.list_students()

# Q8
print()
print("----------Q8 Inventory System----------")
class Product:
    def __init__(self, _name, _price, _quantity):
        if _price < 0:
            print("Price must not be negative! The price is automatically set into $0")
        if _quantity < 0:
            print("Stock must not be negative! The quantity is automatically set into 0")
        self._name = _name
        self._price = max(0, _price)
        self._quantity = _quantity

    def sell(self, amount):
        if amount > self._quantity:
            print("Insufficient stock")
        else:
            self._quantity -= amount
            print("sell success")

    def restock(self, amount):
        if amount < 0:
            print("You can not restock a negative number")
        else:
            self._quantity += amount
            print(f"Success! You have restocked {amount} of {self._name}")


    def get_product_info(self):
        print(f"\"{self._name}\" | ${self._price} | Stock: {self._quantity} ")

print("price should not set to 0 test")
testProduct = Product("G309", -10, 10)
print("price set to 99.99")
testProduct = Product("G309", 99.99, 10)
print("sell more than available test")
testProduct.sell(12)
print("sell test")
testProduct.sell(5)
print("restock test")
testProduct.restock(10)
print("get product info: ")
testProduct.get_product_info()
