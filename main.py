from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP

def toBase64(string):
    return base64.b64encode(string)

def genKeys():
    privateKey = RSA.generate(1024,Random.new().read)
    publickey = privateKey.public_key()
    return privateKey, publickey

# private,public = genKeys()

# real_private_key=private.exportKey()
# real_public_key=public.export_key()

# print(private_key.decode(),public_key.decode())
data="2455"

real_private_key="""
MIICXAIBAAKBgQCXaHFYCspNa+IiFsX90Cjw4tO+gcmDPE2FFgLIjI0AkypkQ+EZ
2jl3yi8gKS62Ha2rLZauLZt/H8oAIvT3AS1F2norCJjeB/4GFzmuZJenASm7xlHe
rYyFUuyRL7K6xuQL6+jT40j304HQq86LQ+aSy07DhSU1e6B97vUshhdivQIDAQAB
AoGAPccXTEGm1t04mQkqwwvO0K70j8xcISiXRsC65QJ4O+5QQzXxIH/KqAZ+oQQ8
s4E7jdddnncsdbvOS6z3v9sikbeN3/uxP8TsZf7qq6KM25IFyT6auR1x/uRpXUV0
GM7TpucUzM8302j8jhKzYlcatOz7rJAIqvGM1a8al08rP08CQQC6AGtcOms0S9X4
947mYIZ98qe0S8vqFWmsN7zHd+5Ud4vaOtgNzIFRbDaEs0oL3sjHSfvVjzV5Ftj6
hM0xsGGPAkEA0GM8fevA8LFLKkMJa1J2hGYbCnwi5Ky2KKAzrfRm9/qvADmnCCDw
aMNIrgzQEKizOp2Hip7XZGyJ59BMs7S48wJAU3XitrSj7AhnT9rNbUQ8tQEQDU/B
hRzsmNE9zQdcktw9jcO/tJliIYX8BJlqjV7/GqVw8gfbh6Uf4XF7nWM2swJBAIuZ
72xsA1U7cJ9fSXAcTklkHblob/fBvEZ7DCP9Fv4JcjM0bDGF34hPSuFOtBR075zU
63hx8NnV3IzvfnLlHwECQCg431OOMZ0SulenD2YsdcoswlIj8aqpyOM5US1Nmtf/
HzNWF+wt2XfQbCXwaV3JuERIUYGxgtxEYkNGWpujNZ4="""

real_public_key='''
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCXaHFYCspNa+IiFsX90Cjw4tO+
gcmDPE2FFgLIjI0AkypkQ+EZ2jl3yi8gKS62Ha2rLZauLZt/H8oAIvT3AS1F2nor
CJjeB/4GFzmuZJenASm7xlHerYyFUuyRL7K6xuQL6+jT40j304HQq86LQ+aSy07D
hSU1e6B97vUshhdivQIDAQAB
'''


imported_private_key=RSA.importKey(base64.b64decode(real_private_key))
imported_public_key=RSA.importKey(base64.b64decode(real_public_key))

def encrypt(pubKey,data):
    print(pubKey)
    return base64.b64encode(pubKey.encrypt(data.encode(),0)[0])

print(encrypt(imported_public_key,data))