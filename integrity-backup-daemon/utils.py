import hashlib
import base64

def hashing_function(my_file):
    return hashlib.sha256(my_file.encode()).hexdigest() # Encodeaza stringul inainte de a aplica sha256 hashing

# def encoding_function(my_file):
#     return base64.b64encode(my_file)