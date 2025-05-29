from typing import List, Optional
from event import Event
from datetime import *

class Event_Manager():
    def __init__(self):
        self._events: List[Event] = []

    def create_event(self):
        print("----------Create Event----------")
        name = input("Input the name of the Event: ")
        tickets = int(input("Input the number of tickets: "))
        price = float(input("Input the price of the ticket: "))
        event_type = input("state the type of event(theather, play, concert): ")
        description = input("Input the description of the event: ")
        
        start_date = None
        while True:
            start_date = input("Input the start date of the event(DD/MM/YYYY): ")
            try:
                start = datetime.strptime(start_date, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")
                
        end_date = None
        while True:
            end_date = input("Input the end date of the event(DD/MM/YYYY): ")
            try:
                end = datetime.strptime(end_date, "%d/%m/%Y").date()
                if end >= start:
                    break
                else:
                    print("The end date must be after the start date")  
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")
        
        
        new_event = Event(
            name = name,
            total_tickets = tickets,
            ticket_price = price,
            event_type = event_type,
            description = description,
            start_date = start_date,
            end_date = end_date
        )
        self._events.append(new_event)
        print(f"created {name}, with {tickets} tickets")

manajo = Event_Manager()
manajo.create_event(
    
)