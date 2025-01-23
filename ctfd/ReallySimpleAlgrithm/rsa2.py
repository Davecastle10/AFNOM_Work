# uses n, e, d to calcualte M

h = (pow(5189205821715720347521652982774921966138647958872467797572,2660999334261448452922645074562350060142352651227539822209, 5592416411284394152744721339669598822174066776228429413003))

#the hex of the decrypted message
print (hex(h))

# the text obtained form the hex when converted to ascii? and reveresd
txt = "}LL4M5_O0T_N{MONFA"[::-1]
print(txt)# the flag printed properly
