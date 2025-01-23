# code obtained from the internet and modified to fit the challenge
# think this link was the main page whose subpage i got the code from
#https://0xb0b.gitbook.io/writeups/tryhackme/2024/breaking-rsa

import gmpy2
from Cryptodome.PublicKey import RSA

def fermat_factorization(n):
    """Fermat's Factorization Method"""
    a = gmpy2.isqrt(n) + 1
    b2 = gmpy2.square(a) - n
    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n
    p = a + gmpy2.isqrt(b2)
    q = a - gmpy2.isqrt(b2)
    return p, q

def calculate_private_key(p, q, e):
    """Calculate the private key 'd'"""
    phi = (p - 1) * (q - 1)
    d = gmpy2.invert(e, phi)
    return d
"""
# Open the RSA key file
with open("id_rsa.pub", "r") as f:
    # Import the RSA key
    key = RSA.import_key(f.read())

# Retrieve the modulus (n) and public exponent (e)
n = key.n
e = key.e
"""
n = 169110111150246174221951591062214641241271111718815524654288210424833123127173150112140251238120878758198621586155681764225225225321760331311382495154109226429722162163222225192184871961478914521711220128776162134322458212471039532244301621751871121922261671557312014549194242143232337569621953581541281472201191212361321244323410514101615614247175244892267156205548921723723114922420924813031213180146362037117410224917460882501022199416924761123116255741383646145347915221824010030138143241155882511407317716517117689244667322321417818121161682041244416214787175701692202401741474811914324118316822883332011683207232395833171735119123516218242412716616717514239
e = 1601



# Print the modulus and public exponent
print("\033[96mModulus (n):\033[0m", n)
print("\033[96mPublic Exponent (e):\033[0m", e)

# Factorize n into p and q using Fermat's Factorization
# inefficent so use online calc from bookmarks
#p, q = fermat_factorization(n)

p = 74727135712875084008830410637
q = 74837826419203310244891545719

# Calculate private key 'd' using p, q, and public exponent 'e'
d = calculate_private_key(p, q, e)

difference = abs(p - q)
print("\033[93mp:\033[0m", p)
print("\033[93mq:\033[0m", q)
print("\033[93mDifference between q and p:\033[0m", difference)
print("\033[96mPrivate Key (d):\033[0m", d)


key_params = (n, e, d, p, q)
key = RSA.construct((n,e,int(d)))

# Export the private key to a file
"""
with open('id_rsa', 'wb') as f:
    f.write(key.export_key('PEM'))

print("\033[92mPrivate key generated and saved as 'id_rsa'.\033[0m")
"""