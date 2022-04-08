import string
import random
import uuid


def generate_random_string(length: int) -> str:
    generated_id = random.choice(string.ascii_lowercase, k=length)
    id = ''.join(generated_id)

    return id


def random_uuid(self, length: int) -> str:
    return str(uuid.uuid4())[:length]


def random_uuid2(self, length: int) -> str:
    return uuid.uuid4().hex[:length]
