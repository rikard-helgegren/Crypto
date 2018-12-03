ciphertext ='jag kommer har att formedla ett mycket hemligt medaelande som ingen far lasa'
key = 'crypted'
alphabet='abcdefghijklmnopqrstuvwxyz'
values=[]
output=[]
mode='crypt'
#mode='decrypt'

def vigenere(ciphertext,key,alphabet,mode):
    for x in key:
        values.append(ord(x) - 97)
    counter = 0
    if mode=='decrypt':
        for x in ciphertext:
            if x in alphabet:
                if ord(x) - values[counter]>96:
                    output.append(chr(ord(x)-values[counter]))
                    counter += 1
                    if counter==len(key):
                        counter=0

                else:
                    output.append(chr(ord(x)-values[counter]+26))
                    counter += 1
                    if counter==len(key):
                        counter=0
            else:
                output.append(x)
    elif mode=='crypt':
        for x in ciphertext:
            if x in alphabet:
                if ord(x) + values[counter] < 123:
                    output.append(chr(ord(x) + values[counter]))
                    counter += 1
                    if counter == len(key):
                        counter = 0

                else:
                    output.append(chr(ord(x) + values[counter] - 26))
                    counter += 1
                    if counter == len(key):
                        counter = 0
            else:
                output.append(x)
    return ''.join(output)

print(vigenere(ciphertext,key,alphabet,mode))