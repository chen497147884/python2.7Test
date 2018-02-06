from hashlib import sha1
import hmac
from base64 import b64encode

hashed = hmac.new('testsecret&', string_to_sign, sha1)
signature = b64encode(hashed.digest())
print signature