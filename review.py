from datetime import date
from typing import TYPE_CHECKING

# if TYPE_CHECKING:
# from participant import Participant # Not needed if using reviewer_id: str


class Review:
    def __init__(
        self,
        review_id: str,
        reviewer_id: str,
        rating: int,
        comment: str,
        review_date: date,
    ):
        self._review_id = review_id
        self._reviewer_id = reviewer_id  # Changed from Participant object
        self._rating = rating
        self._comment = comment
        self._review_date = review_date

    @property
    def review_id(self) -> str:
        return self._review_id

    @property
    def reviewer_id(self) -> str:  # Assuming CPF of the reviewer
        return self._reviewer_id

    # No setter for reviewer_id as it's set on creation

    @property
    def rating(self) -> int:
        return self._rating

    @rating.setter
    def rating(self, value: int):
        if not (1 <= value <= 5):  # Example validation
            raise ValueError("Rating must be between 1 and 5.")
        self._rating = value

    @property
    def comment(self) -> str:
        return self._comment

    @comment.setter
    def comment(self, value: str):
        self._comment = value

    @property
    def review_date(self) -> date:
        return self._review_date
