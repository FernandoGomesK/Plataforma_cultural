from datetime import datetime
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from ticket import Ticket

class Transaction:
    def __init__(
        self,
        transaction_id: str,
        value: float,
        payment_method: str,
        buyer_id: str,
        event_id: str,
    ):
        self._transaction_id = transaction_id
        self._value = value
        self._payment_method = payment_method
        self._tickets: List["Ticket"] = []  # Stores actual Ticket objects
        self._buyer_id = buyer_id
        self._event_id = event_id
        self._transaction_date = datetime.now()
        self._status = "pending"  # e.g., pending, completed, failed, refunded

    @property
    def transaction_id(self) -> str:
        return self._transaction_id

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, val: float):
        self._value = val

    @property
    def payment_method(self) -> str:
        return self._payment_method

    @payment_method.setter
    def payment_method(self, val: str):
        self._payment_method = val

    @property
    def transaction_date(self) -> datetime:
        return self._transaction_date

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str):
        self._status = value

    @property
    def tickets(self) -> List["Ticket"]:
        return self._tickets

    # Method to add tickets to the transaction
    def add_ticket(self, ticket: "Ticket"):
        if ticket.transaction_id != self._transaction_id:
            raise ValueError("Ticket's transaction ID does not match this transaction.")
        self._tickets.append(ticket)

    @property
    def buyer_id(self) -> str:  # Participant's CPF
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value: str):
        self._buyer_id = value

    @property
    def event_id(self) -> str:
        return self._event_id

    @event_id.setter
    def event_id(self, value: str):
        self._event_id = value

    def show_transaction(self) -> str:
        ticket_ids_str = ", ".join([ticket.ticket_id for ticket in self._tickets])
        return (
            f"Transaction ID: {self._transaction_id}\n"
            f"Event ID: {self._event_id}\n"
            f"Buyer ID (CPF): {self._buyer_id}\n"
            f"Value: R${self._value:.2f}\n"
            f"Payment Method: {self._payment_method}\n"
            f"Date: {self._transaction_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Status: {self._status}\n"
            f"Tickets: [{ticket_ids_str}]"
        )
