from datetime import date
from participant import Participant

class Review:
    def __init__(self, review_id: str, reviewer: Participant, rating: int, 
                 comment: str, review_date: date):
        self._review_id = review_id
        self._reviewer = reviewer
        self._rating = rating
        self._comment = comment
        self._review_date = review_date
        
    @property
    def review_id(self):
        return self._review_id
    
    @property
    def reviewer(self):
        return self._reviewer
    
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, value):
        self._rating = value
    
    @property
    def comment(self):
        return self._comment
    
    @comment.setter
    def comment(self, value):
        self._comment = value
    
    @property
    def review_date(self):
        return self._review_date