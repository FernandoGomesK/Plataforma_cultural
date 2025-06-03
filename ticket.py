import uuid
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from event import Event
class Ticket:
    def __init__(self,
                 id_value: Optional[str] = None, event_name: str = None, price: float):
        self.id = id_value if id_value is not None else str(uuid.uuid4())[:4]
        self.event = event
        self.price = price
        self.sold = False
    
    def mark_as_sold(self):  
        self.sold = True      
        
    def to_dict(self):
        return {
            'id': self.id,
            'event': self.event, 
            'price': self.price,
            'sold': self.sold
        }
        
