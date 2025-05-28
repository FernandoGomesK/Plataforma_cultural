from person import Person
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from ticket import (
        Ticket,
    )
    from event import Event


class Intermediary(Person):
    def __init__(self, name: str, cpf: str, age: str, address: str):
        super().__init__(name, cpf, age, address)
        self._managed_event_ids: List[str] = []  # Stores Event IDs
        self._sold_ticket_ids: List[str] = []  # Stores Ticket IDs

    @property
    def managed_event_ids(self) -> List[str]:
        return self._managed_event_ids

    # Method to add a managed event by ID
    def add_managed_event(self, event_id: str) -> None:
        if event_id not in self._managed_event_ids:
            self._managed_event_ids.append(event_id)

    @property
    def sold_ticket_ids(self) -> List[str]:
        return self._sold_ticket_ids

    def authenticate(self) -> bool:
        print(f"Authenticating intermediary: {self.name}")
        return True

    def register_sale(self, ticket_id: str) -> None:
        self._sold_ticket_ids.append(ticket_id)
        print(f"Intermediary {self.name} registered sale of ticket ID: {ticket_id}.")

    def list_available_events(self, all_events: Dict[str, "Event"]) -> List["Event"]:
        """
        Lists available events from the managed events.
        Requires a dictionary of all event objects (event_id -> Event object)
        to access their details (like remaining_tickets).
        """
        available_events: List["Event"] = []
        for event_id in self._managed_event_ids:
            event = all_events.get(event_id)
            if event and event.remaining_tickets > 0:
                available_events.append(event)
        return available_events
