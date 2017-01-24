import rsa
(pubkeya, privkeya) = rsa.newkeys(512, poolsize=2)
print(pubkeya)
print(privkeya)
kutas=pubkeya.save_pkcs1('PEM')
plik= open('pubkey','w')
plik.write(kutas)

penis=privkeya.save_pkcs1('PEM')
plik= open('privkey','w')
plik.write(penis)
