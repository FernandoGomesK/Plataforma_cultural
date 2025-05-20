from typing import List
from datetime import date
from organizer import Organizer
from review import Review
from ticket import Ticket
from participant import Participant
from transaction import Transaction
import uuid


class Event:
    def __init__(
        self,
        name: str,
        type: str,
        description: str,
        start_date: date,
        end_date: date,
        organizer: Organizer,
        total_tickets: int,
    ):
        self._name = name
        self._type = type
        self._description = description
        self._start_date = start_date
        self._end_date = end_date
        self._organizer = organizer
        self._total_tickets = total_tickets
        self._remaining_tickets = total_tickets
        self._reviews: List[Review] = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value: date):
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value: date):
        self._end_date = value

    @property
    def organizer(self):
        return self._organizer

    @organizer.setter
    def organizer(self, value: Organizer):
        self._organizer = value

    @property
    def total_tickets(self):
        return self._total_tickets

    @total_tickets.setter
    def total_tickets(self, value):
        self._total_tickets = value

    @property
    def remaining_tickets(self):
        return self._remaining_tickets

    @remaining_tickets.setter
    def remaining_tickets(self, value):
        self._remaining_tickets = value

    @property
    def reviews(self):
        return self._reviews

    def add_review(self, review: Review):
        self._reviews.append(review)

    def sell_ticket(
        self,
        participant: Participant,
        ticket_type: str,
        price: float,
        transaction: Transaction,
    ) -> Ticket:
        if self._remaining_tickets <= 0:
            raise Exception("Ingressos esgotados.")

        ticket = Ticket(
            event=self,
            owner=participant,
            purchase_date=date.today(),
            ticket_id=str(uuid.uuid4()),
            price=price,
            ticket_type=ticket_type,
            is_active=True,
            transaction=transaction,
        )

        self._remaining_tickets -= 1
        return ticket
