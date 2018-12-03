ciphertext= 'hej vektor. denna angen blev det mycket svarare'    #'2e000d1f0e190d011d4813c295181554011c0f1a410a4b0318070b0b1c4f'
key='hackathon'

M=ciphertext
K=key


def xor(M,K):
    E=''
    for i,c in enumerate(M):
        k = ord(K[i%len(K)])
        E += chr(ord(c) ^ k)    # xor
    return E

E = xor(M, K)
Mprime = xor(E, K)

import binascii
def hexdump(x):
    return binascii.hexlify(x.encode())

print('Original', hexdump(M))
print('        ', M)
print('Encrypted', hexdump(E))
print('        ')
print('Decrypted', hexdump(Mprime))
print('        ', Mprime)