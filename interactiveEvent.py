from datetime import date
from event import Event


class InteractiveEvent(Event):
    def __init__(
        self,
        name: str,
        event_type: str,
        description: str,
        start_date: date,
        end_date: date,
        organizer_id: str,
        total_tickets: int,
        interaction_type: str,
        max_participants_interaction: int,  # Renamed from max_participants to avoid confusion with total_tickets
    ):
        super().__init__(
            name,
            event_type,
            description,
            start_date,
            end_date,
            organizer_id,
            total_tickets,
        )
        self._interaction_type = interaction_type
        self._max_participants_interaction = max_participants_interaction

    @property
    def interaction_type(self) -> str:
        return self._interaction_type

    @interaction_type.setter
    def interaction_type(self, value: str):
        self._interaction_type = value

    @property
    def max_participants_interaction(self) -> int:
        return self._max_participants_interaction

    @max_participants_interaction.setter
    def max_participants_interaction(self, value: int):
        self._max_participants_interaction = value

    def enable_participant_input(self) -> None:
        # Logic to enable participant input
        print(
            f"Participant input enabled for {self.name} (Type: {self._interaction_type})."
        )
