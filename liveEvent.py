from datetime import date
from event import Event


class LiveEvent(Event):
    def __init__(
        self,
        name: str,
        event_type: str,
        description: str,
        start_date: date,
        end_date: date,
        organizer_id: str,
        total_tickets: int,
        venue: str,
        capacity: int,
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
        self._venue = venue
        self._capacity = capacity  # This is venue capacity, total_tickets is for sales

    @property
    def venue(self) -> str:
        return self._venue

    @venue.setter
    def venue(self, value: str):
        self._venue = value

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int):
        self._capacity = value

    def check_venue_capacity(self) -> bool:
        # This might compare tickets sold (or total_tickets) against venue capacity
        # For simplicity, let's assume it checks if tickets planned exceed capacity
        if self.total_tickets > self._capacity:
            print(
                f"Warning: Total tickets ({self.total_tickets}) for {self.name} exceeds venue capacity ({self._capacity})."
            )
            return False
        print(f"Venue capacity check for {self.name} at {self._venue}: OK.")
        return True
