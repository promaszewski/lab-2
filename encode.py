import rsa
with open('pubkey') as privatefile:
	keydata = privatefile.read()
	pubkey =  rsa.PublicKey.load_pkcs1(keydata)
from rsa.bigfile import *
with open('tekst.txt', 'rb') as infile, open('encode.txt', 'wb') as outfile:
	encrypt_bigfile(infile, outfile, pubkey)
plik= open("encode.txt","r")

plik1= plik.read()
plik.close()
from binascii import unhexlify
aplik= open("encode.txt","w")
aplik.write(plik1.encode("hex"))
aplik.close()
