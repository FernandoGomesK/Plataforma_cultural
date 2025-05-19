from person import Person
from typing import List
from ticket import Ticket
from event import Event
class Intermediary(Person):
    def __init__(self, name, cpf, age, adress):
        self._managed_events = List['Event']
        self._sold_events = List['Ticket']
        super().__init__(name, cpf, age, adress)
    
    def authenticate():
        pass
    
    def register_sale(ticket:'Ticket'):
        pass
    
    def list_available_events():
        pass