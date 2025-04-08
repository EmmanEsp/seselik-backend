from faker import Faker

from app.customer.domain.requests.customer_request import CustomerRequest

fake = Faker()

CREATE_CUSTOMER_REQUEST_DATA = {
    "firstName": fake.first_name(),
    "lastName": fake.last_name(),
    "phoneNumber": fake.phone_number(),
    "email": fake.email(),
    "password": fake.password(length=24),
}

CREATE_CUSTOMER_REQUEST_MOCK = CustomerRequest(**CREATE_CUSTOMER_REQUEST_DATA)
