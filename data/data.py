from dataclasses import dataclass, field
from faker import Faker

faker = Faker()

@dataclass
class Person:
    full_name: str = field(default_factory=lambda: faker.name())
    email: str = field(default_factory=lambda: faker.email())
    current_address: str = field(default_factory=lambda: faker.address())
    permanent_address: str = field(default_factory=lambda: faker.address())