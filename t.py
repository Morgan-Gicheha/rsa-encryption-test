import rsa

# generate public and private keys with
# rsa.newkeys method,this method accepts
# key length as its parameter
# key length should be atleast 16
(publicKey, privateKey) = rsa.newkeys(512)
rsa.PublicKey
print("###publick key###",publicKey,"###publick key###")
print("###privateKey key###",privateKey,"###privateKey key###")
# this is the string that we will be encrypting
message = "hello geeks"

# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method
encMessage = rsa.encrypt(message.encode(),
						"8156675980327170096655570111977226566575680364198596742079726741713043611326772887316653900160544446462113921577079947226987906430362851235698950892060159")

print("original string: ", message)
print("encrypted string: ", encMessage)

# the encrypted message can be decrypted
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption
decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("decrypted string: ", decMessage)
