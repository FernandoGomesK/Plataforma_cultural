from datetime import datetime
from typing import List
from ticket import Ticket
from participant import Participant
from event import Event

class Transactions:
    def __init__(self, transaction_id: str, 
                 value: float, 
                 payment_method: str,
                 tickets: List[Ticket],
                 buyer: Participant,
                 event: Event):
        
        self._transaction_id = transaction_id
        self._value = value
        self._payment_method = payment_method
        
        self._tickets = tickets if tickets else []
        self._buyer = buyer
        self._event = event
        
        self._transaction_date = datetime.now()
        self._status = "pending"  # pending, completed, failed, refunded

    def show_transaction(self) -> str:
        return (f"ID: {self._transaction_id}\n"
                f"Valor: R${self._value:.2f}\n"
                f"Método: {self._payment_method}\n"
                f"Status: {self._status}")

    @property
    def tickets(self) -> List[Ticket]:
        return self._tickets

    @property
    def buyer(self) -> Participant:
        return self._buyer

    @property
    def event(self) -> Event:
        return self._event