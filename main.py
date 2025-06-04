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
        self.active_users: List[BaseUser] = []
        self.current_user: Optional[BaseUser] = None
        self.event_manager = Event_Manager()
        #self.data_manager = Data_manager()
        self.load()
        
    def run(self):
            while True:
                if not self.current_user:
                    choice = self._manage_Login_and_Register()
                    if choice == "exit":
                        print("/////////////////////////////")
                        print("Goodbye!")
                        self.save()
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

        """
        This function is responsible for managing the user interaction when the user wants to manage events.

        If the user is an admin, it will show the admin options:
            - Create Event: creates a new event
            - Remove Event: removes an event
            - Show Events: shows all active events
            - Show Reviews: shows all reviews for all events
            - Exit: exits the event menu

        If the user is not an admin, it will show the user options:
            - Show Events: shows all active events
            - Buy Ticket: allows the user to buy a ticket for an event
            - Show Reviews: shows all reviews for all events
            - Write Review: allows the user to write a review for an event
            - Exit: exits the event menu

        It will keep asking the user for an option until the user chooses to exit.
        """
        is_current_user_admin = self.current_user.admin
        while True:
            print("\n--- Event Menu ---")
            
            choice = Event_Menu.show_menu(is_admin=is_current_user_admin)

            if is_current_user_admin:
                # Lógica para opções de ADMIN
                if choice == "1": # Create Event
                    new_event = self.event_manager.create_event()
                    if new_event:
                        self.active_events.append(new_event)
                        print(f"event {new_event.name}")
                        self.save()
                    else:
                        print("error creating event")
                elif choice == "2": # Remove Event
                    self.remove_event()
                elif choice == "3": 
                    self.show_active_events()
                elif choice == "4": 
                    self.show_reviews()
                elif choice == "5": 
                    break 
                else:
                    print("Admin invalid Option.")
            else:
               
                if choice == "1":
                    self.show_active_events()
                elif choice == "2":
                    self.sell_tickets()
                elif choice == "3": 
                    self.show_reviews()
                elif choice == "4":
                    self.create_review()
                elif choice == "5": 
                    break 
                else:
                    print("User invalid Option.")
          
    def main_menu(self):
        while True:  
            choice = Main_menu.show_menu() 
            if choice == "1":
                self.manage_event_menu()
            elif choice == "2": 
                print("Logging out and returning to login menu...")
                self.current_user = None 
                break 
            else:
                print("Invalid Option, please select one from the menu.") 
                           
    def create_user(self):
        user_type_choice = input("What User do you want to register? (1-User, 2-Organizer, 3-Intermediary): ")
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
                self.save()
                break
            else:
                print("please use a valid e-mail adress")
           
        username = input("username: ")
        password = input("password: ")
        
        try:
            if user_type_choice == '1': # User
                new_person = User(name=name, cpf=cpf, age=str(age), email=email, username=username, password=password)
            elif user_type_choice == '2': # Organizer
                new_person = Organizer(name=name, cpf=cpf,age = str(age),email=email, username=username, password=password)
            elif user_type_choice == '3': # Intermediary
                new_person = Intermediary(name=name, cpf=cpf, age = str(age), email=email, username=username, password=password)
            else:
                print("Invalid User Type.")
                return 

            self.active_users.append(new_person)
            print(f"{type(new_person).__name__} {new_person.name} Created Sucessfully!")

        except Exception as e:
            print(f"Error creating User: {e}")
                                     
    def sell_tickets(self):
        if not self.active_events:
            print("there is no event with tickets to be sold")
            return
        
        self.show_active_events()
            
        try:
            choice_str = input("select Event (digite o número): ")
            if not choice_str.isdigit(): 
                print("Seleção inválida. Por favor, digite um número.")
                return
            choice = int(choice_str) - 1

            if not (0 <= choice < len(self.active_events)):
                print("Número do evento fora do intervalo.")
                return
                
            selected_event = self.active_events[choice]
            
            ticket_vendido = selected_event.sell_ticket() 
            
            self.current_user.buy_ticket(ticket_vendido)
            
            print(f"Ingresso ID {ticket_vendido.id} para o evento '{selected_event.name}' comprado com sucesso por {self.current_user.name}!")
            print(f"Você agora tem {len(self.current_user.tickets)} ingresso(s).")

        except ValueError as ve: 
            print(f"Erro na venda: {ve}")
        except IndexError: 
            print("Seleção de evento inválida!")
        except Exception as e: 
            print(f"Ocorreu um erro inesperado: {e}")
            
    def show_active_events(self):
        if not self.active_events:
            print("there is no events currently active")
            return
        else:    
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
            'users': [u.to_dict() for u in self.active_users]
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
                #////////////event loading///////////////
                for event_data in data.get('events', []):
                    event_name = event_data.get("name")
                    event_ticket_price = event_data.get("ticket_price")
                    event_tickets_data = event_data.get("tickets", [])
                    event_type_str = event_data.get("type")
                    event_description = event_data.get("description")
                    event_start_date = event_data.get("start_date")
                    event_end_date = event_data.get("end_date")
                    
                    if not all([event_name, event_ticket_price, event_tickets_data, event_type_str, event_description, event_start_date, event_end_date]):
                        print("Invalid event data. Skipping event.")
                        continue
                    
                    event = Event(
                        name=event_name,
                        total_tickets=len(event_tickets_data),
                        ticket_price=event_ticket_price,
                        event_type=event_type_str,
                        description=event_description,
                        start_date=event_start_date,
                        end_date=event_end_date
                    )
                    
                    for ticket_data, ticket_obj in zip(event_tickets_data, event._tickets):
                        saved_ticket_id = ticket_data.get('id')
                        if saved_ticket_id: 
                            ticket_obj.id = saved_ticket_id 
                        ticket_obj.sold = ticket_data.get('sold', False)

                    event.reviews = []
                    for review_data in event_data.get('reviews', []):
                        event.reviews.append(Review(
                            author=review_data.get('author'),
                            review=review_data.get('review')
                    ))
                    self.active_events.append(event)
                    
                    #////////////user loading///////////////
                    
                self.active_users = []
                for user_data in data.get('users', []):
                    user_type = user_data['user_type']
                    name = user_data['name']
                    cpf = user_data['cpf']
                    age = user_data['age']
                    email = user_data['email']
                    username = user_data['username']
                    password = user_data['password']
                    admin = user_data['admin']

                    if not all([name, cpf, age, email, username, password, admin]):
                        print("Invalid user data. Skipping user.")
                        continue
                        
                    new_user_object = None
                    try:
                        if user_type == "User":
                            new_user_object = User(name, cpf, age, email, username, password, admin)
                        elif user_type == "Organizer":
                            new_user_object = Organizer(name, cpf, age, email, username, password, admin)
                        elif user_type == "Intermediary":
                            new_user_object = Intermediary(name, cpf, age, email, username, password, admin)
                        else:
                            print(f"Invalid user type {user_type}. Skipping user.")
                    except Exception as e:
                        print(f"error creating user {user_type}, {name} , {e}")
                        continue
                        
                    if new_user_object:
                        loaded_user_tickets = []
                        for ticket_dict in user_data.get('tickets', []):
                            try:
                                ticket_id = ticket_dict.get('id')
                                ticket_event_name = ticket_dict.get('event_name')
                                ticket_price = ticket_dict.get('price')
                                ticket_sold = ticket_dict.get('sold')
                                    
                                if ticket_id is None or ticket_event_name is None or ticket_price is None or ticket_sold is None:
                                    print(f"Ticket Data is missing {ticket_data}. Skipping ticket.")
                                    continue
                                    
                                created_ticket = Ticket(
                                    id=ticket_id,
                                    event_name=ticket_event_name,
                                    price=ticket_price,
                                    sold_status=ticket_sold
                                    )
                            except Exception as e:
                                print(f"Couldnt get ticket data, skipping ticket {e}")
                                    
                        new_user_object.tickets = loaded_user_tickets
                        self.active_users.append(new_user_object)
                    
                        
                print('The Data Was Loaded sucessully')
                print('//////////////////////////////')
                
        except FileNotFoundError:
            print("No existing data found - starting fresh")
        except Exception as e:
            print(f"Error loading data: {e}")
            
    def gen_admin(self):
        new_person = User(name= "eu2", cpf="123.456.789-11", age=str("20"), email="eu@eu.com", username="user", password="123", admin=False)
        self.active_users.append(new_person)

if __name__ == "__main__":
    cultural = System()
    cultural.gen_admin()
    cultural.run()