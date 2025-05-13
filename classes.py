class Person:
    def __init__(self, name:str, cpf:str, age:str, adress:str):
        self._name = name
        self._cpf = cpf
        self._age = age 
        self._adress = adress

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def adress(self):
        return self._adress

    @adress.setter
    def adress(self, value):
        self._adress = value
        
class Intermediary(Person):
    def __init__(self, name, cpf, age, adress):
        super().__init__(name, cpf, age, adress)
    
class Worker(Person):
    def __init__(self):
        pass
    
class Staff(Person):
    def __init__(self):
        pass
    
class Participant(Person):
    def __init__(self):
        super().__init__()
