from dataclasses import dataclass
from typing import List
from ticket import Ticket
from abc import ABC, abstractmethod


@dataclass
class Person(ABC):
    name: str
    cpf: str
    age: str
    email: str
    
    def to_dict_base(self):
        return {
            "user_type" : self.__class__.__name__,
            "name": self.name,
            "cpf": self.cpf,
            "age": self.age,
            "email": self.email
        }
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Base_User(Person, ABC):
    def __init__(self, name: str, cpf: str, age: str, email: str, username: str, password: str, admin: bool = False):
        super().__init__(name, cpf, age, email)
        self.username = username
        self.password = password   
        self.admin = admin
        self.tickets: List[Ticket] = []
    
    def to_dict(self):
        data = super().to_dict_base()
        data.update({
            "username": self.username,
            "password": self.password,
            "admin": self.admin,
            "tickets": [t.to_dict() for t in self.tickets]
        })
        return data
    def verify_password(self, password: str) -> bool:
        return self.password == password
    
    def buy_ticket(self, ticket: Ticket):
        ticket.mark_as_sold()
        self.tickets.append(ticket)
        return ticket
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class User(Base_User):
    def __init__(self, name: str, cpf: str, age: str, email: str,username: str, password: str, admin: bool = False):
        super().__init__(name, cpf, age, email, username, password, admin)
                 
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Organizer(Base_User):
    def __init__(self, name: str, cpf: str, age: str, email: str, username:str, password: str, admin: bool = True):
        super().__init__(name, cpf, age, email, username, password, admin)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    
class Intermediary(Base_User):
    def __init__(self, name: str, cpf: str, age: str, email: str, username:str, password: str, admin: bool = True):
        super().__init__(name, cpf, age, email, username, password, admin)
        
    def sell_tickets(self, ticket: Ticket):
        ticket.mark_as_sold
        return ticket

    