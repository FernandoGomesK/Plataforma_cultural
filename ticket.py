from  event import Event
from participant import Participant
from datetime import date

class Ticket:
    def __init__(self, event:Event, owner:Participant, purchase_date: date, ticket_id:str,price:float, ticket_type:str, is_active:bool):
        self._event = event
        self._owner = owner
        self._purchase_date = purchase_date 
        self._ticket_id = ticket_id
        self._price = price
        self._ticket_type = ticket_type
        self._is_active = False

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @property
    def purchase_date(self):
        return self._purchase_date

    @purchase_date.setter
    def purchase_date(self, value):
        self._purchase_date = value

    @property
    def ticket_id(self):
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, value):
        self._ticket_id = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def ticket_type(self):
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, value):
        self._ticket_type = value

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value):
        self._is_active = value

    def cancel(self):
        pass
    
    def validate(self):
        pass
    
    def transfer_to(new_owner: Participant):
        pass