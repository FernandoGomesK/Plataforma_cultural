import uuid
from typing import TYPE_CHECKING, Optional

class Ticket:
    def __init__(self, price: float, event_name: str, id_value: Optional[str] = None, sold_status: bool = False ):
        self.id = id_value if id_value is not None else str(uuid.uuid4())[:4]
        self.event_name = event_name
        self.price = price
        self.sold = sold_status   
    def mark_as_sold(self):  
        """
        Marks this ticket as sold. If the ticket is already sold, this method does nothing.

        Returns:
            None
        """
        self.sold = True             
    def to_dict(self):
        """
        Converts this Ticket instance to a dictionary.

        The dictionary contains the ticket's id, event_name, price, and sold status.

        Returns:
            dict: A dictionary containing the ticket's attributes.
        """
        return {
            'id': self.id,
            'event_name': self.event_name, 
            'price': self.price,
            'sold': self.sold
        }
        