import random
import string


def generate_uuid(uuid_length: int = 8) -> str:
    # chars = string.printable
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(uuid_length))


print(generate_uuid())
print(generate_uuid(10))
