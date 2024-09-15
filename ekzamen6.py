# # EXAM FOR WEEK 6

# ## KEEP IN MIND: YOU ARE DOING THIS FOR YOUR BRIGHT FUTURE, SO GIVE YOUR 120%!
# ## ПОМНИТЕ: ВЫ ДЕЛАЕТЕ ЭТО ДЛЯ СВОЕГО СВЕТЛОГО БУДУЩЕГО, ПОЭТОМУ ВЫКЛАДЫВАЙТЕСЬ НА ВСЕ СВОИ 120%!

# ## RULES:
# > No interner, no help to each other!

# > Make one file and place all your work there (e.g. ubaydov_ahmad.py)

# > Send the file at 

# > You have 2 hours only

# ### 1 Question
# Create a class Employee with a public attribute name, a protected attribute _salary, and a private attribute __id. Demonstrate how these are accessed and restricted.

# Создайте класс Employee с публичным атрибутом name, защищенным атрибутом _salary и закрытым атрибутом __id. Покажите, как они доступны и ограничены.

# class Employee:
#     name="Alijon"
#     _salary=1000
#     __id=1234
#     @classmethod
#     def show(cls):
#         print(cls.name,cls._salary,cls.__id)
# obj1=Employee()
# obj1.show()
# obj1._salary=2000
# obj1.__id=4321
# obj1.show()

# ### 2 Question
# Create a class BankAccount with private attributes _balance and __pin.
# Initialize the values in the constructor.
# Access the _balance directly and see what happens when you try to access __pin.

# Создайте класс BankAccount с приватными атрибутами _balance и __pin.
# Инициализируйте значения в конструкторе.
# Получите доступ к _balance напрямую и посмотрите, что произойдет, когда вы попытаетесь получить доступ к __pin.

# class BankAccount:
#     _balance=1000
#     __pin=1234
#     def __init__(self,_balance,__pin):
#         self._balance=_balance
#         self.__pin=__pin
#     def show(self):
#         print(self._balance,self.__pin)
# obj1=BankAccount(int(input()),int(input()))
# obj1.show()

# ### 3 Question
# a) In the same BankAccount class, define a setter method to update the private attribute _balance.
# Ensure that balance can’t be negative by checking in the setter.
# В том же классе BankAccount определите метод-сеттер для обновления частного атрибута _balance.
# Убедитесь, что баланс не может быть отрицательным, проверив в сеттере.

# b) Create a class Employee with an instance attribute name and a class attribute company.
# Create two objects and modify the company class attribute. Print the result to observe the behavior.
# Создайте класс Employee с атрибутом экземпляра name и атрибутом класса company.
# Создайте два объекта и измените атрибут класса company. Распечатайте результат, чтобы понаблюдать за поведением.

# class Employee:
#     company="Softclub"
#     def __init__(self,name):
#         self.name=name
#     def show(cls):
#         print(cls.company)
# obj1=Employee(input())
# obj2=Employee(input())
# obj1.company="Google"
# obj2.company="Google"
# obj1.show()
# obj2.show()

# ### 4 Question
# Create a base class Animal with a method speak().
# Create a derived class Dog that overrides speak().
# Further, derive a class Puppy from Dog and override the speak() method again.
# Call the speak() method from a Puppy object.

# Создайте базовый класс Animal с методом speak().
# Создайте производный класс Dog, который переопределяет speak().
# Далее, выведите класс Puppy из Dog и снова переопределите метод speak().
# Вызовите метод speak() из объекта Puppy.

# class Animal:
#     def speak():
#         pass
# class Dog(Animal):
#     def speak():
#         print("Hello ")
# class Puppy(Dog):
#     def speak():
#         print("World")
# obj1=Puppy()

# ### 5 Question
# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age. Use incapsulation methods as well. / Напишите программу на Python для создания класса человека. Включите такие атрибуты, как имя, страна и дата рождения. Реализуйте метод определения возраста человека. Также используйте методы инкапсуляции.

# class Person:
#     name="Alijon"
#     country="Hisor"
#     date=2004
#     def __init__(self,__age):
#         self.__age=__age
#     def show(self):
#         print(self.name,self.country,self.date,self.__age)
# obj1=Person(int(input()))
# obj1.show()
    

# ### 6 Question
# Build a Nobel class. An instance is already created for you and instance attributes are included inside the print. Take those clues and try to reverse engineer the class.  Implement string representation of a class object using str method inside the class.

# Создайте Nobel класс. Экземпляр уже создан для вас, и атрибуты экземпляра включены в результат print. Воспользуйтесь этими подсказками и попытайтесь спроектировать класс. Реализуйте строковое представление объекта класса, используя метод str внутри класса.
# ```
# class Nobel:
#     pass

# np2005=Nobel("Peace", 2005, "Muhammad Yunus")
# print(np2005.category, np2005.year, np2005.winner)
# ```

# ### 7 Question
# Create a function which returns "upper" if all the letters in a word are uppercase, "lower" if lowercase and "mixed" for any mix of the two.
# Создайте функцию, которая возвращает «верхнюю», если все буквы в слове прописные, «нижнюю», если строчные, и «смешанную» для любого сочетания   этих двух букв.

# getCase("whisper...") ➞ "lower"

# getCase("SHOUT!") ➞ "upper"

# ### 8 Question
# The Fibonacci sequence is defined as follows: φ0=1, φ1=1, φn=φn-1+φn-2 for n>1. The beginning of the Fibonacci series looks like this: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Write a function int phi(int n) (C/C++), function phi (n:integer ): integer, (Pascal), which, given a natural number n, returns φn.

# Последовательность Фибоначчи определена следующим образом: φ0=1, φ1=1, φn=φn-1+φn-2 при n>1. Начало ряда Фибоначчи выглядит следующим образом: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Напишите функцию int phi(int n) (C/C++), function phi (n:integer): integer, (Pascal), которая по данному натуральному n возвращает φn.

# # input 
# 3
# # output
# 3



# ### 9 Question
# Print the following pattern.(Распечатайте следующий шаблон.)
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6
# 7 7 7
# 8 8
# 9



# ### 10
# Create a function which takes a list of objects from the class IceCream and returns the sweetness value of the sweetest ice cream. Note that there is a class provided for you in the Tests tab.
# Each sprinkle has a sweetness value of 1
# Check below for the sweetness values of the different flavors.
# Создайте функцию, которая берет список объектов класса IceCream и возвращает значение сладости самого сладкого мороженого. Обратите внимание, что на вкладке «Тесты» вам предоставлен класс.
# Каждая посыпка имеет показатель сладости 1.
# Ниже приведены значения сладости различных вкусов.
 
#   class IceCream:
#           def __init__(self, flavor, num_sprinkles):
#               self.flavor = flavor
#               self.num_sprinkles = num_sprinkles

#  Flavors	        |Sweetness Value    |
#  -------------------|-------------------|
#  Plain	            |   0               |
#  Vanilla	        |   5               |
#  ChocolateChip	    |   5               |
#  Strawberry         |   10              |
#  Chocolate	        |   10              |   
#  ---------------------------------------|
 
# ice1 = IceCream("Chocolate", 13)         # value of 23
# ice2 = IceCream("Vanilla", 0)           # value of 5

# sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) ➞ 23
# sweetest_icecream([ice3, ice1]) ➞ 23