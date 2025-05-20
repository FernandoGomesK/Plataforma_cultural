from person import Person
from typing import List, Optional
from ticket import Ticket
from event import Event


class Intermediary(Person):
    def __init__(self, name: str, cpf: str, age: str, address: str):
        super().__init__(name, cpf, age, address)
        self._managed_events: List[Event] = []
        self._sold_tickets: List[Ticket] = []

    @property
    def managed_events(self) -> List[Event]:
        return self._managed_events

    @property
    def sold_tickets(self) -> List[Ticket]:
        return self._sold_tickets

    def authenticate(self) -> bool:
        return True

    def register_sale(self, ticket: Ticket) -> None:
        self._sold_tickets.append(ticket)

    def list_available_events(self) -> List[Event]:
        return [event for event in self._managed_events if event.remaining_tickets > 0]
