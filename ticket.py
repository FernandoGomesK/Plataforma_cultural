from datetime import date

class Ticket:
    def __init__(
        self,
        event_id: str,
        owner_id: str,
        purchase_date: date,
        ticket_id: str,
        price: float,
        ticket_type: str,
        is_active: bool,
        transaction_id: str,
    ):
        self._event_id = event_id
        self._owner_id = owner_id
        self._purchase_date = purchase_date
        self._ticket_id = ticket_id
        self._price = price
        self._ticket_type = ticket_type
        self._is_active = is_active
        self._transaction_id = transaction_id

    @property
    def event_id(self) -> str:
        return self._event_id

    @event_id.setter
    def event_id(self, value: str):
        self._event_id = value

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value: str):  # Participant's CPF
        self._owner_id = value

    @property
    def purchase_date(self) -> date:
        return self._purchase_date

    @purchase_date.setter
    def purchase_date(self, value: date):
        self._purchase_date = value

    @property
    def ticket_id(self) -> str:
        return self._ticket_id

    # ticket_id should be immutable

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        self._price = value

    @property
    def ticket_type(self) -> str:
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, value: str):
        self._ticket_type = value

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool):
        self._is_active = value

    @property
    def transaction_id(self) -> str:
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value: str):
        self._transaction_id = value

    def transfer_to(self, new_owner_id: str):
        if not self._is_active:
            raise Exception("Ticket inativo não pode ser transferido.")
        self._owner_id = new_owner_id
        print(f"Ticket {self.ticket_id} transferred to new owner (ID: {new_owner_id}).")
