from event import Event
from participant import Participant
from datetime import date
from organizer import Organizer

class OnlineEvent(Event):
    def __init__(self, streaming_link: str, platform: str,
                 name: str, description: str,
                 start_date: date, end_date: date,
                 organizer: Organizer):
        
        super().__init__(name, "ONLINE", description,
                        start_date, end_date, organizer,
                        None, None)
        
        self._streaming_link = streaming_link
        self._platform = platform

    def send_access_link(self, participant: Participant):
        pass

    @property
    def streaming_link(self):
        return self._streaming_link
    
    @streaming_link.setter
    def streaming_link(self, value):
        self._streaming_link = value
    
    @property
    def platform(self):
        return self._platform
    
    @platform.setter
    def platform(self, value):
        self._platform = value
