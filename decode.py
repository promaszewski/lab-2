import rsa
plik= open("encode.txt","r")

plik1= plik.read()
plik.close()
from binascii import unhexlify
aplik= open("encode.txt","w")
aplik.write(plik1.decode("hex"))
aplik.close()
with open('privkey') as privatefile:
	keydata = privatefile.read()
	privkey =  rsa.PrivateKey.load_pkcs1(keydata)
from rsa.bigfile import *
with open('encode.txt', 'rb') as infile, open('decode.txt', 'wb') as outfile:
	decrypt_bigfile(infile, outfile, privkey)

