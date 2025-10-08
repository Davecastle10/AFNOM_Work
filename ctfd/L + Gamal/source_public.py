from Cryptodome.Random import random
from Cryptodome.Util.number import bytes_to_long

FLAG = b"AFNOM{????????????????????????????????????}"

class ElGamal():
    def __init__(self):
       self.q = 12600908927583695025915922760858062869504898731692176260536498123355811076649093419400976600871355970813118607850398283879552845362863097769033273386072687
       self.g = 6376134701041263881538692443881627157067668610080003727492498791102569951797
       self.x = random.randint(2, self.q)
       self.h = pow(self.g, self.x, self.q) # like rsa encrypt c = m^e % n

    def encrypt(self,m):
       s = pow(self.h, self.x, self.q) # (base, exponent, modulus)
       c1 = pow(self.g, self.x, self.q)
       c2 = (s * m) % self.q
       return (c1, c2)


if __name__ == '__main__':
    chal = ElGamal()
    c1, c2 = chal.encrypt(bytes_to_long(FLAG))
    print(f'Ciphertext: ({hex(c1)}, {hex(c2)})')
    print(f'Public key: {chal.h}')
    msg = input('Enter text to input (as hex): ')
    rm = int(msg, 16)
    c_1,c_2 = chal.encrypt(rm)
    print(f'Ciphertext: ({hex(c_1)}, {hex(c_2)})')
