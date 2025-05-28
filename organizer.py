from person import Person


class Organizer(Person):
    def __init__(self, name: str, cpf: str, age: str, address: str, role: str):
        super().__init__(name, cpf, age, address)
        self._role = role

    @property
    def role(self) -> str:
        return self._role

    @role.setter
    def role(self, value: str):
        self._role = value

    def request_event(self):
        print(f"Organizer {self.name} ({self.cpf}) is requesting a new event.")
        pass

    def authenticate(self) -> bool:
        print(f"Authenticating organizer: {self.name}")
        return True
