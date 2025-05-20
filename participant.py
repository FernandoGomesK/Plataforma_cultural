from person import Person
from ticket import Ticket
from event import Event

class Participant(Person):
    def __init__(self, name: str, cpf: str, age: int, address: str, ticket: Ticket | None = None) -> None:
        super().__init__(name, cpf, age, address)
        self.tickets: list[Ticket] = [] 
        if ticket:
            self.tickets.append(ticket)
    
    def authenticate(self, password: str) -> bool:  
        pass
    
    def write_review(self, event: 'Event', comment: str, rating: int) -> None:
        pass