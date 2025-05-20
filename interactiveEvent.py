from event import Event
from datetime import date
from organizer import Organizer

class InteractiveEvent(Event):
    def __init__(self, interaction_type: str, max_participants: int,
                 name: str, description: str,
                 start_date: date, end_date: date,
                 organizer: Organizer):
        
        super().__init__(name, "INTERACTIVE", description,
                        start_date, end_date, organizer,
                        max_participants, max_participants)
        
        self._interaction_type = interaction_type  # Ex: "Q&A", "Poll", "Workshop"
        self._active_participants = 0

    def enable_participant_input(self):
        self._active_participants += 1