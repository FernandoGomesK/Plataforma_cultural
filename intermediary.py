from person import Person
from ticket import Ticket
from event import Event


class Intermediary(Person):
    def __init__(self, name: str, cpf: str, age: str, adress: str):
        self._managed_events: list[Event] = []
        self._sold_events: list[Ticket] = []
        super().__init__(name, cpf, age, adress)

    def authenticate(self, password: str) -> bool:
        pass

    def register_sale(ticket: "Ticket"):
        pass

    def list_available_events():
        pass
