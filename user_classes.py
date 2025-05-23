from dataclasses import dataclass
from typing import List
from ticket import Ticket


@dataclass
class Person:
    name: str
    cpf: str
    age: str
    email: str
    
class User(Person):
    def __init__(self, name: str, cpf: str, age: str, email: str,username: str, password: str):
        super().__init__(name, cpf, age, email)
        self.username = username
        self.password = password
        self.tickets: List[Ticket] = []
        
    def verify_password(self, password: str) -> bool:
        return self.password == password
        
class Organizer(Person):
    def __init__(self, name: str, cpf: str, age: str, email: str, password: str, admin: bool = True):
        super().__init__(name, cpf, age, email)
        self.password = password
        self.admin = admin
        self.tickets: List[Ticket] = []
        
    def verify_password(self, password: str) -> bool:
        return self.password == password
        
        
class Intermediary(Person):
    def __init__(self, name: str, cpf: str, age: str, email: str, password: str, admin: bool = True):
        super().__init__(name, cpf, age, email)
        self.password = password
        self.admin = admin
        self.tickets: List[Ticket] = []
        
    def verify_password(self, password: str) -> bool:
        return self.password == password