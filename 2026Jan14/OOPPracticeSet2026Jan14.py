import random

# easy level
# Q3
print("----------Q3 Game Character----------")
class GameCharacter:
    def __init__(self, name, health = 100): # usually a characters' health is 100
        self.name = name
        self.health = health

    def take_damage(self, amount):
        if amount > self.health:
            self.health = 0
        else:
            self.health -= amount
        print(f"{self.name} has taken {amount} damage, {self.health} health left.")

    def heal(self, amount):
        if self.health + amount > 100:
            self.health = 100
        else:
            self.health += amount
        print(f"{self.name} has heal {amount} health, {self.health} health left.")

testCharacter = GameCharacter("Justin")
testCharacter.take_damage(50)
testCharacter.heal(40)

# medium level
# Q6
print()
print("----------Q6 Teacher and Student Interaction----------")
class Student:
    def __init__(self, grade):
        self.grade = grade

    def view_grade(self):
        print(f"Your grade is {self.grade}")

class Teacher:
    def __init__(self, name):
        self.name = name

    def assign_grade(self, student, grade):
        student.grade = 100
        print(f"The student has assigned {grade} on his/her assignment")

teacher1 = Teacher("T1")
student1 = Student(0)
student1.view_grade()
teacher1.assign_grade(student1, 100)
student1.view_grade()

# hard level
# Q9
print()
print("----------Q9 Mini Game - Character Battle----------")
class Character:
    def __init__(self, name, health, attack_power, critical_hits = 0.15, defense_points = 0.15):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.critical_hits = critical_hits
        self.defense_points = defense_points

    def attack(self, other_character):
        x = random.random()
        i = random.random()
        if x < other_character.defense_points:
            print(f"{self.name} attacked {other_character.name}, but {other_character.name} dodged it! {other_character.name} has taken 0 damage")
        elif i < self.critical_hits:
            other_character.health -= 2 * self.attack_power
            print(f"{self.name} attacked {other_character.name}, critical hits! {other_character.name} has taken {2 * self.attack_power} damage")
        else:
            other_character.health -= self.attack_power
            print(f"{self.name} attacked {other_character.name}, {other_character.name} has taken {self.attack_power} damage")

    def is_alive(self):
        if self.health > 0:
            print(f"{self.name} is alive")
            return True
        else:
            print(f"{self.name} is not alive. Game Over!")
            return False

C1 = Character("Justin", 100, 8)
C2 = Character("Victor", 100, 7)
turn = 1
while True:
    print(f"----Turn{turn}----")
    C1.attack(C2)
    y = C2.is_alive()
    if not y:
        break

    C2.attack(C1)
    y = C1.is_alive()
    if not y:
        break

    turn += 1
