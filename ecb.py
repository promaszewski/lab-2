
from Crypto.Cipher import AES
from Crypto import Random
from binascii import unhexlify

plik = open('kluczecb.txt', 'r')
cz = plik.read().splitlines()
klucz = unhexlify(cz[0])

a = Random.new().read(AES.block_size)
c = AES.new(klucz, AES.MODE_ECB, a)

msg = a + c.decrypt(unhexlify(cz[1]))
print (msg)

