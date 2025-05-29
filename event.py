from typing import List
from ticket import Ticket
from review import Review


class Event:
    def __init__(self, name: str, total_tickets: int, ticket_price: float,
                 event_type: str, description: str, start_date: str, end_date: str):
        self.name = name
        self.ticket_price = ticket_price
        self._tickets = [Ticket(self, price = ticket_price) for x in range(total_tickets)]
        self.reviews: List[Review] = []
        self.event_type = event_type
        self.description = description  
        self.start_date = start_date
        self.end_date = end_date
        
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
            'reviews': [r.to_dict() for r in self.reviews],
            'type': self.event_type,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date
        }