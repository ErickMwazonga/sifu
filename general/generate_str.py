import string
import random
import uuid


def generate_random_string(length: int) -> str:
    generated_id = random.choice(string.ascii_lowercase, k=length)
    _id = ''.join(generated_id)

    return _id


def random_uuid(length: int) -> str:
    return str(uuid.uuid4())[:length]


def random_uuid_v2(length: int) -> str:
    return uuid.uuid4().hex[:length]
