from Cryptodome.Util.number import *
#from flag import secret

#want to find out what secret was

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 1

#enc = pow(secret, e, n)
print('n =', n)
print('e =',e)
#print('c =', enc)



#outppus of original run?
#150155341283781612667945486411409499728931469785857915938586786139361490570601976305507430049333117
print(hex(150155341283781612667945486411409499728931469785857915938586786139361490570601976305507430049333117))