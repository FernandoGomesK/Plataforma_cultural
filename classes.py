from typing import List
from datetime import date

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
        self._managed_events = List['Event']
        self._sold_events = List['Ticket']
        super().__init__(name, cpf, age, adress)
    
    def authenticate():
        pass
    
    def register_sale(ticket:Ticket):
        pass
    
    def list_available_events():
        pass
        
class Participant(Person):
    def __init__(self, name, cpf, age, adress, tickets):
        super().__init__(name, cpf, age, adress)
        self.tickets = List["Ticket"]
    
    def authentiicate():
        pass

    def write_review():
        pass
    
    

class Organizer(Person):
    def __init__(self, name, cpf, age, adress, role: str):
        self._role = role
        super().__init__(name, cpf, age, adress)
    
    def request_event():
        pass
    
    def autentheticate():
        pass
    
class Worker(Person):
    def __init__(self):
        pass

class Event:
    def __init__(self, name: str, type:str, description:str, start_date:date, end_date:date, organizer:Organizer, total_tickets:int,
                 remaining_tickets: int, transactions: List['Transactions'], review: List['Review']):
        self._name = name
        self._type = type
        self._description = description
        self.start_date = start_date # inserir dia inicial via biblioteca datetime
        self.end_date = end_date # inserir dia final ''   '' ''
        self._organizer = organizer
        self._total_tickets = total_tickets
        self._remaining_tickets = remaining_tickets
        self._transactions = transactions
        self.review = review
        

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, value):
        self.start_date = value

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, value):
        self.end_date = value

    @property
    def organizer(self):
        return self._organizer

    @organizer.setter
    def organizer(self, value):
        self._organizer = value

    @property
    def total_tickets(self):
        return self._total_tickets

    @total_tickets.setter
    def total_tickets(self, value):
        self._total_tickets = value

    @property
    def remaining_tickets(self):
        return self._remaining_tickets

    @remaining_tickets.setter
    def remaining_tickets(self, value):
        self._remaining_tickets = value

    @property
    def transactions(self):
        return self._transactions

    @transactions.setter
    def transactions(self, value):
        self._transactions = value

    def get_review(self):
        return self.review

    def set_review(self, value):
        self.review = value
