from person import Person
from typing import List


class Participant(Person):
    def __init__(self, name, cpf, age, adress, tickets):
        super().__init__(name, cpf, age, adress)
        self.tickets = List["Ticket"]
    
    def authentiicate():
        pass

    def write_review():
        pass