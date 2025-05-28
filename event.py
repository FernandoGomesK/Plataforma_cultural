from typing import List, TYPE_CHECKING
from datetime import date
import uuid

# To handle circular dependencies for type hinting if Review or Ticket import Event
if TYPE_CHECKING:
    from review import Review
    from ticket import Ticket
    from transaction import Transaction
    from participant import (
        Participant,
    )


class Event:
    def __init__(
        self,
        name: str,
        event_type: str,
        description: str,
        start_date: date,
        end_date: date,
        organizer_id: str,
        total_tickets: int,
    ):
        self._event_id = str(uuid.uuid4())
        self._name = name
        self._event_type = event_type
        self._description = description
        self._start_date = start_date
        self._end_date = end_date
        self._organizer_id = organizer_id
        self._total_tickets = total_tickets
        self._remaining_tickets = total_tickets
        self._reviews: List["Review"] = []  # Stores Review objects as per aggregation

    @property
    def event_id(self) -> str:
        return self._event_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def event_type(self) -> str:
        return self._event_type

    @event_type.setter
    def event_type(self, value: str):
        self._event_type = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def start_date(self) -> date:
        return self._start_date

    @start_date.setter
    def start_date(self, value: date):
        self._start_date = value

    @property
    def end_date(self) -> date:
        return self._end_date

    @end_date.setter
    def end_date(self, value: date):
        self._end_date = value

    @property
    def organizer_id(self) -> str:
        return self._organizer_id

    @organizer_id.setter
    def organizer_id(self, value: str):  # Assuming CPF of the organizer
        self._organizer_id = value

    @property
    def total_tickets(self) -> int:
        return self._total_tickets

    @total_tickets.setter
    def total_tickets(self, value: int):
        self._total_tickets = value

    @property
    def remaining_tickets(self) -> int:
        return self._remaining_tickets

    @remaining_tickets.setter
    def remaining_tickets(self, value: int):
        self._remaining_tickets = value

    @property
    def reviews(self) -> List["Review"]:
        return self._reviews

    def add_review(self, review: "Review") -> None:
        self._reviews.append(review)

    def sell_ticket(
        self,
        participant_id: str,
        ticket_type: str,
        price: float,
        transaction_id: str,
    ) -> "Ticket":
        # Import Ticket locally to avoid circular import issues at module level
        from ticket import Ticket

        if self._remaining_tickets <= 0:
            raise Exception("Ingressos esgotados.")

        ticket = Ticket(
            event_id=self._event_id,
            owner_id=participant_id,
            purchase_date=date.today(),
            ticket_id=str(uuid.uuid4()),  # Ticket generates its own ID
            price=price,
            ticket_type=ticket_type,
            is_active=True,
            transaction_id=transaction_id,
        )

        self._remaining_tickets -= 1
        return ticket
