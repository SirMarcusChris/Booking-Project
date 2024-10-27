from enum import Enum

class Users(Enum): # наследуем класс Enum. Enum - Create a collection of name/value pairs.
    USERNAME = "admin"
    PASSWORD = "password123"

class Timeouts(Enum):
    TIMEOUT = 5
