from typing import List, Optional
import uuid
import json
from pathlib import Path
from user_classes import *
from ticket import *
from event import *
from review import *
from menus import *

class System():
    def __init__(self):
        self.active_events: List[Event] = []
        self.active_users: List[User] = []
        self.current_user: Optional[User] = None
        self.run()
        
        def run(self):
            while True:
                
                
                try:
                    self.load()
                except Exception as e:
                    print(f"Error loading data: {e}")
                    
                if not self.current_user:
                    login_menu()
                    
                
                
        def login_menu():
            while True:
                choice = login_menu.show_menu()
            
                if choice == "1":
                    self.login()
                elif choice == "2": 
                    self.create_user()
                elif choice == "3":   
                    break
                else:
                    print("invalid option, please select one from the menu")  
                    
        def main_menu():
            while True:
                choice = main_menu.show_menu()
                
                if choice == "1":
                    pass
        
                    
                
     
            """       
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
                print("that was a invalid option, please pick one on the menu") """
                
    def create_user(self):
        user = User(
            name = input("Input your name: "),
            cpf = input("CPF: "),
            age = input("Age: "),
            email = input("E-mail: "),
            username = input("username: "),
            password = input("password: ")
        )
        self.active_users.append(user)
        self.current_user = user
                
    def login(self, username: str, password: str):
        for user in self.active_users:
            if user.username == username and user.verify_password(password):
                return self.current_user
        raise ValueError("invalid Login")

                
                          
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

        
    def show_active_events(self):
        """
    Prints all active events, with their current ticket availability.
    
    If there are no active events, the function will print a message and return
    immediately.
    """
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
                   
