from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, cpf: str, age: str, address: str):
        self._name = name
        self._cpf = cpf  # CPF can serve as a unique ID for persons
        self._age = age
        self._address = address

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def age(self) -> str:
        return self._age

    @age.setter
    def age(self, value: str):
        self._age = value

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str):
        self._address = value

    @abstractmethod
    def authenticate(self) -> bool:
        """Authenticates the person."""
        pass
