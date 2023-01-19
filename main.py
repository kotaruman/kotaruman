import random 
import string

def generate_password(size =8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(size)) 

print(generate_password())