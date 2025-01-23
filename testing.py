# can't remeber what this was for

from pwn import *
cipherText = ""

cipherText = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

#print(b64e(b'\xe3\xdd\xbb\xe9\xdd\xb4\xe9\xbe\xbd\xe9\xce\x9c\xeb\xde\x9e\xeb\xbd\xb4\xef\xde\x9f\xef\x9e\xf6\xdbN\xb6\xefn\xb5\xeb\xde\x9e\xdbN\x9c\xeb\xde\x9b\xeb\x9d\xb4\xeb]\xb4\xefN\x9f\xeb\xde\xf7\xe9\xfe\x9e\xe9\xfe\xf9\xef}\xb4\xe9\xde\xf9\xef~\xbc\xefn\x9f\xe9\xfe\x9d'))
#print(b64e(unhex(cipherText)))
#print(unhex(cipherText))

#print(xor(b'unhex(1c0111001f010100061a024b53535009181c)', b'686974207468652062756c6c277320657965'))

#print(xor(b64e(unhex("1c0111001f010100061a024b53535009181c")), '686974207468652062756c6c277320657965'))

text = "1c0111001f010100061a024b53535009181c"
key = "686974207468652062756c6c277320657965"

print(enhex(xor(unhex(text), unhex(key))))