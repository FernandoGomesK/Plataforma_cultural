from typing import List
from datetime import date
from organizer import Organizer
class Event:
    def __init__(self, name: str, type:str, description:str, start_date:date, end_date:date, organizer:Organizer, total_tickets:int,
                 remaining_tickets: int, transactions: List['Transactions'], review: List['Review']):
        self._name = name
        self._type = type
        self._description = description
        self.start_date = start_date # inserir dia inicial via biblioteca datetime
        self.end_date = end_date # inserir dia final ''   '' ''
        self._organizer = organizer
        self._total_tickets = total_tickets
        self._remaining_tickets = remaining_tickets
        self._transactions = transactions
        self.review = review
        

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, value):
        self.start_date = value

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, value):
        self.end_date = value

    @property
    def organizer(self):
        return self._organizer

    @organizer.setter
    def organizer(self, value):
        self._organizer = value

    @property
    def total_tickets(self):
        return self._total_tickets

    @total_tickets.setter
    def total_tickets(self, value):
        self._total_tickets = value

    @property
    def remaining_tickets(self):
        return self._remaining_tickets

    @remaining_tickets.setter
    def remaining_tickets(self, value):
        self._remaining_tickets = value

    @property
    def transactions(self):
        return self._transactions

    @transactions.setter
    def transactions(self, value):
        self._transactions = value

    def get_review(self):
        return self.review

    def set_review(self, value):
        self.review = value

