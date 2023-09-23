import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random student ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A student in a school."""
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Set the login to the first letter of the name and the surname."""
        self.login = self.name[0] + self.surname
