from faker import Faker

faker = Faker()
user_db = []


def generate_user_mock_data(size):
    for i in range(size):
        yield {
            'id': i+1,
            'first_name': faker.first_name(),
            'last_name': faker.last_name(),
            'email': faker.email(),
            'phone': faker.phone_number(),
            'address': faker.street_address(),
            'city': faker.city(),
            'state': faker.state(),
            'country': faker.country()
        }


def get_user_data(size):
    #user_db.clear()
    if len(user_db) == 0:
        for data in generate_user_mock_data(size):
            user_db.append(data)

    return user_db


def get_user_by_id(user_id):
    user = list(filter(lambda user: user['id'] == user_id, user_db))
    return user


def add_user(user):
    last_id = 0
    if len(user_db) > 0:
        last_id = user_db[-1]['id']
    _user = user.dict()
    _user['id'] = last_id + 1
    user_db.append(_user)
    return True
