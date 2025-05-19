from person import Person

class Organizer(Person):
    def __init__(self, name, cpf, age, adress, role: str):
        self._role = role
        super().__init__(name, cpf, age, adress)
    
    def request_event():
        pass
    
    def autentheticate():
        pass