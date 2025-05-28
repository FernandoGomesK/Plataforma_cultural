from person import Person
from review import Review  # Participant creates Review objects
from ticket import Ticket  # Participant holds Ticket objects
from transaction import Transaction  # Participant initiates Transactions
from typing import List, TYPE_CHECKING
from datetime import date
import uuid

if TYPE_CHECKING:
    from event import Event


class Participant(Person):
    def __init__(self, name: str, cpf: str, age: str, address: str):
        super().__init__(name, cpf, age, address)
        self._tickets: List[Ticket] = []

    @property
    def tickets(self) -> List[Ticket]:
        return self._tickets

    @tickets.setter
    def tickets(self, value: List[Ticket]):
        self._tickets = value

    def authenticate(self) -> bool:
        print(f"Authenticating participant: {self.name}")
        return True

    def write_review(self, event_id: str, rating: int, comment: str) -> Review:
        # Note: This method creates a Review, but adding it to the Event's list
        # would require an Event object or a system-level function.

        review = Review(
            review_id=str(uuid.uuid4()),
            reviewer_id=self.cpf,  # Participant's CPF as reviewer_id
            rating=rating,
            comment=comment,
            review_date=date.today(),
        )
        # To link review to an event, an Event instance or a service is needed.
        # Example: event_object.add_review(review)
        print(f"Participant {self.name} wrote a review for event {event_id}.")
        return review

    def buy_ticket(
        self,
        event_object: "Event",  # Pass the actual Event object to call its methods
        ticket_type: str,
        quantity: int,
        price_per_ticket: float,  # Assuming price is per ticket
        payment_method: str,
    ) -> List[Ticket]:

        # This method interacts with an Event object directly to check remaining tickets
        # and call sell_ticket.

        bought_tickets: List[Ticket] = []
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        # Create one transaction for potentially multiple tickets in this purchase
        # The total value would be quantity * price_per_ticket
        total_value = quantity * price_per_ticket

        # Transaction needs its own ID
        transaction_id = str(uuid.uuid4())

        # The Transaction object is created here.
        # Note: The `Transaction` constructor in transaction.py expects buyer_id and event_id.
        # The list of tickets in Transaction is filled after tickets are created.
        current_transaction = Transaction(
            transaction_id=transaction_id,
            value=total_value,
            payment_method=payment_method,
            buyer_id=self.cpf,  # Participant's CPF
            event_id=event_object.event_id,  # Event's ID
        )

        for _ in range(quantity):
            if event_object.remaining_tickets <= 0:
                # Update status of transaction if some tickets were processed before running out
                if not bought_tickets:  # No tickets bought yet
                    current_transaction.status = "failed"
                else:  # Partially completed
                    current_transaction.status = "partially_completed"
                    current_transaction.value = len(bought_tickets) * price_per_ticket
                print(
                    f"Transaction {current_transaction.transaction_id} status: {current_transaction.status}"
                )
                raise Exception("Ingressos esgotados durante a compra.")

            # Event's sell_ticket method creates the Ticket object
            # It needs participant_id and the transaction_id
            ticket = event_object.sell_ticket(
                participant_id=self.cpf,  # Participant's CPF
                ticket_type=ticket_type,
                price=price_per_ticket,
                transaction_id=current_transaction.transaction_id,  # Pass the ID
            )

            current_transaction.add_ticket(
                ticket
            )  # Add created ticket to transaction's list
            self._tickets.append(ticket)  # Add ticket to participant's list
            bought_tickets.append(ticket)

        current_transaction.status = "completed"
        print(
            f"Participant {self.name} bought {len(bought_tickets)} ticket(s) for event {event_object.name}."
        )
        print(
            f"Transaction {current_transaction.transaction_id} status: {current_transaction.status}"
        )
        # The current_transaction object could be returned or handled by a system service.
        return bought_tickets
