a=2
b=1
c=1

aANDb = a & b
bXORc = b ^ c
bORc = b | c
g = bXORc & bORc

final = aANDb ^ g

print("q = ",final)