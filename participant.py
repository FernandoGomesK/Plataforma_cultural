from person import Person
from event import Event
from transaction import Transaction
from ticket import Ticket
from review import Review
from datetime import date
from typing import List
import uuid


class Participant(Person):
    def __init__(self, name, cpf, age, address):
        super().__init__(name, cpf, age, address)
        self.tickets: List[Ticket] = []

    @property
    def tickets(self):
        return self._tickets

    def authenticate(self) -> bool:
        return True

    def write_review(self, event: Event, rating: int, comment: str) -> Review:
        review = Review(
            review_id=str(uuid.uuid4()),
            reviewer=self,
            rating=rating,
            comment=comment,
            review_date=date.today(),
        )
        event.add_review(review)
        return review

    def buy_ticket(
        self,
        event: Event,
        ticket_type: str,
        quantity: int,
        price: float,
        payment_method: str,
    ) -> List[Ticket]:

        tickets: List[Ticket] = []
        for _ in range(quantity):
            if event.remaining_tickets <= 0:
                raise Exception("Ingressos esgotados.")
            transaction = Transaction(
                transaction_id=str(uuid.uuid4()),
                value=price,
                payment_method=payment_method,
                tickets=[],
                buyer=self,
                event=event,
            )
            ticket = event.sell_ticket(self, ticket_type, price, transaction)
            transaction._tickets.append(ticket)
            self.tickets.append(ticket)
            tickets.append(ticket)
        return tickets
