from typing import List
from ticket import Ticket
from review import Review
from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from transactions import Transactions
    from user_classes import Organizer
#
class Event:
    def __init__(self, name: str, type:str, description:str, start_date:date, end_date:date, organizer: Organizer, total_tickets:int,
                remaining_tickets: int, transactions: List['Transactions'], review: List['Review']):
        self._name = name
        self._type = type
        self._description = description
        self.start_date = start_date # inserir dia inicial via biblioteca datetime
        self.end_date = end_date # inserir dia final ''   '' ''
        self._organizer = organizer
        self._total_tickets = total_tickets
        self._remaining_tickets = remaining_tickets
        self._transactions = transactions
        self.review = review
        

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

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, value):
        self.start_date = value

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, value):
        self.end_date = value

class Event:
    def __init__(self, name: str, total_tickets: int, ticket_price: float):
        self.name = name
        self.ticket_price = ticket_price
        self._tickets = [Ticket(self, price = ticket_price)     for x in range(total_tickets)]
        self.reviews: List[Review] = []
        
    @property
    def available_tickets(self) -> List[Ticket]:
        return [ticket for ticket in self._tickets if not ticket.sold]
    
    def sell_ticket(self) -> Ticket:
        for ticket in self._tickets:
            if not ticket.sold:
                ticket.mark_as_sold()
                return ticket
        raise ValueError("unavailable")
        
    def write_review(self, author: str, review: str) -> Review:
        review = Review(author, review)
        self.reviews.append(review)
        return review
    
    def show_reviews(self):
        if not self.reviews:
            print("no reviews yet")
            return
        
        print(f"reviews for {self.name}")
        for review in self.reviews:
            print(f"{review.author}")
            print(f"{review.review}")
            
    def to_dict(self):
        return {
            'name': self.name,
            'ticket_price': self.ticket_price,
            'tickets': [t.to_dict() for t in self._tickets],
            'reviews': [r.to_dict() for r in self.reviews]
        }