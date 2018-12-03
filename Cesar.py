#alphabet='abcdefghijklmnopqrstuvxyz'
#ciphertext='zuhnigyh bul nci ncalulm mnsleu'
#ciphertext='fungerar'
ciphertext='Figaro vegetarisk'
skift=20
mode='kryptera'
def cesar(ciphertext,skift, mode):
    output=[]
    if mode=='dekryptera':
        for x in ciphertext:
            if ord(x)-skift<97:
                output.append(chr(ord(x)+26-skift))
            else:
                output.append(chr(ord(x) - skift))
    elif mode=='kryptera':
        for x in ciphertext:
            if ord(x) + skift > 122:
                output.append(chr(ord(x) - 26 + skift))
            else:
                output.append(chr(ord(x) + skift))
    return ''.join(output)

print(cesar(ciphertext,skift,mode))
''''
for x in ciphertext:
    ord(x)
    '''