from faker import Faker
from data.data import Person

faker = Faker()

def generated_person():
    yield Person(
        full_name=faker.name(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address(),
    )