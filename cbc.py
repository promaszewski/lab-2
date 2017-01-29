from Crypto.Cipher import AES
from Crypto import Random
from binascii import unhexlify

plik = open('aescbc.txt', 'r')
cz = plik.read().splitlines()

a = unhexlify(cz[1])
klucz = unhexlify(cz[0])

c = AES.new(klucz, AES.MODE_CBC, a)

msg = a + c.decrypt(unhexlify(cz[2]))

print (msg)
