from event import Event
from datetime import date
from organizer import Organizer

class LiveEvent(Event):
    def __init__(self, venue: str, capacity: int, 
                 name: str, description: str, 
                 start_date: date, end_date: date, 
                 organizer: Organizer, 
                 total_tickets: int):
        
        super().__init__(name, "LIVE", description,
                        start_date, end_date, organizer,
                        total_tickets, total_tickets)
        
        self._venue = venue
        self._capacity = capacity

    def check_venue_capacity(self) -> bool:
        return self._remaining_tickets < self._capacity
    
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, value):
        self._venue = value
    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, value):
        self._capacity = value