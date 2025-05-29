from typing import List, Optional
import uuid
import json
from datetime import *
from user_classes import *
from ticket import *
from event import *
from review import *
from menus import *
from Event_manager import *

from verifications import *

class System():
    def __init__(self):
        self.active_events: List[Event] = []
        self.active_users: List[User] = []
        self.current_user: Optional[User] = None
        self.event_manager = Event_Manager()
        #self.data_manager = Data_manager()
        self.load()
        
    def run(self):
            while True:
                if not self.current_user:
                    choice = self._manage_Login_and_Register()
                    if choice == "exit":
                        break
                else:
                    self.main_menu()
                    
    
                if not self.current_user:
                    Login_menu()
                    
    def _manage_Login_and_Register(self) -> str:
            while True:
                choice = Login_menu.show_menu()
            
                if choice == "1":
                    username = input("username: ")
                    password = input("password: ")
                    try: 
                        user_found = self.login(username, password)
                        if user_found:
                            self.current_user = user_found
                            print(f"Welcome {self.current_user.name}")
                            return "continue"
                    except ValueError as e:
                        print(f"Error logging in: {e}")
                elif choice == "2": 
                    self.create_user()
                elif choice == "3":   
                    return "exit"
                else:
                    print("invalid option, please select one from the menu")
                    
                
                    
    def login(self, username: str, password: str):
        for user in self.active_users:
            if user.username == username and user.password == password:
                return user
        raise ValueError("User not found")
    

    def manage_event_menu(self):
        is_current_user_admin = self.current_user.admin
        while True:
            print("\n--- Menu de Eventos ---")
            # 2. Chamar Event_Menu.show_menu() com o status de admin correto
            choice = Event_Menu.show_menu(is_admin=is_current_user_admin)

            if is_current_user_admin:
                # Lógica para opções de ADMIN
                if choice == "1": # Create Event
                    self.create_event()
                elif choice == "2": # Remove Event
                    self.remove_event()
                elif choice == "3": # Show Events
                    self.show_active_events()
                elif choice == "4": # Show Reviews
                    self.show_reviews()
                elif choice == "5": # Exit (do Menu de Eventos)
                    break # Sai do loop do manage_event_menu
                else:
                    print("Opção inválida para administrador.")
            else:
                # Lógica para opções de USUÁRIO NÃO-ADMIN
                if choice == "1": # Show Events
                    self.show_active_events()
                elif choice == "2": # Show Reviews
                    self.show_reviews()
                elif choice == "3":
                    self.create_review()
                elif choice == "4": # Exit (do Menu de Eventos)
                    break # Sai do loop do manage_event_menu
                else:
                    print("Opção inválida para usuário.")
        
    
    
    def main_menu(self):
        while True:
            print("\n--- Menu Principal ---")
            # Supondo que Main_menu.show_menu() exibe "1 - Event Menu", "2 - Sair do Menu Principal"
            choice = Main_menu.show_menu() # Do seu menus.py

            if choice == "1":
                # CORRETO: Chama o manage_event_menu quando a opção 1 é escolhida
                self.manage_event_menu()
            elif choice == "2": # Ou a opção que significa "Sair" ou "Deslogar"
                print("Deslogando e voltando para tela inicial...")
                self.current_user = None # Importante para a lógica no run()
                break # Sai do loop do main_menu, voltando para o loop do run()
            else:
                print("Opção inválida, por favor escolha uma do menu.")
        
                    
    def create_user(self):
        name = input("Input your name: ")
        while True:
            cpf = input("CPF(xxx.xxx.xxx-xx): ")
            if is_valid_cpf(cpf):
                break
            else:
                print("Please use xxx.xxx.xxx-xx format")
        while True:
            birth_date = input("Birth date(DD/MM/YYYY): ")
            try:
                birth = datetime.strptime(birth_date, "%d/%m/%Y")
                age = (datetime.now() - birth).days // 365
                if age >= 16:
                    break
                else:
                    print("The User must be older than 16 years old")
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")
        while True: 
            email = input("E-mail: ")
            if is_valid_email(email):
                break
            else:
                print("please use a valid e-mail adress")
           
        username = input("username: ")
        password = input("password: ")
        
        try:
            new_user = User(name=name, cpf=cpf, age=str(age), email=email, username=username, password=password)
            self.active_users.append(new_user)
            print(f"User {username} created successfully!")
            self.current_user = new_user
            print(f"Welcome, {new_user.name}!")
        except Exception as e:
            print(f"Error creating user object: {e}")
      

    def create_e            
                          
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
        
        self.show_active_events()
            
        try:
            choice = int(input("select Event: ")) - 1
            selected_event = self.active_events[choice]
            ticket = selected_event.sell_ticket()
            print(f"Sold ticket for {selected_event.name}! ID: {ticket.id}")
        except (ValueError, IndexError):
            print("Invalid event selection!")

        
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
                   
if __name__ == "__main__":
    cultural = System()
    cultural.run()