class Review:
    def __init__(self, author: str, review: str):
        self.author = author
        self.review = review
        
    def to_dict(self):
        return {
            'author': self.author,
            'review': self.review
        }