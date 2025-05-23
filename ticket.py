import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from event import Event
class Ticket:
    def __init__(self, event: 'Event', price: float):
        self.id = str(uuid.uuid4())[:4]
        self.event = event
        self.price = price
        self.sold = False
    
    def mark_as_sold(self):  
        self.sold = True      
        
    def to_dict(self):
        return {
            'id': self.id,
            'sold': self.sold
        }
        
