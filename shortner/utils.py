import random, string

def generate_short_path():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))