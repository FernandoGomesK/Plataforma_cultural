from datetime import date
from event import Event


class OnlineEvent(Event):
    def __init__(
        self,
        name: str,
        event_type: str,
        description: str,
        start_date: date,
        end_date: date,
        organizer_id: str,
        total_tickets: int,
        streaming_link: str,
        platform: str,
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
        self._streaming_link = streaming_link
        self._platform = platform

    @property
    def streaming_link(self) -> str:
        return self._streaming_link

    @streaming_link.setter
    def streaming_link(self, value: str):
        self._streaming_link = value

    @property
    def platform(self) -> str:
        return self._platform

    @platform.setter
    def platform(self, value: str):
        self._platform = value

    def send_access_link(
        self, participant_email: str
    ):
        print(
            f"Sending access link for {self.name} to {participant_email} for platform {self._platform}: {self._streaming_link}"
        )