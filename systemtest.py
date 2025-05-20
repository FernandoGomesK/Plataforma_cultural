from typing import List
import uuid

class Review:
    def __init__(self, author: str, review: str):
        self.author = author
        self.review = review
        
class Ticket:
    def __init__(self, event: 'Event', price: float):
        self.id = str(uuid.uuid4())[:4]
        self.event = event
        self.price = price
        self.sold = False
    
    def mark_as_sold(self):  
        self.sold = True      
class Event:
    def __init__(self, name: str, total_tickets: int, ticket_price: float):
        self.name = name
        self.ticket_price = ticket_price
        self._tickets = [Ticket(self, price = ticket_price) for x in range(total_tickets)]
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
        
        
        

class System():
    def __init__(self):
        self.active_events: List[Event] = []
        
    def run(self):
        while True:
            print("Main Menu")
            print("1 Create Event")
            print("2 Sell Ticket")
            print("3 list event")
            print("4 write review")
            print("5 show review")
            
            choice = input("choose one option: ")
            
            if choice == "1":
                self.create_event()
            elif choice == "2":
                self.sell_tickets()
            elif choice == "3":
                self.show_active_events()
            elif choice == "4":
                self.create_review()
            elif choice == "5":
                self.show_reviews()
                
                
    def create_event(self):
        name = input("Event name: ")
        tickets = int(input("Ticket Quantity: "))
        price = float(input("Ticket price: "))
        
        new_event = Event(name, tickets, price)
        self.active_events.append(new_event)
        print(f"created {name}, with {tickets} tickets")
        
    def sell_tickets(self):
        if not self.active_events:
            print("there is no event with tickets to be sold")
            return
        
        print("current active events")
        for idx, event in enumerate(self.active_events, 1):
            print(f"{idx}. {event.name} {len(event.available_tickets)} left")
            
        try:
            choice = int(input("select Event: ")) - 1
            selected_event = self.active_events[choice]
            ticket = selected_event.sell_ticket()
            print(f"Sold ticket for {selected_event.name}! ID: {ticket.id}")
        except (ValueError, IndexError):
            print("Invalid event selection!")

        
    def show_active_events(self):
        for event in self.active_events:
            print(f"Event Name: {event.name}, Ticket Price: R${event.ticket_price}, remaining tickets: {len(event.available_tickets)}")
            
    def create_review(self):
        if not self.active_events:
            print("there is no event to write a review on")
            return
        print("current active events")
        for idx, event in enumerate(self.active_events):
            print(f"{idx}. {event.name}")
            
            choice = int(input("Select Event: ")) - 1
            selected_event = self.active_events[choice]
            
            author = input("user name:")
            review = input("write your review: ")
            
            selected_event.write_review(author, review)
            
    def show_reviews(self):
        if not self.active_events:
            print("\nThere are no events to review")
            return
            
        print("\nSelect an event to view reviews:")
        for idx, event in enumerate(self.active_events, 1):
            print(f"{idx}. {event.name}")
            
        try:
            choice = int(input("Enter event number: ")) - 1
            selected_event = self.active_events[choice]
            selected_event.show_reviews()  
        except (ValueError, IndexError):
            print("Invalid event selection!")
            
tique = System()
tique.run()