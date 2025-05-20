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