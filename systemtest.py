from typing import List
import uuid
import json
from pathlib import Path

class Review:
    def __init__(self, author: str, review: str):
        self.author = author
        self.review = review
        
    def to_dict(self):
        return {
            'author': self.author,
            'review': self.review
        }
        
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
            print("6 remove event")
            print("7 save data")
            print("8 load data")
            print("9 exit")
            
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
            elif choice == "6":
                self.remove_event()
            elif choice == "7":
                self.save()
            elif choice == "8":
                self.load()
            elif choice == "9":
                print("thank you for using cultural app!")
                break
            else:
                print("that was a invalid option, please pick one on the menu")
                
                
                
    def create_event(self):
        name = input("Event name: ")
        tickets = int(input("Ticket Quantity: "))
        price = float(input("Ticket price: "))
        
        new_event = Event(name, tickets, price)
        self.active_events.append(new_event)
        print(f"created {name}, with {tickets} tickets")
        
    def sell_tickets(self):
        """
    Prompts user to select an event and sells one ticket for the selected event.
    
    If there are no events with tickets left, the function will print a message and
    return immediately.
    
    If the user enters an invalid event number, the function will print an error
    message and return.
    
    When a ticket is successfully sold, the function will print a confirmation
    message.
    """
        if not self.active_events:
            print("there is no event with tickets to be sold")
            return
        
        self.show_active_events()
            
        try:
            choice = int(input("select Event: ")) - 1
            selected_event = self.active_events[choice]
            ticket = selected_event.sell_ticket()
            print(f"Sold ticket for {selected_event.name}! ID: {ticket.id}")
        except (ValueError, IndexError):
            print("Invalid event selection!")
           #self.save_events()

        
    def show_active_events(self):
        if not self.active_events:
            print("there is no events currently active")
            return
            
        print("current active events")
        for idx, event in enumerate(self.active_events, 1): 
            print(f"{idx}. Event name: {event.name} price: R${event.ticket_price}, {len(event.available_tickets)}/{len(event._tickets)} tickets left")
            print("/////////////////////////////")
        
            
    def create_review(self):
        if not self.active_events:
            print("there is no event to write a review on")
            return
        print("current active events")
        for idx, event in enumerate(self.active_events, 1):
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
            
        self.show_active_events()
            
        try:
            choice = int(input("Enter event number: ")) - 1
            selected_event = self.active_events[choice]
            selected_event.show_reviews()  
        except (ValueError, IndexError):
            print("Invalid event selection!")
            
    def remove_event(self):
        if not self.active_events:
            print("there is no event to be removed")
            
        self.show_active_events()
            
        try:
            choice = int(input("Enter the number of the event to be removed: ")) - 1  
            if 0 <= choice < len(self.active_events):
                removed_event = self.active_events.pop(choice)
                print(f"removed event: {removed_event.name}")  
            else:
                print("Invalid Event Number")        
        except ValueError:
            print("please input a valid number")
            
    def save(self):
        data = {
            'events': [e.to_dict() for e in self.active_events],
        }   

        try:
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=2)
            print('The Data Was Saved sucessully')
        except Exception as e:
            print(f"Error saving data: {e}")
        
         
    def load(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                
                self.active_events = []
                for event_data in data.get('events', []):
                    event = Event(
                        name=event_data['name'],
                        total_tickets=len(event_data['tickets']),
                        ticket_price=event_data['ticket_price']
                    )
                    
                    for ticket_data, ticket_obj in zip(event_data['tickets'], event._tickets):
                        ticket_obj.sold = ticket_data['sold']
                        ticket_obj.id = ticket_data.get('id', str(uuid.uuid4())[:4])
                        
                    for review_data in event_data['reviews']:
                        event.reviews.append(Review(
                            author=review_data['author'],
                            review=review_data['review']
                    ))
                
                self.active_events.append(event)
                print('The Data Was Loaded sucessully')
                print('//////////////////////////////')
                
        except FileNotFoundError:
            print("No existing data found - starting fresh")
        except Exception as e:
            print(f"Error loading data: {e}")
         
            
tique = System()
tique.run()