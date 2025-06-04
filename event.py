from typing import List
from ticket import Ticket
from review import Review


class Event:
    def __init__(self, name: str, total_tickets: int, ticket_price: float,
                 event_type: str, description: str, start_date: str, end_date: str):
        """
    Initializes an Event instance with the specified attributes.
    Parameters:
        name (str): The name of the event.
        total_tickets (int): The total number of tickets available for the event.
        ticket_price (float): The price of each ticket for the event.
        event_type (str): The type of the event (e.g., theater, concert).
        description (str): A brief description of the event.
        start_date (str): The start date of the event in the format 'DD/MM/YYYY'.
        end_date (str): The end date of the event in the format 'DD/MM/YYYY'.
    """
        self.name = name
        self.ticket_price = ticket_price
        self._tickets = [Ticket(price = ticket_price, event_name = name) for x in range(total_tickets)]
        self.reviews: List[Review] = []
        self.event_type = event_type
        self.description = description  
        self.start_date = start_date
        self.end_date = end_date
        
    @property
    def available_tickets(self) -> List[Ticket]:
        """
        Returns a list of available tickets for the event.

        The available tickets are those that have not been sold yet.

        Returns:
            List[Ticket]: A list of unsold Ticket objects.
        """
        return [ticket for ticket in self._tickets if not ticket.sold]
    
    def sell_ticket(self) -> Ticket:
        """
        Sells one ticket from the event.

        If there are available tickets, marks one as sold and returns it.
        If there are no available tickets, raises a ValueError with the message 'unavailable'.

        Returns:
            Ticket: A sold Ticket object.
        """
        for ticket in self._tickets:
            if not ticket.sold:
                ticket.mark_as_sold()
                return ticket
        raise ValueError("unavailable")
       
    def write_review(self, author: str, review: str) -> Review:
        """
        Writes a review for the event.

        Parameters:
            author (str): The name of the person writing the review.
            review (str): The text of the review.

        Returns:
            Review: The created Review instance.
        """
        review = Review(author, review)
        self.reviews.append(review)
        return review
    
    def show_reviews(self):
        """
        Displays all reviews for the event.

        If no reviews have been written, indicates that there are no reviews yet.
        Otherwise, prints each review's author and content.

        Returns:
            None
        """
        if not self.reviews:
            print("no reviews yet")
            return
        
        print(f"reviews for {self.name}")
        for review in self.reviews:
            print(f"{review.author}")
            print(f"{review.review}")
            
    def to_dict(self):
        """
        Converts the Event instance to a dictionary.

        The dictionary contains the event's attributes.

        Returns:
            dict: A dictionary containing the event's attributes.
        """
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