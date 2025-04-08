from faker import Faker

from app.customer.domain.models.customer_model import CustomerModel

fake = Faker()


CUSTOMER_MODEL_DATA = {
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "phone_number": fake.phone_number(),
    "email": fake.email(),
    "password": fake.password(length=24),
}

CUSTOMER_MODEL_MOCK = CustomerModel(**CUSTOMER_MODEL_DATA)
