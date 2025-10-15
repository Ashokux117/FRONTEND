import secrets
import string

def generate_api_key(length=32):
    # yaha tum jitne characters chaho allow kar sakte ho
    characters = string.ascii_letters + string.digits  
    # ascii_letters = ABC...xyz + abc...xyz
    # digits = 0-9
    api_key = ''.join(secrets.choice(characters) for _ in range(length))
    return api_key

api_key = generate_api_key()
print(api_key)
